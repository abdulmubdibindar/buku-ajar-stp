"""Render buku ke HTML (docs/, untuk GitHub Pages) dan PDF (Typst).

Cache `_freeze` dipisah per format (html_freeze/, typst_freeze/) karena hasil
komputasi yang dibekukan untuk satu format tidak selalu cocok untuk format lain.

Pemakaian:
    python render_book.py          # HTML lalu PDF
    python render_book.py html     # HTML saja
    python render_book.py pdf      # PDF saja
"""

import glob
import os
import shutil
import subprocess
import sys

HTML_DIR = "docs"
PDF_TMP_DIR = "_book_pdf"


def run(args):
    print("$ " + " ".join(args))
    return subprocess.call(args)


def remove(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
    elif os.path.exists(path):
        os.remove(path)


def swap_freeze(cache):
    """Pasang cache khusus format sebagai _freeze."""
    remove("_freeze")
    if os.path.exists(cache):
        shutil.copytree(cache, "_freeze")
        print(f"-> Memakai cache '{cache}'")


def save_freeze(cache):
    """Simpan _freeze kembali ke cache khusus format."""
    remove(cache)
    if os.path.exists("_freeze"):
        shutil.move("_freeze", cache)
        print(f"-> Cache disimpan ke '{cache}'")


def render_html():
    print("\n=== HTML -> docs/ ===")
    swap_freeze("html_freeze")
    code = run(["quarto", "render", "--to", "html"])
    save_freeze("html_freeze")
    if code != 0:
        sys.exit("Render HTML gagal.")


def render_pdf():
    print("\n=== PDF (Typst) ===")
    swap_freeze("typst_freeze")
    # Output-dir terpisah agar render PDF tidak menyentuh isi docs/.
    code = run(["quarto", "render", "--to", "typst", "--output-dir", PDF_TMP_DIR])
    save_freeze("typst_freeze")
    if code != 0:
        sys.exit("Render PDF gagal.")
    os.makedirs(HTML_DIR, exist_ok=True)
    for pdf in glob.glob(os.path.join(PDF_TMP_DIR, "*.pdf")):
        shutil.copy2(pdf, HTML_DIR)
        print(f"-> {os.path.basename(pdf)} disalin ke {HTML_DIR}/")
    remove(PDF_TMP_DIR)


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "all"
    if target in ("all", "html"):
        render_html()
    if target in ("all", "pdf"):
        render_pdf()
    print("\nSelesai.")
