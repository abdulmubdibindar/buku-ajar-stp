// Definisi Typst buku (via include-in-header): kotak callout yang boleh
// terpotong antarhalaman, ukuran huruf tabel, dan penomoran persamaan.
#let kotak-warna = (
  capaian: (garis: rgb("#00a152"), latar: rgb("#e8f5e9")),
  kasus: (garis: rgb("#ff8f00"), latar: rgb("#fff8e1")),
  latihan: (garis: rgb("#8e24aa"), latar: rgb("#f3e5f5")),
  penting: (garis: rgb("#d32f2f"), latar: rgb("#ffebee")),
  catatan: (garis: rgb("#1e88e5"), latar: rgb("#e3f2fd")),
)

#let kotak-buku(jenis: "catatan", judul: none, isi) = {
  let w = kotak-warna.at(jenis)
  block(
    breakable: true,
    width: 100%,
    fill: w.latar,
    stroke: (left: 3pt + w.garis),
    inset: (x: 10pt, y: 8pt),
    above: 1.2em,
    below: 1.2em,
  )[
    #if judul != none {
      block(sticky: true, below: 0.8em, text(weight: "bold", fill: w.garis.darken(40%), judul))
    }
    #isi
  ]
}

// Ukuran huruf tabel tidak boleh melebihi teks badan.
#show table: set text(size: 0.9em)

// Hanya persamaan berlabel ({#eq-...}) yang bernomor, sama seperti di HTML.
// Persamaan tanpa label dirender ulang tanpa nomor dan penghitungnya
// dikembalikan, agar nomor persamaan berlabel tidak bergeser.
#show math.equation.where(block: true): it => {
  if it.has("label") {
    it
  } else {
    counter(math.equation).update(n => n - 1)
    [#math.equation(it.body, block: true, numbering: none)<eq-tanpa-nomor>]
  }
}
