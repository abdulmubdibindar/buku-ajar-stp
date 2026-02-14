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
  1. Struktur (outline) bab
  2. Paragraf penjelasan konsep
  3. Contoh-contoh (non-studi kasus)
  4. Studi kasus
  5. Soal evaluasi
- **Pembersihan Teks**: Identifikasi dan bersihkan elemen tekstual yang mengganggu alur bacaan, seperti hal-hal berikut:
  - Nomor halaman yang terselip di tengah paragraf.
  - Hasil ekstraksi tabel yang berantakan/tidak terbaca.
  - Sisa-sisa rujukan gambar atau caption gambar yang tidak relevan (karena format .txt).

### 2. Restrukturisasi Konten

- **Alur**: Susun ulang setiap subbab dengan alur: **Penjelasan Konsep → Studi Kasus**.
- **Penghapusan**: Hapus contoh-contoh non-studi kasus. Pastikan studi kasus yang ada/dibuat sudah mewakili konsep yang dijelaskan.
- **Prioritas Dataset**: Prioritaskan penggunaan dataset dari `@datasets` (data mahasiswa UNILA/ITERA/UBL/UINRIL) untuk membuat atau memodifikasi studi kasus agar relevan dengan konteks lokal.

### 3. Penulisan dan Bahasa

- **Konsep**: Salin kalimat penjelasan konsep **1:1** (sama persis) dari file asli.
- **Studi Kasus**: Boleh ditulis ulang/dimodifikasi gaya bahasanya agar mengalir dengan penjelasan konsep dan relevan dengan dataset baru.
- **Evaluasi**: Salin soal evaluasi **1:1**. Pastikan sesuai dengan capaian pembelajaran.
- **Gaya Bahasa**: Gunakan Bahasa Indonesia formal. Istilah asing dicetak _miring_.

### 4. Format dan Teknis

- **Aturan**: Patuhi aturan di `@.agent/rules` (headers, chunks, formatting).
- **Heading**: Sesuaikan level heading (misal: Heading 3 untuk judul rmdkasus/rmdnote di baris pertama container).
- **Container**: Gunakan format container yang benar sesuai rules (misal: `::: {.rmdkasus ...}`).
