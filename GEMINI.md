# BUKU AJAR STATISTIKA UNTUK PERENCANAAN

Proyek ini adalah penulisan buku seperti yang disebutkan dalam [[README]]. Pada _branch_ `main`, buku ini masih dikembangkan menggunakan paket R Markdown/Bookdown. Akan tetapi, dalam keberjalanannya ditemukan persoalan dalam hal _rendering_. Buku ini masih "diterbitkan" menggunakan [GitHub Page](https://abdulmubdibindar.github.io/buku-ajar-stp) yang mengambil data dari direktori [`docs`](./docs/). Di sisi lain, kami juga ingin buku ini nantinya diterbitkan dalam bentuk PDF.

Persoalan _rendering_ ditemukan ketika kami me-_render_ buku ini ke dua keluaran: HTML dan PDF. Kelihatannya beberapa sintaks mengakibatkan _render_ ke PDF menjadi gagal, sebagaimana yang didokumentasikan dalam [[20260413-1615-render-attempt]]. Sejak hari itu, proyek buku ini diarahkan ke Quarto.

## Struktur Direktori Proyek

- [`bookdown_files`](./_bookdown_files/): (saya juga tidak terlalu paham apa kegunaan direktori ini) mungkin hasil dari rendering website pada suatu hari
- [`.obsidian`](/.obsidian): 
- [`datasets`](./datasets/): tempat saya menyimpan dataset yang digunakan dalam buku
- [](./docs)
- [](./figures)
- [](./guides)
- [](./how-to-quarto)
- [](./images)
- [](./quarto-migration-plan)
