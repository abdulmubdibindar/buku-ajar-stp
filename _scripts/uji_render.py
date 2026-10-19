"""Uji render seluruh buku ke HTML dan PDF (Typst) tanpa R.

Menyalin buku ke _uji_render/, mengganti setiap chunk R dengan placeholder
berlabel sama (gambar untuk fig-, tabel untuk tbl-, dibuang untuk lainnya)
dan kode R inline dengan "0", lalu merender. Gunanya memeriksa markup:
callout, persamaan, rujukan silang, sitasi, dan kompilasi Typst. Hasil
komputasi R tidak diperiksa -- untuk itu tetap perlu render penuh.

Pemakaian (dari akar proyek):
    python _scripts/uji_render.py [--quarto /path/ke/quarto]

Keluar dengan kode 1 bila ada render yang gagal atau ada peringatan.
"""

import os
import re
import shutil
import struct
import subprocess
import sys
import zlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from indeks_callout import chapter_files  # noqa: E402

OUT = "_uji_render"
SALIN = ["_quarto.yml", "callout-buku.lua", "style.css", "referensi.bib", "_scripts", "_typst", "images", "figures"]


def png_abu(path, w=300, h=150):
    """Tulis PNG abu-abu polos tanpa pustaka tambahan."""
    def chunk(tag, data):
        return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)

    raw = b"".join(b"\x00" + b"\xcc" * w for _ in range(h))
    with open(path, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n")
        f.write(chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 0, 0, 0, 0)))
        f.write(chunk(b"IDAT", zlib.compress(raw)))
        f.write(chunk(b"IEND", b""))


def ganti_chunk(m):
    indent, body = m.group(1), m.group(0)
    label = re.search(r"#\|\s*label:\s*(\S+)", body)
    cap = re.search(r"#\|\s*(?:fig|tbl)-cap:\s*'(.*)'\s*$", body, re.M)
    teks = cap.group(1).replace("''", "'") if cap else "x"
    if label and label.group(1).startswith("fig-"):
        return f"{indent}![{teks}](_stub.png){{#{label.group(1)}}}"
    if label and label.group(1).startswith("tbl-"):
        return f"{indent}| A | B |\n{indent}|---|---|\n{indent}| 1 | 2 |\n\n{indent}: {teks} {{#{label.group(1)}}}"
    return ""


def siapkan():
    shutil.rmtree(OUT, ignore_errors=True)
    os.makedirs(OUT)
    for p in SALIN:
        if os.path.isdir(p):
            shutil.copytree(p, os.path.join(OUT, p))
        elif os.path.exists(p):
            shutil.copy2(p, OUT)
    png_abu(os.path.join(OUT, "_stub.png"))
    with open("_quarto.yml", encoding="utf-8") as f:
        bab = [p for p, _ in chapter_files(f.read())]
    for path in bab:
        with open(path, encoding="utf-8-sig") as f:
            text = f.read()
        text = re.sub(r"(?ms)^([ \t]*)```\{r\}.*?\n[ \t]*```[ \t]*$", ganti_chunk, text)
        text = re.sub(r"`r [^`]*`", "0", text)
        with open(os.path.join(OUT, path), "w", encoding="utf-8") as f:
            f.write(text)


def render(quarto, args, log):
    with open(os.path.join(OUT, log), "w") as f:
        code = subprocess.call([quarto, "render", *args], cwd=OUT, stdout=f, stderr=subprocess.STDOUT)
    with open(os.path.join(OUT, log)) as f:
        masalah = [line.rstrip() for line in f if re.search(r"WARN|ERROR", line)]
    status = "OK" if code == 0 and not masalah else "GAGAL"
    print(f"{' '.join(args):45} {status}  ({len(masalah)} peringatan/galat, log: {OUT}/{log})")
    for line in masalah[:15]:
        print("   " + line)
    return code == 0 and not masalah


if __name__ == "__main__":
    quarto = sys.argv[sys.argv.index("--quarto") + 1] if "--quarto" in sys.argv else "quarto"
    siapkan()
    ok = render(quarto, ["--to", "html"], "html.log")
    ok = render(quarto, ["--to", "typst", "--output-dir", "_book_pdf"], "typst.log") and ok
    sys.exit(0 if ok else 1)
