---
name: format-pdf-layout
description: Panduan praktis mengendalikan layout dan dimensi Tabel serta Gambar saat mengkompilasi dokumen R Markdown/Bookdown ke dalam output PDF (LaTeX) agar tidak melampaui batas margin kertas.
---

# Panduan Layout PDF untuk Tabel dan Gambar

Ketika Anda mengkompilasi dokumen R Markdown (khususnya menggunakan Bookdown) ke dalam format PDF (LaTeX), objek-objek besar memiliki kecenderungan menerobos paksa batas akhir *margin* kertas alih-alih mengecil secara otomatis. 

Gunakan panduan dan *code snippet* berikut ini ketika Anda menemui grafis atau tabel yang hancur di PDF.

## 1. Menyelamatkan Tabel yang Sangat Lebar (kableExtra)

Lebar total tabel yang memiliki banyak kolom akan memaksa cetakan melewati margin kanan PDF. Kita harus menginstruksikan `kableExtra` untuk men-skalakan tabel tersebut menyesuaikan dengan ukuran kertas secara proporsional.

### Sintaks Penyelamat:

```r
library(knitr)
library(kableExtra)

kbl(dataset_anda, 
    caption = "Judul Tabel Anda",
    booktabs = TRUE) |> 
  kable_styling(
    bootstrap_options = c("striped", "hover"), 
    full_width = FALSE, 
    latex_options = c("scale_down", "HOLD_position") # << INI KUNCINYA
  ) |>
  column_spec(1, width = "4cm") # Opsi tambahan membatasi porsi kolom spesifik
```

- **`scale_down`**: Menekan keseluruhan font dan padding tabel agar pas dengan sisa margin buku (*autofit* ukuran).
- **`HOLD_position`**: Berkomunikasi langsung dengan paket LaTeX `[H]` (`float`) agar tabel tersebut diletakkan diam persis di bawah paragraf teks terakhir tanpa terlempar melayang acak ke halaman ganjil selanjutnya.
- **`booktabs = TRUE`**: Kritis untuk mencetak garis batas horizontal ala publikasi ilmiah yang elegan (tanpa *vertical lines*). 

## 2. Mengendalikan Gambar/Plot yang Melampaui Margin

Plot grafik bawaan dari R base atau `ggplot2` sering terender lebih besar dari kertas PDF. Penanganannya tidak dilakukan melalui kode R di badan Chunk, melainkan 100% diatur pada header **Chunk Options**.

*Catatan: Anda dapat menggunakan gaya Quarto (`#|`) atau R Markdown klasik (di samping `r`).*

### Sintaks Penyelamat:

```r
#| echo: false
#| out.width: "80%"
#| fig.align: "center"
#| fig.pos: "H"
#| fig.cap: "Judul Gambar"

plot(dataset_anda) 
```

Atau dalam gaya R Markdown Klasik:
` ```{r echo=FALSE, out.width="80%", fig.align="center", fig.pos="H", fig.cap="Judul Gambar"} `

- **`out.width`**: Mengunci lebar plot fisik agar patuh menjadi sekian persen (contoh: 80%) dari alokasi badan *text layer* keseluruhan tempat plot tersebut disematkan.
- **`fig.align="center"`**: Menempatkan plot sentral simetris agar lebih rapi.
- **`fig.pos="H"`**: Sama halnya seperti tabel, atribut paksa dari pustaka `float` ini memastikan ilustrasi Anda pantang bergeser menjauhi sumber referensi teksnya sekalipun ruang halaman sekarat.
