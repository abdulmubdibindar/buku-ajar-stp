---
name: render-buku
description: Cara merender buku ajar ke HTML (docs/, GitHub Pages) dan PDF (Typst) dengan Quarto, serta mengatasi galat render. Pakai saat diminta merender, mempratinjau, menerbitkan, atau memperbaiki hasil render HTML/PDF.
---

# Render Buku

## Prasyarat

- Quarto **≥ 1.10** (1.7 belum mendukung buku Typst), R dengan paket yang
  dipakai bab (`knitr`, `kableExtra`, `ggplot2`, `dplyr`, …), Python 3.
- Tidak perlu LaTeX: PDF dibuat lewat Typst yang dibundel Quarto.

## Perintah

```bash
python render_book.py          # HTML lalu PDF
python render_book.py html     # HTML saja  -> docs/
python render_book.py pdf      # PDF saja   -> docs/*.pdf
quarto preview                 # pratinjau HTML selama menulis
```

- HTML **harus** ke `docs/` (GitHub Pages membaca folder itu); commit `docs/`
  setelah render agar situs diperbarui.
- PDF dirender ke `_book_pdf/` lalu disalin ke `docs/`: render Typst
  langsung ke `docs/` akan menghapus hasil HTML.
- Cache `_freeze` dipisah per format (`html_freeze/`, `typst_freeze/`).

## Uji tanpa R

```bash
python _scripts/uji_render.py [--quarto /path/ke/quarto]
```

Menyalin buku ke `_uji_render/`, mengganti chunk R dengan placeholder
berlabel sama, lalu merender HTML dan PDF. Lolos = 0 peringatan. Jalankan
setelah mengubah markup, callout, persamaan, atau konfigurasi; hasil
perhitungan R tetap perlu render penuh.

## Komponen render

| Berkas | Fungsi |
|---|---|
| `_quarto.yml` | konfigurasi buku, urutan bab |
| `_scripts/indeks_callout.py` | pre-render: nomor bab & label callout → `_callout-index.json` |
| `callout-buku.lua` | judul/nomor callout, TOC, rujukan `@kasus-…` |
| `_typst/kotak-buku.typ` | kotak callout PDF (bisa terpotong halaman), ukuran huruf tabel, hanya persamaan berlabel yang bernomor |
| `style.css` | gaya HTML |
| `_common.R` | opsi knitr bersama, di-source tiap bab |
| `_tests/callout/` | proyek uji callout tanpa R |
| `_scripts/uji_render.py` | uji render seluruh buku tanpa R |

## Mengatasi galat

1. Jalankan `python _scripts/lint_buku.py` dulu — sisa sintaks Bookdown sering
   jadi penyebab.
2. Uji tanpa R: `python _scripts/uji_render.py`; untuk filter callout saja:
   `cd _tests/callout && quarto render --to html && quarto render --to typst`.
3. Galat Typst: render ulang dengan `quarto render --to typst -M keep-typ:true
   --output-dir _book_pdf` lalu periksa `.typ` pada baris yang disebut.
4. Nomor callout salah/rujukan `??kasus-…`: pastikan pre-render berjalan
   (`_callout-index.json` ada) dan id di callout sesuai.
5. Hasil kode basi: hapus cache format terkait (`html_freeze/` atau `typst_freeze/`).
