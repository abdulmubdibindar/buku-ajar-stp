## Proyek: Re-formatting Buku Ajar "Statistika Untuk Perencanaan" ke R Markdown

### 1. Tujuan Proyek

Mengonversi naskah buku ajar dari format PDF ke format `.Rmd` (R Markdown) yang siap dirajut (_knit_) menjadi dokumen PDF (via LaTeX), HTML, atau e-book, dengan tetap mempertahankan integritas konten dan estetika tata letak buku tersebut.

### 2. Spesifikasi Teknis Dokumen

- **Format Output:** `bookdown::pdf_book` atau `html_document`.
- **Engine Sintaks:** R (menggunakan `tidyverse` sebagai standar utama).
- **Encoding:** UTF-8.
- **Struktur Metadata (YAML):**
- Sertakan Judul, Penulis, dan Tanggal.
- Konfigurasi daftar isi (_table of contents_), penomoran bab, dan sitasi menggunakan file `.bib`.

### 3. Aturan Konversi Konten

- **Teks Utama:** Ubah _heading_ Word (Level 1, 2, 3) menjadi tag Markdown (`#`, `##`, `###`).
- **Rumus Statistik:** Semua rumus harus dikonversi ke format LaTeX.
- _Inline math:_ Menggunakan `$ \bar{x} = \frac{\sum x}{n} $`.
- _Display math:_ Menggunakan format `$$` untuk rumus kompleks seperti Regresi Linear atau Uji Hipotesis.
- **Tabel:** Jangan gunakan tabel Markdown manual untuk data statistik. Gunakan fungsi `knitr::kable()` atau paket `kableExtra` agar tabel terlihat profesional.
- **Visualisasi Data:**
- Jika ada grafik di Word, buat ulang menggunakan `ggplot2` di dalam _R code chunk_.
- Gunakan tema yang bersih seperti `theme_minimal()` atau `theme_light()`.

### 4. Penanganan Komponen Perencanaan

Pertahankan konten dari file PDF yang sudah ada.

### 5. Standar Kode (Code Style)

- Gunakan komentar pada setiap blok kode (`#`) untuk menjelaskan langkah pembersihan data atau uji statistik yang dilakukan.
- Pastikan opsi _chunk_ diatur dengan benar (misal: `echo=TRUE`, `warning=FALSE`, `message=FALSE`).
