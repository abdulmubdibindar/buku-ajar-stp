# BUKU AJAR STATISTIKA UNTUK PERENCANAAN

Proyek ini adalah penulisan buku seperti yang disebutkan dalam [README](./README.md). Pada _branch_ `main`, buku ini masih dikembangkan menggunakan paket R Markdown/Bookdown. Akan tetapi, dalam keberjalanannya ditemukan persoalan dalam hal _rendering_. Buku ini masih "diterbitkan" menggunakan [GitHub Page](https://abdulmubdibindar.github.io/buku-ajar-stp) yang mengambil data dari direktori [`docs`](./docs/). Di sisi lain, kami juga ingin buku ini nantinya diterbitkan dalam bentuk PDF.

Persoalan _rendering_ ditemukan ketika kami me-_render_ buku ini ke dua keluaran: HTML dan PDF. Kelihatannya beberapa sintaks mengakibatkan _render_ ke PDF menjadi gagal, sebagaimana yang didokumentasikan dalam \[\[20260413-1615-render-attempt]]. Sejak hari itu, proyek buku ini diarahkan ke Quarto: HTML ke `docs/`, PDF lewat Typst (tanpa LaTeX).

## Struktur Direktori Proyek

* [`.agents/skills`](./.agents/skills/): skill penulisan dan render buku untuk semua agen
* [`.claude/skills`](./.claude/skills/): skill untuk Claude Code — `icm-architecture`, plus symlink ke tiap skill di `.agents/skills` (skill baru di `.agents/skills` perlu ditautkan juga di sini)
* [`_bookdown_files`](./_bookdown_files/): sisa hasil _rendering_ Bookdown lama
* [`_scripts`](./_scripts/): skrip pre-render (indeks callout), linter, dan migrasi bab
* [`_tests`](./_tests/): proyek uji kecil untuk filter callout (tanpa R)
* [`_typst`](./_typst/): definisi tampilan PDF (kotak callout, ukuran huruf tabel)
* [`.obsidian`](./.obsidian/): direktori untuk Obsidian mengindeks
* [`datasets`](./datasets/): tempat saya menyimpan dataset yang digunakan dalam buku
* [`docs`](./docs) : direktori yang di-_render_ oleh GitHub Pages (keluaran HTML Quarto)
* [`figures`](./figures) : direktori tempat hasil _running_ kode R yang menghasilkan grafik
* [`guides`](./guides) : direktori tempat saya menyimpan berbagai panduan secara _random_
* [`how-to-quarto`](./how-to-quarto) : direktori tempat saya menyimpan dokumentasi tentang Quarto dari laman situs web-nya
* [`ilustrasi`](./ilustrasi) : antrean permintaan gambar untuk model _text-to-image_ (Gemini)
* [`images`](./images) : direktori tempat gambar statis yang dipakai bab
* [`quarto-migration-plan`](./quarto-migration-plan) : direktori tempat saya menyimpan catatan hasil pertanyaan dari NotebookLM

Dalam direktori akar proyek ini juga terdapat file-file setiap bab

* `index.qmd`
* `00-a-pengantar.qmd`
* `00-b-lembar-persembahan.qmd`
* `01-konsep-dasar.qmd`
* `02-data-terstruktur.qmd`
* `03-statistik-deskriptif.qmd`
* `04-visualisasi-data.qmd`
* `05-pengantar-inferensial.qmd`
* `06-estimasi-parameter.qmd` (sudah dimigrasi ke sintaks Quarto; contoh acuan)
* `07-uji-hipotesis-satu-populasi.qmd`
* `08-uji-hipotesis-dua-populasi.qmd`
* `09-uji-hipotesis-lebih-dua-populasi.qmd`
* `10-korelasi-nominal.qmd`
* `11-korelasi-ordinal.qmd`
* `12-korelasi-metrik.qmd`
* `13-regresi-sederhana.qmd`
* `14-regresi-berganda.qmd`
* `15-multivariat-interdependensi.qmd`
* `89-referensi.qmd`
* `90-lampiran-tabel-statistik.qmd`

Berkas pendukung render di akar: `_quarto.yml`, `callout-buku.lua`, `_common.R`, `style.css`, `render_book.py`.

## _Routing_

| Jika Anda perlu...                     | Pergi ke...                        | Baca...                                       |
| :------------------------------------- | :--------------------------------- | :-------------------------------------------- |
| Menulis/mengedit isi bab               | Direktori _root_ proyek ini        | skill `menulis-bab`                           |
| Meninjau bab                           | Direktori _root_ proyek ini        | skill `tinjau-bab`                            |
| Memigrasi bab Bookdown ke Quarto       | Direktori _root_ proyek ini        | skill `migrasi-bab`                           |
| Render HTML (`docs/`) dan PDF          | Direktori _root_ proyek ini        | skill `render-buku`                           |
| Membuat gambar ilustrasi               | [`ilustrasi`](./ilustrasi)         | `CONTEXT.md`, skill `buat-ilustrasi`          |
| Mempelajari isi pedoman Quarto         | [`how-to-quarto`](./how-to-quarto) | `CONTEXT.md`                                  |
| Mengakses dataset                      | `datasets`                         | (masing-masing dataset)                       |

Sebelum commit perubahan bab, jalankan `python _scripts/lint_buku.py <berkas>`.

Yang tidak usah dibaca:

- `preamble.tex` : karena proyek ini tidak bergantung lagi dengan LaTeX
