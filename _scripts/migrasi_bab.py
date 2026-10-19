"""Migrasi mekanis satu bab dari sintaks Bookdown ke Quarto.

Pemakaian (dari akar proyek):
    python _scripts/migrasi_bab.py 06-estimasi-parameter.qmd

Yang dikerjakan:
  - blok rmdcapaian/rmdkasus/rmdexercise/rmdnote -> callout baru
    (.capaian/.kasus/.latihan/.catatan/.penting), heading judul -> title
  - persamaan (\\#eq:x) dan \\begin{equation} -> $$ ... $$ {#eq-x}
  - chunk {r label, opsi=...} -> {r} + #| label/opsi gaya Quarto;
    label grafik diberi awalan fig-, label tabel tbl-, caption kbl() -> tbl-cap
  - \\@ref(fig:x)/\\@ref(tab:x)/\\@ref(eq:x)/\\@ref(sec) -> @fig-/@tbl-/@eq-/@sec-
    (kata "Gambar/Tabel/Persamaan" di depannya dibuang; Quarto menambahkannya)
  - chunk setup source("_common.R"), BOM, mojibake, baris kosong sebelum daftar

Hasilnya tetap perlu ditinjau manual (skill migrasi-bab): judul callout,
heading lain di dalam callout, rujukan subbab ke bab lain, dan sisa yang
dilaporkan sebagai PERIKSA.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lint_buku  # noqa: E402

SETUP = '```{r}\n#| label: setup\n#| include: false\nsource("_common.R")\n```\n'

OPT_MAP = {
    "fig.cap": "fig-cap",
    "fig.align": "fig-align",
    "fig.width": "fig-width",
    "fig.height": "fig-height",
    "out.width": "out-width",
    "out.height": "out-height",
    "echo": "echo",
    "eval": "eval",
    "include": "include",
    "results": "output",
    "message": "message",
    "warning": "warning",
}
# Sudah menjadi bawaan di _common.R
DEFAULTS = {("echo", "false"), ("message", "false"), ("warning", "false")}
# Khusus LaTeX, dibuang
DROP = {"fig.pos", "crop"}

notes = []


def note(msg):
    notes.append(msg)


def slug(text, maxwords=6):
    text = re.sub(r"\$[^$]*\$", "", text)
    text = re.sub(r"[*_`]", "", text).lower()
    words = re.findall(r"[a-z0-9]+", text)
    return "-".join(words[:maxwords])


def fig_label(label):
    return label if label.startswith("fig-") else "fig-" + label


def tbl_label(label):
    if label.startswith("tbl-"):
        return label
    return "tbl-" + re.sub(r"^(tab|tabel)-", "", label)


def yaml_value(value):
    v = value.strip()
    if v in ("TRUE", "T"):
        return "true"
    if v in ("FALSE", "F"):
        return "false"
    if re.fullmatch(r"-?[\d.]+", v):
        return v
    m = re.fullmatch(r"""(['"])(.*)\1""", v, re.S)
    if m:
        v = m.group(2)
    return "'" + v.replace("'", "''") + "'"


def split_options(text):
    """Pisah 'a, b=1, c="x, y"' dengan memperhatikan tanda kutip."""
    parts, buf, quote, depth = [], "", None, 0
    for ch in text:
        if quote:
            buf += ch
            if ch == quote:
                quote = None
        elif ch in "'\"":
            quote = ch
            buf += ch
        elif ch in "([":
            depth += 1
            buf += ch
        elif ch in ")]":
            depth -= 1
            buf += ch
        elif ch == "," and depth == 0:
            parts.append(buf.strip())
            buf = ""
        else:
            buf += ch
    if buf.strip():
        parts.append(buf.strip())
    return parts


# ---------------------------------------------------------------------------


def convert_chunks(lines, fig_labels, tbl_labels):
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^(\s*)```\{r\s*(.*)\}\s*$", line)
        if not m or not m.group(2).strip():
            out.append(line)
            i += 1
            continue
        indent = m.group(1)
        parts = split_options(m.group(2).lstrip(",").strip())
        label = None
        opts = []
        for p in parts:
            if "=" not in p:
                label = p
                continue
            key, val = p.split("=", 1)
            key = key.strip()
            if key in DROP:
                continue
            if key == "label":
                label = val.strip().strip("'\"")
                continue
            qkey = OPT_MAP.get(key)
            if not qkey:
                note(f"PERIKSA opsi chunk tak dikenal '{key}' pada chunk '{label}'")
                qkey = key
            yv = yaml_value(val)
            if (qkey, yv) in DEFAULTS:
                continue
            opts.append((qkey, yv))

        # Badan chunk
        j = i + 1
        while j < len(lines) and not lines[j].lstrip().startswith("```"):
            j += 1
        body = lines[i + 1 : j]

        has_cap = any(k == "fig-cap" for k, _ in opts)
        if label and (has_cap or label in fig_labels):
            label = fig_label(label)
        elif label and label in tbl_labels:
            label = tbl_label(label)
            text = "\n".join(body)
            cm = re.search(r"""\n?\s*caption\s*=\s*(["'])(.*?)\1\s*,?""", text)
            if cm:
                opts.append(("tbl-cap", yaml_value(cm.group(1) + cm.group(2) + cm.group(1))))
                text = text[: cm.start()] + text[cm.end() :]
                body = text.split("\n")
            else:
                note(f"PERIKSA tabel '{label}': caption tidak ditemukan, tambahkan #| tbl-cap")

        out.append(indent + "```{r}")
        if label:
            out.append(f"{indent}#| label: {label}")
        for k, v in opts:
            out.append(f"{indent}#| {k}: {v}")
        out.extend(body)
        if j < len(lines):
            out.append(lines[j])
        i = j + 1
    return out


def convert_equations(lines):
    out = []
    i = 0
    while i < len(lines):
        if lines[i].strip() != "$$":
            out.append(lines[i])
            i += 1
            continue
        j = i + 1
        while j < len(lines) and not lines[j].strip().startswith("$$"):
            j += 1
        block = lines[i + 1 : j]
        label = None
        kept = []
        for b in block:
            m = re.search(r"\(\\#eq:([\w-]+)\)", b)
            if m:
                label = m.group(1)
                b = b[: m.start()] + b[m.end() :]
            if b.strip() in ("\\begin{equation}", "\\end{equation}"):
                continue
            if b.strip():
                kept.append(b.rstrip())
        out.append("$$")
        out.extend(kept)
        close = lines[j] if j < len(lines) else "$$"
        out.append(close.rstrip() + (f" {{#eq-{label}}}" if label else ""))
        i = j + 1
    return out


def convert_blocks(lines, bab_slug):
    out = []
    i = 0
    counters = {}
    while i < len(lines):
        m = re.match(r"^(:{3,})\s*\{?\s*\.?(rmdcapaian|rmdkasus|rmdexercise|rmdnote)\s*\}?\s*$", lines[i])
        if not m:
            out.append(lines[i])
            i += 1
            continue
        fence, legacy = m.group(1), m.group(2)
        j = i + 1
        while j < len(lines) and not lines[j].strip():
            j += 1
        first = lines[j] if j < len(lines) else ""
        title = None
        hm = re.match(r"^#{1,6}\s+(.*?)\s*(\{[^}]*\})?\s*$", first)
        tm = re.match(r"^\[(.*)\]\{\.tajuksaya\}\s*$", first)
        if hm:
            title = hm.group(1)
            consumed = j
        elif tm:
            title = tm.group(1)
            consumed = j
        else:
            consumed = None

        kind = {"rmdcapaian": "capaian", "rmdkasus": "kasus", "rmdexercise": "latihan", "rmdnote": "catatan"}[legacy]
        if title:
            title = re.sub(r"^(Studi Kasus|Catatan|Soal (Evaluasi|Latihan)\s*\d*)\s*:?\s*", "", title).strip()
            if re.match(r"(?i)^(⚠️\s*)?penting", title):
                kind = "penting"
                title = re.sub(r"(?i)^(⚠️\s*)?penting!?\s*:?\s*", "", title)
            if kind == "capaian" or re.fullmatch(r"(?i)catatan|penting!?", title or ""):
                title = None
        counters[kind] = counters.get(kind, 0) + 1

        attrs = []
        if kind == "capaian":
            attrs.append(f"#capaian-{bab_slug}")
        elif kind == "kasus":
            attrs.append(f"#kasus-{slug(title) if title else bab_slug + '-' + str(counters[kind])}")
        elif kind == "latihan":
            attrs.append(f"#latihan-{bab_slug}-{counters[kind]}")
        attrs.append("." + kind)
        if title:
            attrs.append('title="' + title.replace('"', "'") + '"')
        if kind == "kasus" and not title:
            note("PERIKSA studi kasus tanpa judul: tambahkan title")
        out.append(f"{fence} {{{' '.join(attrs)}}}")
        if consumed is not None:
            i = consumed + 1
            while i < len(lines) and not lines[i].strip():
                i += 1
        else:
            i += 1
    return out


def convert_refs(text, ids_in_file):
    prefix = r"(?:(?:Gambar|Tabel|Persamaan|gambar|tabel|persamaan)\s+)?"

    def fig(m):
        return "@" + fig_label(m.group(1))

    def tab(m):
        return "@" + tbl_label(m.group(1))

    def sec(m):
        target = m.group(1)
        if target not in ids_in_file:
            note(f"PERIKSA @sec-{target}: tambahkan {{#sec-{target}}} pada heading tujuan (mungkin di bab lain)")
        return "@sec-" + target

    text = re.sub(prefix + r"\\@ref\(fig:([\w-]+)\)", fig, text)
    text = re.sub(prefix + r"\\@ref\(tab:([\w-]+)\)", tab, text)
    text = re.sub(prefix + r"\\@ref\(eq:([\w-]+)\)", lambda m: "@eq-" + m.group(1), text)
    text = re.sub(r"\\@ref\(([\w-]+)\)", sec, text)
    return text


def migrate(path):
    with open(path, encoding="utf-8-sig") as f:
        text = f.read()
    text = "\n".join(lint_buku.fix_mojibake(line) for line in text.split("\n"))

    bab_slug = re.sub(r"^\d+-", "", os.path.basename(path)).replace(".qmd", "")
    fig_labels = set(re.findall(r"\\@ref\(fig:([\w-]+)\)", text))
    tbl_labels = set(re.findall(r"\\@ref\(tab:([\w-]+)\)", text))
    tbl_labels |= {
        m.group(1)
        for m in re.finditer(r"```\{r\s+([\w-]+)[^}]*\}\n(?:(?!```).*\n)*?.*kbl\(", text)
    }

    lines = text.split("\n")
    lines = convert_blocks(lines, bab_slug)
    lines = convert_equations(lines)
    lines = convert_chunks(lines, fig_labels, tbl_labels)
    text = "\n".join(lines)

    # Id subbab Bookdown {#x} -> {#sec-x}
    sec_ids = set(re.findall(r"^#{1,6} .*\{#(?!sec-)([\w-]+)[^}]*\}", text, re.M))
    for sid in sec_ids:
        text = re.sub(r"\{#" + re.escape(sid) + r"([\s}])", r"{#sec-" + sid + r"\1", text)
    text = convert_refs(text, sec_ids)

    if "source(\"_common.R\")" not in text:
        text = SETUP + "\n" + text

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    # Rapikan yang mekanis (baris kosong sebelum daftar, dsb.)
    lint_buku.lint(path, lint_buku.collect_ids(sorted(__import__("glob").glob("*.qmd"))), fix=True)


if __name__ == "__main__":
    for p in sys.argv[1:]:
        notes.clear()
        migrate(p)
        print(f"== {p}")
        for n in notes:
            print("  " + n)
    print("\nLanjutkan dengan: python _scripts/lint_buku.py <berkas>")
