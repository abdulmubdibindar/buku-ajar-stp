---
name: migrasi-bab
description: Memigrasi satu bab dari sintaks R Markdown/Bookdown (rmdkasus, \@ref, (\#eq:), opsi chunk gaya knitr) ke sintaks Quarto dan callout buku ini. Pakai saat diminta memigrasi atau mengonversi bab lama. Hapus skill ini setelah semua bab selesai dimigrasi.
---

# Migrasi Bab

Satu bab per commit, dengan dua commit terpisah agar mudah ditinjau:

1. **Mekanis** — jalankan skrip, periksa diff, commit:

   ```bash
   python _scripts/migrasi_bab.py <berkas.qmd>
   python _scripts/lint_buku.py <berkas.qmd>
   ```

   Pesan: `refactor(bab-N): konversi mekanis Bookdown ke Quarto`.

2. **Manual** — selesaikan yang tidak bisa dikerjakan skrip, lalu commit
   `fix(bab-N): rapikan hasil migrasi …`:
   - Setiap `PERIKSA` yang dicetak skrip.
   - `@sec-…` ke bab lain: tambahkan `{#sec-…}` pada heading tujuan.
   - Rujukan `@fig-…`/`@tbl-…` ke bab yang belum dimigrasi akan tampil `?@…`
     sampai bab itu dimigrasi — catat di pesan commit, jangan diakali.
   - Kata yang jadi janggal setelah prefiks otomatis ("subbab @sec-…" →
     tercetak "subbab Bagian 6.5").
   - Galat linter tersisa (heading di dalam callout, karakter sampah).
   - Judul callout yang hilang atau kurang bermakna; id studi kasus terlalu panjang.
   - `kable_styling(latex_options = …)` dan opsi khusus LaTeX lain boleh dibuang.

3. **Isi** — tinjau dengan skill `tinjau-bab` (studi kasus ↔ konsep,
   meta-commentary). Perbaikan isi adalah commit tersendiri.

Setelah bab pertama yang memakai callout baru dimigrasi, gaya `.rmd*` di
`style.css` baru boleh dihapus ketika **semua** bab sudah bebas dari `rmd*`
(`python _scripts/lint_buku.py | grep bookdown` kosong).
