# Ilustrasi

Direktori ini adalah antrean pembuatan gambar ilustrasi dengan model
*text-to-image*. Penulis (atau agen penulis) menulis permintaan; agen yang
punya akses ke model gambar Gemini (Gemini CLI/Antigravity) mengeksekusinya.

## Alur

| Tahap | Siapa | Di mana | Status di berkas permintaan |
|---|---|---|---|
| 1. Tulis permintaan | penulis / agen penulis (skill `buat-ilustrasi`) | [`permintaan/`](permintaan/) | `menunggu` |
| 2. Hasilkan gambar | agen Gemini | [`hasil/`](hasil/) | `dihasilkan` |
| 3. Tinjau | penulis | — | `disetujui` / `revisi` |
| 4. Pakai di buku | penulis / agen penulis | pindahkan ke [`../images/`](../images/), sisipkan di bab | `dipakai` |

## Untuk agen Gemini (tahap 2)

1. Ambil setiap berkas di `permintaan/` berstatus `menunggu` atau `revisi`.
2. Buat gambar dari bagian **Prompt** (dan **Catatan revisi** bila ada),
   mematuhi **Rasio**, **Gaya**, dan **Larangan**.
3. Simpan sebagai `hasil/<nama>.png` (`<nama>` = nama berkas permintaan);
   untuk beberapa varian: `hasil/<nama>-1.png`, `hasil/<nama>-2.png`.
4. Ubah `status:` menjadi `dihasilkan` dan isi `model:` dengan model yang dipakai.
5. Jangan mengubah berkas di luar `ilustrasi/`.

## Aturan umum

- Hanya untuk ilustrasi konseptual (suasana kota, alur pikir, metafora).
  Grafik berbasis data, tabel, dan diagram statistik dibuat dengan ggplot2,
  bukan model gambar.
- Gambar tidak boleh memuat teks panjang; label ditambahkan di caption.
- Hindari logo, wajah orang nyata, dan merek.
