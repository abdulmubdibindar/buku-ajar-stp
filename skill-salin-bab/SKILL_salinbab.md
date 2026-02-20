---
name: salinbab
description: Panduan menulis ulang materi bab buku ajar dari format teks mentah (.txt) ke format R Markdown (.Rmd). Gunakan skill ini saat perlu mengonversi, menstrukturkan ulang, dan memperkaya materi bab dengan studi kasus berbasis dataset lokal, serta membersihkan elemen tekstual yang mengganggu.
---

# Skill Salin Bab (Rewrite Chapter)

Skill ini memandu proses konversi dan penyempurnaan materi bab buku ajar dari raw text ke R Markdown.

## Instruksi Utama

### 1. Analisis dan Persiapan

- **Input**: Baca file bab buku format `.txt` yang diberikan oleh user.
- **Output**: Tuliskan kembali ke file `.Rmd` yang ditentukan user.
- **Klasifikasi Konten**: Analisis isi file `.txt` dan kelompokkan menjadi:
  - Struktur (outline) bab
  - Paragraf penjelasan konsep
  - Contoh-contoh (non-studi kasus)
  - Studi kasus
  - Soal evaluasi
- **Pembersihan Teks**: Identifikasi dan bersihkan elemen tekstual yang mengganggu alur bacaan, seperti hal-hal berikut:
  - Nomor halaman yang terselip di tengah paragraf.
  - Hasil ekstraksi tabel yang berantakan/tidak terbaca.
  - Sisa-sisa rujukan gambar atau caption gambar yang tidak relevan (karena format .txt).

### 2. Restrukturisasi Konten

- **Alur**: Susun ulang setiap subbab dengan elemen: **Konsep → Studi Kasus**. Usahakan setiap satu elemen konsep langsung diikuti dengan pembahasan studi kasus yang relevan.
- **Penghapusan**: Hapus contoh-contoh non-studi kasus. Pastikan studi kasus yang ada/dibuat sudah mewakili konsep yang dijelaskan.
- **Prioritas Dataset**: Prioritaskan penggunaan dataset dari `@datasets` (data mahasiswa UNILA/ITERA/UBL/UINRIL) untuk membuat atau memodifikasi studi kasus agar relevan dengan konteks lokal.

### 3. Penulisan dan Bahasa

- **Konsep**: Salin kalimat penjelasan konsep **1:1** (sama persis) dari file asli.
- **Studi Kasus**: Dapat ditulis ulang/dimodifikasi gaya bahasanya agar mengalir dengan penjelasan konsep dan relevan dengan dataset baru.
- **Evaluasi**: Salin soal evaluasi **1:1**. Pastikan sesuai dengan capaian pembelajaran.
- **Gaya Bahasa**:
  1. Gunakan Bahasa Indonesia formal. Istilah asing dicetak _miring_.
  2. Fokus pada **konsep**, bukan panduan praktikum software. Jangan menuliskan teknik analisis software secara detail di tahap ini.
  3. **Naratif Dataset**: Jangan sebutkan nama file dataset (misal "Berdasarkan DataUtama...") secara eksplisit. Gunakan narasi cerita (misal "Hasil survei terhadap 400 mahasiswa ITERA menunjukkan...").

### 4. Format dan Teknis

- **Aturan**: Patuhi aturan di `@.agent/rules` (headers, chunks, formatting).
- **Heading**:
  - Gunakan `{.unnumbered}` di akhir judul setiap block.
  - `rmdkasus`: Gunakan Heading 3 (`###`).
  - `rmdexercise`: Gunakan Heading 2 (`##`).
- **Container**:
  - `rmdkasus`: Judul harus diawali dengan "Studi Kasus: ".
  - `rmdnote`: Judul harus diawali dengan "Catatan: ".
- **Angka**: Gunakan koma (`,`) untuk desimal dan titik (`.`) untuk ribuan.
- **String**: Gunakan tanda kutip tunggal (`'`) untuk penamaan string dalam kode R.
- **Code Chunks**:
  - **SELALU BERI NAMA CHUNK**.
  - Gunakan format penamaan berikut untuk mencegah duplikasi:
    - `nama-bab-nomor-urutan-konsep-penjelasan`
    - `nama-bab-nomor-urutan-konsep-studi-kasus`
    - `nama-bab-nomor-urutan-konsep-evaluasi`

### 5. Elemen Visual (Gambar & Tabel)

- **Gambar**:
  1. Buat chunk ID dengan separator `-` (misal: `fig-proses-perencanaan`).
  2. Gunakan `knitr::include_graphics()`.
  3. Atur `out.width = '60%'` dan `fig.align = "center"`.
  4. Gunakan `fig.cap` untuk caption gambar.
  5. Gunakan `echo=FALSE` untuk menyembunyikan kode.
  6. Gunakan paket `ggplot2` untuk visualisasi data.

- **Tabel**:
  1. Gunakan fungsi `kableExtra::kbl()`.
  2. Gunakan `kable_styling` untuk style tabel.
  3. Terapkan styling serupa dengan gambar (alignment, width).
  4. Gunakan paket `dplyr` untuk pemrosesan dataset.

- **Persamaan**: Ikuti format persamaan dari `@guides/equation_guide.md`.
