# Persamaan

## Bernomor

```markdown
$$
\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}
$$ {#eq-mean-sampel}

Keterangan:

- $\bar{x}$ = rata-rata sampel
- $x_i$ = nilai observasi ke-$i$
- $n$ = banyaknya observasi
```

- Label: `eq-` + huruf kecil dan tanda hubung, deskriptif (`eq-moe-proporsi`, bukan `eq-rumus1`).
- Rujukan: `@eq-mean-sampel` (tercetak "Persamaan 6.1").
- Persamaan panjang/berjajar: `\begin{aligned} … \end{aligned}` di dalam `$$ … $$`
  (satu nomor). Jangan memakai `\begin{equation}` atau `(\#eq:…)` (sintaks Bookdown).
- Persamaan yang tidak dirujuk: `$$ … $$` tanpa label (tidak bernomor di HTML
  maupun PDF).
- Label unik di seluruh buku; label ganda membuat PDF gagal dikompilasi.

## Agar tampil di PDF (Typst)

- Jangan menulis `\begin{align}`/`\begin{equation}` di luar `$$` — LaTeX
  mentah dibuang saat membuat PDF.
- Di dalam `$$` pakai `aligned` (bukan `align`/`split`) atau `gathered`
  (bukan `gather`).
- Pindah baris `\\` hanya di dalam lingkungan:
  `$$ \begin{gathered} H_0: \mu = 5 \\ H_1: \mu < 5 \end{gathered} $$`.
- Satu backslash per perintah: `$\mu$`, bukan `$\\mu$` (escape string R tidak
  berlaku di markdown maupun di `#| fig-cap:`).
- Keterangan simbol langsung di bawah persamaan, sebagai daftar.

## Angka di dalam math

Desimal di dalam `$…$` tetap koma, tulis `20{,}90` agar tidak ada spasi
setelah koma. Untuk angka dari R, lihat [tabel-grafik.md](tabel-grafik.md).
