# Deskripsi Skill: Menulis Ulang Bab Buku

## Hal-hal terkait substansi materi

1. Membaca file bab buku yang diminta (yang ada sekarang berformat \*.txt)
2. Menuliskan kembali isi bab buku tersebut ke dalam file Rmd yang sesuai (akan diisikan oleh user)
3. Menganalisis isi file bab buku dalam format .txt tersebut untuk mengelompokkan isinya menjadi hal-hal berikut:
   - struktur (outline) bab
   - paragraf penjelasan konsep
   - contoh-contoh non-studi kasus yang diberikan
   - studi kasus
   - soal evaluasi
4. Mengenali elemen-elemen tekstual yang mengganggu flow tulisan, seperti nomor halaman yang ter-render di tengah paragraf, atau hasil ekstraksi tabel yang berantakan, atau gambar yang dirujuk tetapi tidak ada karena ketidakmungkinan file txt menyimpan gambar.
5. Menstrukturkan kembali isi bab ke dalam file Rmd yang sesuai dengan isi setiap subbab menggunakan alur penjelasan konsep → studi kasus; contoh-contoh non-studi kasus dihapus sama sekali dengan memastikan studi kasus mewakili konsep yang dijelaskan
6. Usahakan setiap satu elemen konsep langsung diikuti dengan pembahasan studi kasus yang relevan
7. Menggunakan kalimat konsep 1:1 dari file bab, kecuali studi kasus. Studi kasus dapat ditulis ulang dengan gaya bahasa yang sesuai dengan penjelasan konsep
8. Menuliskan soal evaluasi 1:1 dari file bab. Pastikan soal evaluasi sesuai dengan capaian pembelajaran bab.
9. Bila memungkinkan, gunakan file dalam @datasets yang merupakan data responden mahasiswa empat kampus perguruan tinggi di Bandar Lampung dan Lampung Selatan yang mengandung informasi sosioekonomi dan pola perjalanan mereka ke kampus

## Hal-hal terkait dengan format penulisan

1. Gunakan bahasa Indonesia ragam formal
2. Tuliskan istilah serapan bahasa asing dengan huruf miring
3. Gunakan aturan yang ada di @.agent/rules dan pelajari juga agent/workflow dan patuhi juga aturan-aturan yang ada di dalamnya utuk menuliskan ulang isi Rmd
4. Use "Studi Kasus: " as beginner for the title of rmdkasus
5. Use "Catatan: " as beginner for the title rmdnote
6. Use , for decimal and . for thousand separator

### General blocks

- Use {.unnumbered} at the end of the title of each blocks
- For rmdkasus, use 3rd heading, but for rmdexercise, use 2nd heading

### General chunks

- Use single apostrophe for naming strings

### Images

1. Create chunk id with "-" as separator, e.g. `fig-proses-perencanaan-rasional`
2. Use knitr::include_graphics() to include images
3. Use out.width = '60%' and fig.align = "center" to control image size and alignment
4. Use fig.cap to add image caption
5. Use echo=FALSE to hide code
6. For data viz, use ggplot2 mainly to construct the diagrams

### Tables

1. Use function `kableExtra::kbl` create tables
2. Use `kable_styling` to style tables
3. Use similar styling as in Images from number 3--5
4. Use dplyr package mainly to process dataset

### Equations

1. Follow how to format equations from @guides/equation_guide.md

## Hal-hal terkait gaya penulisan

1. DOKUMEN Rmd YANG AKAN DITULIS BUKANLAH DOKUMEN PANDUAN PRAKTIKUM. Jangan dulu menuliskan teknik-teknik analisis dengan perangkat lunak. Fokus pada pembahasan konsep-konsepnya
2. Jangan membahas dataset secara eksplisit. Ubah gaya penuturan menjadi penjabaran cerita tentang dataset tersebut. Misalnya, tidak perlu menyebutkan "Berdasarkan DataUtama_mhsITERA.csv", tetapi sebutkan "Hasil survei xxx orang mahasiswa ITERA menghasilkan ..."
