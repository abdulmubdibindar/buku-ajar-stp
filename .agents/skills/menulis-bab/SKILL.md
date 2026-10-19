---
name: menulis-bab
description: Panduan menulis dan menyunting isi bab buku ajar Statistika untuk Perencanaan (Quarto). Pakai setiap kali menulis, menulis ulang, atau menambah teks, callout (capaian, studi kasus, soal latihan, penting, catatan), persamaan, tabel, atau grafik di berkas bab .qmd.
---

# Menulis Bab

Berlaku untuk semua berkas bab `*.qmd` di akar proyek. Detail teknis ada di:

- [references/callout.md](references/callout.md) — sintaks Capaian, Studi Kasus, Soal Latihan, Penting, Catatan
- [references/persamaan.md](references/persamaan.md) — persamaan dan rujukannya
- [references/tabel-grafik.md](references/tabel-grafik.md) — tabel, grafik ggplot2, gambar, angka desimal

Setelah menyunting, jalankan `python _scripts/lint_buku.py <berkas>` sampai 0 galat.

## Struktur bab

1. Judul bab (`# Judul`), lalu satu callout `.capaian`.
2. Tiap subbab mengikuti urutan **Konsep → Studi Kasus → Soal Latihan**.
3. Studi kasus memakai data di `datasets/` bila memungkinkan.

## Bahasa

- Bahasa Indonesia yang sederhana dan langsung; tulis untuk mahasiswa S1 perencanaan.
- Istilah asing dimiringkan: *margin of error*.
- **Tebalkan** istilah kunci saat pertama kali didefinisikan, bukan seluruh kalimat.
- Angka memakai koma desimal dan titik ribuan: 20,90 tahun; 18.877 orang.
- Jangan memakai emoji (tidak tampil di PDF).

## Studi kasus memperjelas konsep

Pembahasan studi kasus harus menunjuk balik ke konsep yang baru dijelaskan:
sebut nama konsepnya dan tunjukkan di bagian perhitungan mana konsep itu bekerja.
Studi kasus yang hanya berisi langkah hitung tanpa mengaitkan ke konsep belum selesai.

> Salah: "Hasilnya adalah 20,4 sampai 21,4 tahun."
>
> Benar: "Rentang 20,4–21,4 tahun inilah **estimasi rentang**: estimasi titik
> 20,9 tahun ditambah dan dikurangi *margin of error* 0,5 tahun."

## Tanpa meta-commentary dan penjelasan berlebih

Instruksi penulisan (dari pengguna, skill, atau prompt) adalah arahan untuk
penulis, **bukan isi buku**. Jangan pernah menuliskannya ulang ke dalam teks.

| Instruksi yang diterima | Salah (instruksi bocor) | Benar |
|---|---|---|
| "Buat data fiktif untuk menjelaskan regresi linear" | "Data fiktif di bawah ini akan kita gunakan untuk menjelaskan analisis regresi linear." | "Tabel @tbl-upah-jam memuat upah dan jam kerja 10 pekerja." |
| "Tulis seperti berbicara kepada mahasiswa agar paham" | "Bayangkan saya berbicara kepada Anda agar Anda paham." | Langsung jelaskan dengan kalimat sapaan biasa: "Perhatikan bahwa…" |

Hindari juga:

- Pengumuman isi ("Pada subbab ini kita akan membahas…") — langsung bahas.
- Mengulang penjelasan yang sama dengan kata lain dalam satu subbab.
- Kalimat pengisi tanpa informasi ("Hal ini sangat penting untuk dipahami.").

## Format markdown

- Selalu beri **satu baris kosong** antara paragraf dan butir daftar pertama:

  ```markdown
  Contoh nama kota:

  - Lisbon
  - Magelang
  ```

  Yang dihindari (daftar menempel ke paragraf):

  ```markdown
  Contoh nama kota:
  - Lisbon
  - Magelang
  ```

- Langkah prosedur (mis. uji hipotesis) memakai `a.`, `b.`, … dengan judul langkah
  tebal; penjelasan lanjutan diindentasi di bawahnya.
- Jangan menaruh heading (`##`, `###`) di dalam callout: heading itu masuk TOC.
  Pakai atribut `title`.
- Rujukan silang memakai sintaks Quarto (`@fig-…`, `@tbl-…`, `@eq-…`, `@sec-…`,
  `@kasus-…`). Quarto menambahkan kata "Gambar/Tabel/Persamaan" sendiri; jangan
  menulis "Gambar @fig-…".
- Gambar ilustrasi baru dibuat lewat skill `buat-ilustrasi`.
