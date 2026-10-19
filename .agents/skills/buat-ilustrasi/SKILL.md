---
name: buat-ilustrasi
description: Menyiapkan permintaan gambar ilustrasi untuk model text-to-image (Gemini) dan memasang gambar yang sudah disetujui ke bab. Pakai saat bab butuh ilustrasi konseptual baru, atau saat diminta memproses/menyisipkan hasil di ilustrasi/hasil/.
---

# Buat Ilustrasi

Gambar tidak dihasilkan di sesi ini. Skill ini menulis permintaan ke
`ilustrasi/permintaan/`; agen Gemini (Gemini CLI/Antigravity) yang
mengeksekusinya sesuai [`ilustrasi/CONTEXT.md`](../../../ilustrasi/CONTEXT.md).

## Kapan dipakai

- Ilustrasi konseptual: suasana perkotaan, alur berpikir, metafora visual.
- **Bukan** untuk grafik data, tabel, atau diagram statistik → pakai ggplot2
  (lihat `menulis-bab/references/tabel-grafik.md`).

## Menulis permintaan

1. Salin `ilustrasi/permintaan/_templat.md` menjadi
   `ilustrasi/permintaan/<nama>.md`; `<nama>` = label tanpa `fig-`
   (mis. `label: fig-sampling-acak` → `sampling-acak.md`).
2. Isi semua bagian. **Prompt** dalam bahasa Inggris, konkret dan visual;
   **Tujuan pedagogis** dan **Caption** dalam bahasa Indonesia.
3. Di bab, tandai tempatnya dengan komentar — jangan merujuk gambar yang belum ada:

   ```markdown
   <!-- ilustrasi: ilustrasi/permintaan/sampling-acak.md -->
   ```

4. Beri tahu pengguna bahwa permintaan siap dijalankan oleh agen Gemini.

## Memasang gambar yang disetujui

Untuk permintaan berstatus `disetujui`:

1. Pindahkan `ilustrasi/hasil/<nama>.png` ke `images/<nama>.png`.
2. Ganti komentar penanda di bab dengan:

   ```markdown
   ![<caption>](images/<nama>.png){#fig-<nama> width="70%"}
   ```

3. Ubah status permintaan menjadi `dipakai`.
