"""Linter aturan penulisan buku.

Pemakaian (dari akar proyek):
    python _scripts/lint_buku.py                 # semua *.qmd di akar
    python _scripts/lint_buku.py 06-*.qmd        # berkas tertentu
    python _scripts/lint_buku.py --fix 06-*.qmd  # perbaiki yang mekanis

Galat (keluar dengan kode 1):
  daftar      butir daftar tidak didahului baris kosong            [--fix]
  bom         berkas diawali BOM UTF-8                              [--fix]
  mojibake    teks rusak encoding, mis. "â€”" atau "Ã—"             [--fix]
  bookdown    sisa sintaks Bookdown: \\@ref(), (\\#...), ::: rmd...
  callout     callout bernomor tanpa id/berprefiks salah, studi kasus tanpa title,
              id ganda, atau heading di dalam callout
  rujukan     @fig-/@tbl-/@eq-/@sec-/@kasus-/@latihan-/@capaian- ke label
              yang tidak ada di bab mana pun
  tabel       font_size pada tabel (huruf tabel diatur global)

Peringatan (tinjau manual, lihat skill tinjau-bab):
  meta        frasa yang sering menandai meta-commentary
"""

import glob
import re
import sys

NUMBERED = ("capaian", "kasus", "latihan")
ALL_KINDS = NUMBERED + ("penting", "catatan")

LIST_ITEM = re.compile(r"^\s{0,3}([-*+]|\d+[.)]|[a-zA-Z][.)])\s+\S")
FENCE_OPEN = re.compile(r"^\s*(:{3,})\s*\{([^}]*)\}")
FENCE_LEGACY = re.compile(r"^\s*:{3,}\s*\{?\s*\.?(rmd\w+)")
FENCE_CLOSE = re.compile(r"^\s*(:{3,})\s*$")
CODE = re.compile(r"^\s*(```|~~~)")
REF = re.compile(r"(?<![\w@])@((?:fig|tbl|eq|sec|kasus|latihan|capaian)-[\w:-]*\w)")
LABEL_ATTR = re.compile(r"\{#([\w:.-]+)")
LABEL_CHUNK = re.compile(r"^\s*#\|\s*label:\s*(\S+)")

BOOKDOWN = [
    (re.compile(r"\\@ref\("), "\\@ref() -> @fig-/@tbl-/@eq-/@sec-"),
    (re.compile(r"\(\\#(eq|fig|tab):"), "label (\\#...) -> {#eq-...} atau #| label:"),
    (re.compile(r"\{\.tajuksaya\}"), ".tajuksaya -> teks tebal, atau callout .penting/.catatan"),
    (re.compile(r"^#\s+\(APPENDIX\)"), "(APPENDIX) -> book.appendices di _quarto.yml"),
]

META = [
    r"akan kita gunakan untuk (menjelaskan|mengilustrasikan)",
    r"data fiktif",
    r"bayangkan (saya|kami) (sedang )?berbicara",
    r"di bawah ini akan",
    r"pada (bagian|subbab) ini (kita )?akan",
    r"seperti (sedang )?berbicara kepada",
    r"agar (anda|kalian) (lebih )?paham",
]
META = [re.compile(p, re.IGNORECASE) for p in META]

# Karakter yang muncul ketika teks UTF-8 dibaca sebagai CP1252/Latin-1.
MOJIBAKE_RUN = re.compile(
    "[\u00c2-\u00f4][\u0080-\u00ff\u0152\u0153\u0160\u0161\u0178\u017d\u017e"
    "\u0192\u02c6\u02dc\u2013\u2014\u2018-\u201e\u2020-\u2022\u2026\u2030"
    "\u2039\u203a\u20ac\u2122]+"
)


def to_bytes(text):
    out = bytearray()
    for ch in text:
        if ord(ch) < 256:
            out.append(ord(ch))
        else:
            out.extend(ch.encode("cp1252"))
    return bytes(out)


def fix_mojibake(line):
    def repl(m):
        try:
            fixed = to_bytes(m.group(0)).decode("utf-8")
        except (UnicodeEncodeError, UnicodeDecodeError):
            return m.group(0)
        # Hasil berupa aksara Ibrani/Arab dsb. berarti ini sampah, bukan
        # mojibake yang bisa dipulihkan; biarkan untuk dihapus manual.
        if any(0x0590 <= ord(c) <= 0x08FF for c in fixed):
            return m.group(0)
        return fixed

    return MOJIBAKE_RUN.sub(repl, line)


def parse_attrs(attrs):
    classes = re.findall(r"(?:^|\s)\.([\w-]+)", attrs)
    ident = re.search(r"(?:^|\s)#([\w:.-]+)", attrs)
    title = re.search(r'title\s*=\s*"([^"]*)"', attrs)
    return classes, ident.group(1) if ident else None, title.group(1) if title else None


def collect_ids(files):
    ids = {}
    for path in files:
        with open(path, encoding="utf-8-sig") as f:
            in_code = False
            for n, line in enumerate(f, 1):
                if CODE.match(line):
                    in_code = not in_code
                    continue
                if in_code:
                    m = LABEL_CHUNK.match(line)
                    if m:
                        ids.setdefault(m.group(1), []).append(f"{path}:{n}")
                    continue
                m = FENCE_OPEN.match(line)
                if m:
                    classes, ident, _ = parse_attrs(m.group(2))
                    if ident and any(c in NUMBERED for c in classes):
                        ids.setdefault(ident, []).append(f"{path}:{n}")
                    continue
                for label in LABEL_ATTR.findall(line):
                    ids.setdefault(label, []).append(f"{path}:{n}")
    return ids


def lint(path, ids, fix):
    issues = []
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    has_bom = raw.startswith("\ufeff")
    if has_bom:
        issues.append((1, "bom", "berkas diawali BOM UTF-8", True))
        raw = raw[1:]
    lines = raw.split("\n")
    out = []
    in_code = False
    stack = []  # (panjang fence, jenis callout atau None)
    for i, line in enumerate(lines):
        n = i + 1
        prev = out[-1] if out else ""

        # Mojibake juga dicek di chunk kode: string R ikut tampil di buku.
        fixed = fix_mojibake(line)
        if fixed != line:
            pairs = [(m.group(0), fix_mojibake(m.group(0))) for m in MOJIBAKE_RUN.finditer(line)]
            desc = ", ".join(f"{a!r} -> {b!r}" for a, b in pairs if a != b)
            issues.append((n, "mojibake", desc, True))
            if fix:
                line = fixed
        for junk in MOJIBAKE_RUN.findall(line):
            if fix_mojibake(junk) == junk:
                issues.append((n, "mojibake", f"karakter sampah {junk!r}: hapus atau ganti manual", False))

        if CODE.match(line):
            in_code = not in_code
            if re.match(r"^\s*```\{r\s+[^}]*[=,]", line):
                issues.append((n, "bookdown", "opsi chunk gaya knitr -> #| label/opsi", False))
            out.append(line)
            continue
        if in_code:
            out.append(line)
            continue

        m = FENCE_OPEN.match(line)
        if m:
            classes, ident, title = parse_attrs(m.group(2))
            kind = next((c for c in classes if c in ALL_KINDS), None)
            stack.append((len(m.group(1)), kind))
            if kind in NUMBERED:
                if not ident:
                    issues.append((n, "callout", f".{kind} wajib punya id #{kind}-...", False))
                elif not ident.startswith(kind + "-"):
                    issues.append((n, "callout", f"id #{ident} harus berawalan '{kind}-'", False))
                elif len(ids.get(ident, [])) > 1:
                    issues.append((n, "callout", f"id #{ident} ganda: {', '.join(ids[ident])}", False))
                if kind == "kasus" and not title:
                    issues.append((n, "callout", f'.{kind} wajib punya title="..."', False))
        elif FENCE_LEGACY.match(line):
            issues.append((n, "bookdown", f"blok {FENCE_LEGACY.match(line).group(1)} -> callout baru", False))
            stack.append((3, None))
        elif FENCE_CLOSE.match(line) and stack:
            stack.pop()
        elif line.startswith("#") and any(k for _, k in stack):
            issues.append((n, "callout", "heading di dalam callout (ikut masuk TOC); jadikan title", False))

        if (
            LIST_ITEM.match(line)
            and prev.strip()
            and not LIST_ITEM.match(prev)
            and not prev.startswith((" ", "\t", ":::", "#", "|", "$$", "<", "```"))
        ):
            issues.append((n, "daftar", "butir daftar tanpa baris kosong sebelumnya", True))
            if fix:
                out.append("")

        for pattern, msg in BOOKDOWN:
            if pattern.search(line):
                issues.append((n, "bookdown", msg, False))
        for ref in REF.findall(line):
            if ref not in ids:
                issues.append((n, "rujukan", f"@{ref} tidak ditemukan", False))
        if re.search(r"font_size\s*=", line):
            issues.append((n, "tabel", "jangan atur font_size tabel", False))
        for pattern in META:
            if pattern.search(line):
                issues.append((n, "meta", f"tinjau: '{pattern.search(line).group(0)}'", None))

        out.append(line)

    if fix:
        new = "\n".join(out)
        if new != raw or has_bom:
            with open(path, "w", encoding="utf-8") as f:
                f.write(new)
    return issues


def main(argv):
    fix = "--fix" in argv
    args = [a for a in argv if a != "--fix"]
    files = sorted({p for a in args for p in glob.glob(a)}) if args else sorted(glob.glob("*.qmd"))
    ids = collect_ids(sorted(glob.glob("*.qmd")))
    errors = warnings = fixed = 0
    for path in files:
        for n, rule, msg, fixable in lint(path, ids, fix):
            if fixable is None:
                warnings += 1
                level = "peringatan"
            elif fix and fixable:
                fixed += 1
                level = "diperbaiki"
            else:
                errors += 1
                level = "galat"
            print(f"{path}:{n}: {level} [{rule}] {msg}")
    print(f"\n{errors} galat, {warnings} peringatan" + (f", {fixed} diperbaiki" if fix else ""))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
