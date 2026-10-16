"""Pre-render: buat _callout-index.json untuk callout-buku.lua.

Indeks berisi nomor bab tiap berkas dan label setiap callout bernomor yang
punya id, sehingga rujukan seperti @kasus-jarak-hunian bisa dicetak sebagai
"Studi Kasus 6.3" dan ditautkan walaupun callout-nya ada di bab lain.

Nomor bab = urutan bab dalam book.chapters (dan book.appendices) yang judul
H1-nya tidak bertanda {.unnumbered} atau {-}. Nomor callout = urutan
kemunculan per jenis di dalam bab. Aturan yang sama dipakai filter Lua saat
indeks tidak tersedia.

Skrip ini hanya memakai pustaka standar Python dan dijalankan dari direktori
proyek (tempat _quarto.yml berada).
"""

import json
import re
import sys

NUMBERED = {
    "capaian": "Capaian Pembelajaran Bab {bab}",
    "kasus": "Studi Kasus {bab}.{n}",
    "latihan": "Soal Latihan {bab}.{n}",
}

FENCE = re.compile(r"^\s*:{3,}\s*\{([^}]*)\}")
H1 = re.compile(r"^#\s+(.*)$")
CODE = re.compile(r"^\s*(```|~~~)")


def chapter_files(config_text):
    """Ambil daftar .qmd dari book.chapters dan book.appendices, urut."""
    files = []
    in_list = False
    for line in config_text.splitlines():
        stripped = line.strip()
        if stripped in ("chapters:", "appendices:"):
            in_list = True
            continue
        if in_list:
            m = re.match(r"^-\s+(?:part:\s+)?([^\s#]+\.qmd)\s*$", stripped)
            if m:
                files.append(m.group(1))
            elif stripped.startswith("- "):
                continue
            elif stripped and not stripped.startswith("#"):
                in_list = False
    return files


def scan(path):
    """Kembalikan (bab_bernomor, [(jenis, id), ...]) untuk satu berkas."""
    with open(path, encoding="utf-8-sig") as f:
        lines = f.read().splitlines()
    numbered = None
    callouts = []
    in_code = False
    for line in lines:
        if CODE.match(line):
            in_code = not in_code
            continue
        if in_code:
            continue
        if numbered is None:
            m = H1.match(line)
            if m:
                attrs = re.search(r"\{([^}]*)\}\s*$", m.group(1))
                tokens = attrs.group(1).split() if attrs else []
                numbered = not ("-" in tokens or ".unnumbered" in tokens)
        m = FENCE.match(line)
        if m:
            attrs = m.group(1)
            classes = re.findall(r"(?:^|\s)\.([\w-]+)", attrs)
            kind = next((c for c in classes if c in NUMBERED), None)
            if kind:
                ident = re.search(r"(?:^|\s)#([\w:.-]+)", attrs)
                callouts.append((kind, ident.group(1) if ident else None))
    return bool(numbered), callouts


def build(config_path="_quarto.yml"):
    with open(config_path, encoding="utf-8") as f:
        files = chapter_files(f.read())
    index = {"chapters": {}, "callouts": {}}
    bab = 0
    for path in files:
        try:
            numbered, callouts = scan(path)
        except FileNotFoundError:
            print(f"indeks_callout: {path} tidak ditemukan", file=sys.stderr)
            continue
        if not numbered:
            continue
        bab += 1
        index["chapters"][path] = bab
        counters = {}
        html = re.sub(r"\.qmd$", ".html", path)
        for kind, ident in callouts:
            counters[kind] = counters.get(kind, 0) + 1
            if ident is None:
                continue
            if ident in index["callouts"]:
                print(f"indeks_callout: id ganda '{ident}' di {path}", file=sys.stderr)
            index["callouts"][ident] = {
                "label": NUMBERED[kind].format(bab=bab, n=counters[kind]),
                "file": html,
            }
    return index


if __name__ == "__main__":
    with open("_callout-index.json", "w", encoding="utf-8") as f:
        json.dump(build(), f, ensure_ascii=False, indent=1)
