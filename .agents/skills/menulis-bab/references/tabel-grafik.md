# Tabel, Grafik, dan Gambar

Buku dirender ke HTML dan PDF (Typst). Tidak ada LaTeX: opsi seperti
`latex_options`, `scale_down`, `HOLD_position`, `fig.pos` tidak berguna.

## Chunk kode

Opsi chunk ditulis gaya Quarto (`#|`), bukan di header `{r …}`:

```r
#| label: fig-sebaran-jarak
#| fig-cap: "Sebaran jarak tempat tinggal mahasiswa ITERA"
#| out-width: "70%"
#| fig-align: center
```

- Label grafik `fig-…`, tabel `tbl-…`; hanya label berprefiks ini yang bisa dirujuk.
- Tabel dari kode: `#| tbl-cap: "…"` (bukan argumen `caption` di `kbl()`).
- Setiap bab punya chunk setup yang memanggil `source("_common.R")`
  (echo/message/warning mati, `OutDec = ","`).
- Pipe `|>`, data diolah dengan `dplyr`, string memakai tanda kutip tunggal.

## Tabel

- `knitr::kable()` / `kableExtra::kbl()` dengan
  `format.args = list(decimal.mark = ",", big.mark = ".")`.
- **Jangan** mengatur ukuran huruf (`font_size`, CSS inline): ukuran huruf
  tabel diatur global (≤ teks badan) di `style.css` dan `_typst/kotak-buku.typ`.
- Hindari gaya yang hanya jalan di satu format (`row_spec(background = …)`,
  `scroll_box()`); bila terpaksa, bungkus dengan `if (knitr::is_html_output())`.
- Tabel statis ditulis sebagai tabel markdown dengan label:
  `: Judul tabel {#tbl-simbol}` di bawah tabel.

## Grafik ggplot2 dan `OutDec = ","`

`OutDec = ","` membuat `paste()`/`format()` menghasilkan koma, yang merusak
parser ekspresi R:

- Ekspresi math pada grafik: pakai `bquote(mu == .(nilai))`, atau
  `format(nilai, decimal.mark = ".")` sebelum `parse(text = …)`.
- Label sumbu: `scales::label_number(decimal.mark = ",", big.mark = ".")`.
- Angka di dalam `$…$` hasil `paste()`: format dengan titik dulu lalu ganti,
  mis. `sub(".", "{,}", format(x, decimal.mark = "."), fixed = TRUE)`.

## Gambar statis

```markdown
![Proses perencanaan rasional. Diadaptasi dari @ewing2020basic](images/proses-perencanaan.png){#fig-proses-perencanaan width="60%"}
```

Gambar baru yang perlu dibuat model text-to-image: skill `buat-ilustrasi`.
