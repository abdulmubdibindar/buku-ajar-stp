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
- Persamaan yang tidak dirujuk: `$$ … $$` tanpa label.
- Keterangan simbol langsung di bawah persamaan, sebagai daftar.

## Angka di dalam math

Desimal di dalam `$…$` tetap koma, tulis `20{,}90` agar tidak ada spasi
setelah koma. Untuk angka dari R, lihat [tabel-grafik.md](tabel-grafik.md).
