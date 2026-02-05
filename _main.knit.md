---
title: "Buku Ajar Statistika untuk Perencanaan"
author:
  - "Muhammad Abdul Mubdi Bindar"
  - "Husna Tiara Putri"
  - "Valendya Rilansari"
site: bookdown::bookdown_site
output:
    bookdown::gitbook:
        css: style.css
        split_bib: false
        keep_md: true
    bookdown::pdf_book:
        latex_engine: xelatex
        citation_package: natbib
        keep_tex: true
        includes:
            in_header: preamble.tex
bibliography: referensi.bib
biblio-title: "Referensi"
link-citations: true
---



# Statistika untuk Perencanaan {.unnumbered}

Buku ini dirancang untuk membantu mahasiswa dalam memahami konsep statistika dan penggunaan R dalam pengolahan data kuantitatif, terutama dalam perencanaan wilayah dan kota. Buku ini terdiri atas x bagian:

1. Konsep Dasar Statistika dalam Perencanaan
2. Data Terstruktur
3. Analisis Statistik Deskriptif
4. Visualisasi Data Kuantitatif
5. Pengantar Statistik Inferensial
6. Estimasi Parameter
7. Uji Hipotesis Satu Populasi
8. Uji Hipotesis Dua Populasi
9. Uji Hipotesis Lebih dari Dua Populasi
10. Korelasi Antarvariabel Nominal
11. Korelasi Antarvariabel Ordinal
12. Korelasi Antarvariabel Metrik
13. Regresi Linear Sederhana
14. Regresi Linear Berganda
15. Analisis Statistik Multivariat Interdependensi


------------------------------------

# Pengantar {.unnumbered}

Puji dan syukur kami panjatkan ke hadirat Tuhan Yang Maha Esa, Allah *subhanahu wa ta’aala*, yang tanpa rahmat, izin, dan kekuatan dari-Nya modul ini tidak akan pernah bisa dirampungkan. Kami juga memanjatkan salawat dan permohonan keselamatan untuk Rasul junjungan kami dan seluruh alam, Nabi Muhammad *shallallahu alaihi wa sallam*, pembawa risalah kebenaran dan transformator peradaban terbesar sepanjang sejarah.

Buku ajar ini kami rancang sebagai media pembelajaran sekaligus instrumen evaluasinya untuk mahasiswa yang mempelajari statistika, khususnya di bidang Perencanaan Wilayah dan Kota. Kasus-kasus yang digunakan dalam pembahasannya diambil dari dataset yang diupayakan oleh delapan orang mahasiswa PWK ITERA angkatan 2020: Alvian Syah Syaidina Muhammad, Muhammad Gilang Ramadhan, Assa Bangsa Putra, Fachrian Noor Kusnadi, Bonafasius Geoffrey Titawanno, dan Ramli Indran Alif di bawah bimbingan penulis.

Buku ajar ini pastinya masih jauh dari kesempurnaan. Untuk itu, kami sangat terbuka akan masukan dan kritikan demi kesempurnaan modul ini ke depannya. Segala masukan dan kritikan akan kami tampung melalui surel [muhammad.bindar@pwk.itera.ac.id](mailto:muhammad.bindar@pwk.itera.ac.id) dan jadikan pembelajaran untuk perbaikan selanjutnya.

Lampung Selatan, 2025

Tim Penulis

<!--chapter:end:index.Rmd-->

# Konsep Dasar Statistika dalam Perencanaan

::: rmdcapaian
### Capaian Pembelajaran {.unnumbered}

Setelah mempelajari bab ini, Anda diharapkan:

* Mampu menjelaskan kedudukan dan peran analisis statistik dalam perencanaan [STP-1.1]{.capaian}
* Mampu menjelaskan perbedaan analisis kuantitatif dan kualitatif dengan tepat [STP-1.2]{.capaian}
:::

## Kedudukan dan Peran Analisis Data dalam Perencanaan

Proses perencanaan adalah proses yang sangat memerlukan data di seluruh tahapannya. Seperti yang ditunjukkan dalam Gambar \@ref(fig:proses-perencanaan-rasional) tentang proses perencanaan secara rasional, setiap tahapnya sangat memerlukan data sebagai masukan untuk melaksanakan **setiap tahap**.

<div class="figure" style="text-align: center">
<img src="images/proses-perencanaan-rasional.png" alt="Proses Perencanaan Rasional. Diadaptasi dari @ewing2020basic" width="60%" />
<p class="caption">(\#fig:proses-perencanaan-rasional)Proses Perencanaan Rasional. Diadaptasi dari @ewing2020basic</p>
</div>

Kita ambil contoh di tahap pertama. Penetapan tujuan dan sasaran memerlukan data dari berbagai sumber di wilayah perencanaan, termasuk dari pemangku kepentingan (*stakeholder*). Data-data tersebut dikumpulkan dan untuk merumuskan tujuan dan sasaran yang benar-benar mencerminkan kebutuhan wilayah perencanaan.

Lain lagi di tahap kedua, contoh lainnya. Perumusan persoalan (*problem*) adalah hal yang harus dilakukan dengan mempertimbangkan data dan fakta kondisi yang ada (kondisi eksisting). Hal ini dikarenakan jika kita salah mendefinisikan persoalan, implementasi rencana tidak akan menjawab persoalan yang seharusnya.

Dari paparan sebelumnya, kita dapat menyimpulkan bahwa setiap tahap dalam perencanaan memerlukan penelitian, yakni kegiatan membuat pertanyaan mengenai suatu permasalahan dan menjawab pertanyaan tersebut dengan proses yang sistematis.

::: rmdkasus
### Studi Kasus: Analisis Data dalam Perencanaan Transportasi Berkelanjutan di Kampus ITERA {.unnumbered #kasus-analisis-data-dalam-perencanaan}

Kita akan mengambil kasus berupa perencanaan transportasi berkelanjutan mahasiswa dan staf pegawai di kampus ITERA. Transportasi berkelanjutan adalah perpindahan dalam konteks transportasi yang memiliki nilai berkelanjutan, salah satunya minim polusi udara.

Dalam kasus ini, kita sudah mengetahui bahwa tujuan dari rektorat adalah “transportasi mahasiswa dan pegawai yang berkelanjutan.” Selanjutnya, kita perlu mengetahui apa persoalan yang ada saat ini di kampus ITERA (perhatikan Gambar \@ref(fig:kasus-bab1))

<div class="figure" style="text-align: center">
<img src="images/kasus-bab1.png" alt="Persoalan Transportasi di ITERA" width="60%" />
<p class="caption">(\#fig:kasus-bab1)Persoalan Transportasi di ITERA</p>
</div>

Untuk mengetahui persoalan terkait dengan transportasi mahasiswa dan pegawai, kita perlu mengajukan pertanyaan terkait hal ini, yakni *sudah sejauh mana keberlanjutan pada pola pergerakan pada mahasiswa dan pegawai kampus ITERA saat ini?*

Ini adalah pertanyaan penelitian kita untuk menjawab apa persoalan yang ada terkait rencana transportasi berkelanjutan di kampus ITERA. Untuk menjawab pertanyaan ini, kita mengumpulkan data terkait pola pergerakan mahasiswa dan pegawai di ITERA dengan menyebarkan kuesioner kepada para mahasiswa dan pegawai kampus ITERA tentang pola pergerakan mereka.
:::

## Penelitian Kuantitatif vs. Penelitian Kualitatif dan Kedudukan Statistik

Selanjutnya kita akan membahas dua pendekatan terbesar dalam penelitian yakni penelitian kuantitatif dan penelitian kualitatif.

Penelitian secara umum adalah proses mengajukan pertanyaan dan menjawabnya secara sistematis. Pertanyaan yang diajukan bisa terkait dengan tahap yang dilakukan dalam proses perencanaan tadi.

Secara umum, pendekatan penelitian terbagi menjadi **pendekatan kuantitatif** dan **pendekatan kualitatif**. Singkatnya, pendekatan kuantitatif menekankan penggunaan angka-angka (kuantitas) dalam prosesnya, sementara pendekatan kualitatif menekankan pada eksplorasi data-data yang bersifat non-angka dan perlu diindra (dilihat, dicium, diraba, didengar) dan dirasakan.

### Analisis Kuantitatif vs. Analisis Kualitatif {#analisis-kuantitatif-vs-kualitatif}

Analisis adalah salah satu proses dalam penelitian yang mengolah data yang dikumpulkan menjadi jawaban dari pertanyaan di awal. Sebagaimana pendekatannya, secara umum analisis juga dapat dibagi menjadi **analisis kuantitatif** dan **analisis kualitatif**.

Di sisi lain, data sebagai bahan analisis juga dapat dibagi menjadi **data kuantitatif** dan **data kualitatif**. Kita dapat memaknai data kuantitatif sebagai fakta/fenomena yang diukur sehingga dinyatakan dalam bentuk angka, sementara data kualitatif adalah fakta/fenomena yang dijelaskan dalam bentuk pemaknaan dan pemahaman yang mendalam dari pelaku penelitian (subjek penelitian).

Karena analisis kuantitatif menggunakan angka-angka, pengumpulan data kuantitatif dapat disebut juga sebagai **pengukuran**.

::: rmdkasus

### Studi Kasus: Penelitian Mengenai Pola Pergerakan Mahasiswa dan Pegawai di Kampus ITERA {.unnumbered}

Berdasarkan pertanyaan penelitian *sudah sejauh mana keberlanjutan pada pola pergerakan pada mahasiswa dan pegawai kampus ITERA saat ini?*, kita akan  mengumpulkan data terkait pola pergerakan mahasiswa dan pegawai di ITERA dengan menyebarkan kuesioner kepada para mahasiswa dan pegawai kampus ITERA tentang pola pergerakan mereka. Berikut adalah analisis tentang perbandingan antara analisis kuantitatif dan analisis kualitatif.

| Aspek                | Analisis Kuantitatif                                                    | Analisis Kualitatif                                                          |
| :------------------- | :---------------------------------------------------------------------- | :--------------------------------------------------------------------------- |
| **Fokus**            | Luas (*Breadth*), mencari generalisasi.                                 | Dalam (*Depth*), mencari makna/alasan.                                       |
| **Pertanyaan Utama** | Berapa banyak emisi yang dihasilkan?                                    | Mengapa orang enggan naik shuttle?                                           |
| **Alat Analisis**    | Statistik (SPSS, Excel, Pemodelan Transportasi).                        | Transkrip wawancara, observasi lapangan, analisis tema.                      |
| **Kelebihan**        | Akurat untuk menghitung target penurunan emisi karbon secara matematis. | Sangat baik untuk merancang kebijakan yang sesuai dengan psikologi pengguna. |
| **Kelemahan**        | Tidak bisa menjelaskan alasan personal di balik angka.                  | Hasilnya tidak bisa digeneralisasi untuk seluruh populasi secara kaku.       |
:::

### Analisis Statistik sebagai Analisis Kuantitatif

Statistik adalah serangkaian teknik matematis yang digunakan untuk mengorganisir, memanipulasi, dan menganalisis data dengan tujuan menjawab pertanyaan penelitian [@healey2021statistics]. Ilmu yang mempelajari statistik disebut statistika yang dalam bahasa Inggris menjadi "statistics" (menggunakan "s").

Dalam pengertian tersebut terdapat kata kunci "matematis". Kata kunci tersebut tentunya mengantarkan kita berpikir bahwa analisis statistik adalah bagian dari penelitian kuantitatif.

Analisis statistik dapat melakukan hal-hal berikut:

1.  **Meringkas dan Mengorganisasi Data**. Statistik membantu mereduksi banyak item informasi menjadi beberapa angka yang jelas, ringkas, dan mudah dipahami, sebuah proses yang dikenal sebagai reduksi data.
2.  **Mengidentifikasi Pola dan Hubungan**. Statistik memungkinkan peneliti untuk mendeteksi pola dalam data dan mengukur hubungan antara dua atau lebih variabel.
3.  **Membuat Generalisasi**. Salah satu jenis statistik, statistik inferensial, mampu untuk menggeneralisasi temuan dari sampel kecil ke populasi yang lebih luas, memberikan perkiraan seberapa mungkin pola yang diamati dalam sampel berlaku di populasi. Ini akan kita pelajari di bab selanjutnya.
4.  **Menguji Hipotesis dan Teori**. Dalam penelitian secara umum, statistik membantu kita menguji apakah ide atau dugaan yang kita buat benar, berdasarkan data. Dari teori yang ada, kita bisa membuat hipotesis dan mengujinya secara empiris, atau bahkan menemukan hipotesis baru dari data.

Secara umum, statistika dapat dibagi menjadi dua menurut keperluannya terkait data: **statistika deskriptif** dan **statistika inferensial** [@ewing2020basic]. Statistika deskriptif berfungsi untuk mendeskripsikan data dari sebuah sampel atau populasi. Di sisi lain, statistik inferensial menarik kesimpulan dari data yang dikumpulkan (sampel) terhadap cakupan yang lebih besar dari data tersebut, yakni populasi.

Berdasarkan jumlah variabelnya statistika juga dapat dibagi menjadi 3: **statistika univariat**, **statistika bivariat** dan **statistika multivariat**. Sesuai namanya, statistika univariat adalah statistika yang digunakan untuk menganalisis satu variabel saja. Statistika bivariat adalah statistika yang menganalisis dua variabel secara bersamaan, sementara multivariat menganalisis lebih dari dua.

Jawablah soal evaluasi berikut untuk menguji pemahaman Anda tentang konsep dasar statistika dalam perencanaan.

::: rmdexercise
## Soal Evaluasi 1 {.unnumbered}

1.  Jelaskanlah penggunaan analisis data dalam setiap tahap perencanaan untuk kasus acara kumpul keakraban angkatan! [STP-1.1]{.capaian}
2.  Ceritakan perbedaan  analisis kuantitatif dan kualitatif yang mungkin digunakan dalam perencanaan acara tersebut. [STP-1.2]{.capaian}
:::

<!--chapter:end:01-konsep-dasar.Rmd-->

# Data Terstruktur

::: rmdcapaian
### Capaian Pembelajaran {.unnumbered}

Setelah mempelajari bab ini, Anda diharapkan:

1. mampu menganalisis variabel dan objek dalam sebuah format data terstruktur sesuai dengan konsepnya [STP-1.3]{.capaian}
2. mampu menentukan tingkat pengukuran yang tepat untuk sebuah variabel [STP-2.1]{.capaian}
:::

Berdasarkan formatnya, data dapat dibedakan menjadi dua jenis. Jenis data berdasarkan formatnya tersebut terdiri atas **data tidak terstruktur**  (*unstructured data*) dan **data terstruktur** (*structured data*).

Data tidak terstruktur adalah data yang tidak memiliki format yang terdefinisikan sebelum dikumpulkan, seperti teks wawancara, rekaman suara, gambar, atau video. Bentuk dan ukuran data-data tersebut dapat berbeda-beda, dengan kata lain formatnya tidak sama sehingga dapat dikatakan juga tidak terdefinisi atau tidak terstruktur [@oracle2024structured].

Di sisi lain, data terstruktur adalah data yang memiliki definisi yang jelas dan pola yang telah ditentukan sebelum dikumpulkan. Definisi yang jelas di sini diperlihatkan dengan bentuk data terstruktur berupa tabel. Dengan bentuk tabel, data memiliki format yang terdefinisi, lebih jelas isinya, dan dapat dikenali polanya sehingga lebih mudah untuk dianalisis.

**Penelitian yang menggunakan analisis statistik pasti menghasilkan data terstruktur dari pengumpulannya** [@devaus2014surveys]. Hal ini bukan berarti penelitian kualitatif juga tidak bisa menghasilkan data terstruktur, akan tetapi hal tersebut tidak mutlak. Hanya penelitian kuantitatif dengan metode analisis statistik yang mutlak menggunakan data terstruktur.

## Elemen Data Terstruktur {#kasus-elemen-data-terstruktur}

Dengan format yang jelas, data terstruktur dapat dipandang sebagai susunan 3 elemen penting: objek (*object*), variabel (*variable*), dan nilai (*value*). Ketiga hal ini membentuk struktur yang disebut **tabulasi data**. Tabulasi data adalah bentuk penyajian data dalam bentuk tabel yang terdiri atas baris dan kolom. Sebuah tabulasi data yang baik harus memiliki struktur yang jelas di mana baris mewakili objek dan kolom mewakili variabel.

1.  **Objek**. Objek adalah unit analisis yang datanya kita kumpulkan. Dalam tabulasi data, objek biasanya menempati posisi **baris** (*row*). Contoh objek dalam perencanaan wilayah dan kota bisa berupa rumah tangga, individu, kelurahan, kecamatan, atau kabupaten.
2.  **Variabel**. Variabel adalah karakteristik atau atribut yang melekat pada objek yang nilainya bisa berbeda-beda (bervariasi) antar satu objek dengan objek lainnya. Dalam tabulasi data, variabel menempati posisi **kolom** (*column*). Contoh variabel adalah luas lahan, jumlah penduduk, pendapatan per bulan, dan tingkat pendidikan.
3.  **Nilai**. Nilai adalah angka atau kategori yang mengisi perpotongan antara baris (objek) dan kolom (variabel), yakni **sel** (*cell*). Nilai ini merepresentasikan data spesifik dari variabel tertentu untuk objek tertentu.

::: rmdkasus
### Studi Kasus: Elemen Data Terstruktur {.unnumbered #kasus-elemen-data-terstruktur} 

Perhatikan hasil pengumpulan data kuesioner berupa tabulasi data dari mahasiswa-mahasiswa ITERA seperti yang ditampilkan pada Gambar \@ref(fig:bab-2-ilus-data-terstruktur).

<div class="figure" style="text-align: center">
<img src="images/bab-2-ilus-data-terstruktur.png" alt="Ilustrasi elemen data terstruktur" width="60%" />
<p class="caption">(\#fig:bab-2-ilus-data-terstruktur)Ilustrasi elemen data terstruktur</p>
</div>

Kita akan membedah elemen-elemen data terstruktur dari tabulasi data tersebut:
- Objek dari tabulasi data tersebut adalah mahasiswa-mahasiswa ITERA. Tiap objek dibedakan berdasarkan variabel `ID-mahasiswa`.
- Variabel dari tabulasi data tersebut di antaranya adalah `Program Studi`, `Usia`, `Jumlah Motor`, dan `Jumlah Mobil`. Adapun variabel `ID-mahasiswa` tidak termasuk dalam variabel yang dihitung karena hanya bertindak sebagai pengidentifikasi objek.
- Nilai dari tabulasi data tersebut bisa kita lihat di sel-selnya. Misalnya, objek mahasiswa dengan `ID-mahasiswa` 002 memiliki nilai `Program Studi` adalah "Matematika", `Usia` adalah 21 tahun, `Jumlah Motor` adalah 0, dan `Jumlah Mobil` adalah 1.
:::

## Tabulasi Data Terstruktur yang Baik

Agar data dapat diolah dengan baik menggunakan perangkat lunak statistik seperti R, tabulasi data harus memenuhi kaidah "Tidy Data" atau data yang rapi. Berikut adalah prinsip-prinsip data yang rapi:

1.  Setiap variabel harus membentuk satu kolom.
2.  Setiap observasi (objek) harus membentuk satu baris.
3.  Setiap jenis unit observasi membentuk satu tabel.

Pelajari kasus yang berisi perbandingan antara data yang tidak rapi dan data yang rapi berikut.

::: rmdkasus
### Studi Kasus: Perbandingan Data yang Tidak Rapi dan Data yang Rapi {.unnumbered} 

Berikut adalah beberapa contoh kesalahan umum dalam struktur data dan perbaikannya:

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:left;"> Jenis Kesalahan </th>
   <th style="text-align:left;"> Data Tidak Rapi (Salah) </th>
   <th style="text-align:left;"> Data Rapi (Benar) </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;width: 20%; font-weight: bold;"> Kesalahan 1: Header Baris Bersarang </td>
   <td style="text-align:left;width: 40%; "> <img src="images/bab-2-kesalahan-1-recreate.png" width="300"> </td>
   <td style="text-align:left;width: 40%; "> <img src="images/bab-2-perbaikan-1-recreate.png" width="300"> </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 20%; font-weight: bold;"> Kesalahan 2: Struktur Kompleks </td>
   <td style="text-align:left;width: 40%; "> <img src="images/bab-2-kesalahan-2-recreate.png" width="300"> </td>
   <td style="text-align:left;width: 40%; "> <img src="images/bab-2-perbaikan-2-recreate.png" width="300"> </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 20%; font-weight: bold;"> Kesalahan 3: Format Tidak Konsisten </td>
   <td style="text-align:left;width: 40%; "> <img src="images/bab-2-kesalahan-3-recreate.png" width="300"> </td>
   <td style="text-align:left;width: 40%; "> <img src="images/bab-2-perbaikan-3-recreate.png" width="300"> </td>
  </tr>
</tbody>
</table>
:::

Jawablah soal evaluasi berikut untuk menguji pemahaman Anda tentang elemen-elemen data terstruktur.

::: rmdexercise
## Soal Evaluasi 2 {.unnumbered}

Perhatikan tabel hasil pengumpulan data kuesioner berikut ini [STP-1.3]{.capaian}:

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:left;"> ID_rumah </th>
   <th style="text-align:right;"> Usia_KK </th>
   <th style="text-align:right;"> Jml_anggota </th>
   <th style="text-align:right;"> Luas_rumah </th>
   <th style="text-align:right;"> Income_bln </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;width: 20%; font-weight: bold;"> 001 </td>
   <td style="text-align:right;width: 40%; "> 55 </td>
   <td style="text-align:right;width: 40%; "> 2 </td>
   <td style="text-align:right;"> 101 </td>
   <td style="text-align:right;"> 3.3 </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 20%; font-weight: bold;"> 002 </td>
   <td style="text-align:right;width: 40%; "> 64 </td>
   <td style="text-align:right;width: 40%; "> 5 </td>
   <td style="text-align:right;"> 245 </td>
   <td style="text-align:right;"> 6.0 </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 20%; font-weight: bold;"> 003 </td>
   <td style="text-align:right;width: 40%; "> 33 </td>
   <td style="text-align:right;width: 40%; "> 7 </td>
   <td style="text-align:right;"> 69 </td>
   <td style="text-align:right;"> 3.5 </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 20%; font-weight: bold;"> 004 </td>
   <td style="text-align:right;width: 40%; "> 28 </td>
   <td style="text-align:right;width: 40%; "> 2 </td>
   <td style="text-align:right;"> 44 </td>
   <td style="text-align:right;"> 27.0 </td>
  </tr>
</tbody>
</table>

Jawablah pertanyaan-pertanyaan berikut berdasarkan tabel tersebut:

a. Ada berapa objek dalam data terstruktur tersebut? 
b. Sebutkan apa kira-kira objek dari data terstruktur tersebut.
c. Berapa variabel yang dapat dianalisis dari data terstruktur tersebut? Sebutkan apa saja.
d. Apakah format tabel tersebut sesuai dengan prinsip data yang rapi? Jelaskan alasan Anda.
:::

## Tingkat Pengukuran Variabel

Pada subbab ini kita akan membahas lebih dalam tentang nilai dalam variabel yang berpengaruh pada analisis selanjutnya, yakni tingkat pengukuran variabel.

Sebagaimana telah disebutkan pada Subbab \@ref(analisis-kuantitatif-vs-kualitatif) bahwa pengumpulan data kuantitatif dapat disebut juga sebagai pengukuran suatu variabel, cara kita mengukur suatu variabel bisa diibaratkan seperti menggunakan mistar yang memiliki sederet angka [@kachigan1986statistical].

Tingkat pengukuran berbicara tentang cara kita menyatakan hasil pengukuran suatu variabel tersebut dalam angka, mulai dari hasil yang sangat menyerupai angka dalam mistar hingga hasil yang bukan angka sama sekali.

::: rmdkasus
### Studi Kasus: Tingkat Pengukuran Variabel {.unnumbered}

Sesuai dengan kasus \@ref(kasus-elemen-data-terstruktur), kita akan menggunakan kasus variabel `Usia` dari data terstruktur tersebut.

Dalam variabel tersebut, nilai `Usia` dapat kita nyatakan dalam 2 bentuk yang berbeda. Kita akan bedakan bentuknya menjadi kasus-kasus berikut:

1. **Kasus-1:** nilai `Usia` dinyatakan dalam bentuk angka dalam satuan tahun. Dengan demikian, dalam kasus ini nilai `17` berarti "17 tahun", dan nilai `26` berarti "26 tahun", dan seterusnya.

2. **Kasus-2:** nilai `Usia` dinyatakan dalam bentuk rentang usia seperti berikut:

    * kategori 1: 17-25 tahun
    * kategori 2: 26-35 tahun
    * kategori 3: 36-45 tahun
    * kategori 4: 46-55 tahun
    * kategori 5: 56-65 tahun

    Kita bisa menyatakan setiap kategori dengan angka tertentu yang masing-masingnya tentu mewakili rentang usia tersebut. Misalnya, kita bisa menyatakan kategori 1 dengan angka 17, kategori 2 dengan angka 26, dan seterusnya, sehingga rentangnya menjadi seperti ini:

    * 17: 17-25 tahun
    * 26: 26-35 tahun
    * 36: 36-45 tahun
    * 46: 46-55 tahun
    * 56: 56-65 tahun

    Dalam kasus ini, nilai `17` bukan lagi berarti "17 tahun", melainkan "17-25 tahun". Artinya nilai `17` ini bisa saja bernilai `17` atau `18` atau `19` atau `20` atau `21` atau `22` atau `23` atau `24` atau `25`.

Kedua kasus tersebut menunjukkan bahwa kita bisa menggunakan tingkat pengukuran yang berbeda untuk variabel yang sama. 

Kita akan mempelajari nama-nama tingkat pengukuran tersebut dalam subbab-subbab selanjutnya.
:::

## Jenis-jenis Tingkat Pengukuran Variabel

Tingkat pengukuran variabel secara umum memiliki 3 jenis dari yang paling rendah ke yang paling tinggi di antaranya adalah nominal, ordinal, dan metrik (metric). Kita akan bahas lebih dalam tentang jenis-jenis tersebut sebagai berikut mulai dari yang paling rendah ke yang paling tinggi.

### Nominal

Tingkat pengukuran nominal adalah tingkat pengukuran yang **paling rendah**. Jika angka dikenakan pada variabel ini, angka tersebut hanya bertindak sebagai label.

### Ordinal

Tingkat pengukuran ordinal berada di atas nominal. Angka pada tingkat ini hanya menunjukkan **urutan** atau **posisi** tetapi tidak dapat memberikan penafsiran berapa jarak di antara posisi-posisi tersebut.

### Metrik (Angka)

Variabel dengan tingkat pengukuran angka (bahasa Inggris: *metric*) adalah variabel dengan **angka yang sebenarnya** karena angka pada tingkat pengukuran ini memiliki penafsiran angka yang sebenarnya, yaitu memiliki posisi dan skala nilainya.

Dalam literatur lain, seperti @tjokropandojo2021pengantar, tingkat pengukuran ini banyak dibagi menjadi dua tingkat lagi, yaitu **interval** dan **rasio**. Perbedaan antara keduanya adalah bahwa interval **tidak memiliki posisi nol absolut** seperti rasio.

Contoh yang paling mudah adalah suhu. Suhu dapat dinyatakan dalam skala Celsius dan Fahrenheit. Dalam skala Celsius, air membeku pada tingkat 0 derajat, tetapi dalam skala Fahrenheit air membeku pada tingkat 32 derajat. Ini menunjukkan posisi nol yang tidak absolut pada pengukuran suhu.

Contoh lainnya adalah tahun. Dalam penanggalan Masehi, tahun-0 ditempatkan pada masa kelahiran Isa Al-Masih. Sementara itu, dalam penanggalan Hijriah, tahun-0 ditempatkan masa hijrahnya Nabi Muhammad SAW. Masa kelahiran Isa Al-Masih tentunya terjadi lebih dulu dibandingkan masa hijrah Nabi Muhammad SAW. Ini juga menunjukkan posisi nol yang tidak absolut pada pengukuran tahun.

## Menentukan Tingkat Pengukuran Variabel

Dalam praktiknya, menentukan tingkat pengukuran variabel seringkali tidak mudah karena seringkali data yang kita kumpulkan tidak memiliki tingkat pengukuran yang jelas. Oleh karena itu, kita perlu melakukan analisis lebih dalam untuk menentukan tingkat pengukuran variabel tersebut. Berikut adalah langkah-langkah yang dapat kita lakukan untuk menentukan tingkat pengukuran variabel.

1. Tentukan apakah jenis nilai dari variabel: apakah **kategorik** atau **numerik**
2. Jika **kategorik**, tentukan apakah terdapat tingkatan yang masuk akal. Jika terdapat tingkatan, maka ia pasti berupa ordinal. Jika tidak terdapat tingkatan, maka ia pasti berupa nominal.
3. Jika **numerik**, pastikan apakah angka-angka merepresentasikan angka sebenarnya. Jika tidak, ia sebenarnya adalah **kategorik**. Kembali ke langkah 1.
4. Jika **numerik** dan angka-angka merepresentasikan angka sebenarnya, pastikan apakah angka-angka memiliki posisi nol absolut. Jika tidak, ia pasti berupa **interval**. Jika ya, ia pasti berupa **rasio**.

Langkah-langkah tersebut dapat diilustrasikan dalam diagram alir yang ditampilkan dalam Gambar \@ref(fig:fig-menentukan-tingpeng) berikut. 

<div class="figure" style="text-align: center">
<img src="images/bab-2-menentukan-tingpeng.svg" alt="Diagram alir menentukan tingkat pengukuran variabel"  />
<p class="caption">(\#fig:fig-menentukan-tingpeng)Diagram alir menentukan tingkat pengukuran variabel</p>
</div>

::: rmdkasus
### Studi Kasus: Menentukan Tingkat Pengukuran Variabel {.unnumbered}

Melanjutkan kasus pengumpulan data pergerakan mahasiswa ITERA dari bab sebelumnya, setelah merumuskan pertanyaan penelitian mengenai keberlanjutan pola pergerakan, kita perlu menentukan variabel yang akan diukur. Berikut adalah variabel-variabel tersebut beserta penjelasannya:

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-2-rancangan-metadata)Penelaahan tingkat pengukuran variabel penelitian</caption>
 <thead>
  <tr>
   <th style="text-align:left;"> Variabel </th>
   <th style="text-align:left;"> Nama Panggilan </th>
   <th style="text-align:left;"> Penjelasan </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> Moda transportasi yang digunakan responden </td>
   <td style="text-align:left;"> `kend` </td>
   <td style="text-align:left;"> Nilai-nilai dari moda transportasi bukanlah angka, melainkan label yang merepresentasikan jenis moda transportasi yang digunakan responden. Oleh karena itu, jenis nilai dari variabel ini adalah kategorik. Tidak ada tingkatan pada nilai-nilai di variabel ini, sehingga tingkat pengukurannya adalah nominal. </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Jarak tempuh dari rumah ke kampus </td>
   <td style="text-align:left;"> `jarak` </td>
   <td style="text-align:left;"> Nilai-nilai dari jarak tempuh dari rumah ke kampus adalah angka yang merepresentasikan jarak tempuh dari rumah ke kampus. Oleh karena itu, jenis nilai dari variabel ini adalah numerik. Angka 0 merepresentasikan tidak ada jarak tempuh. Karena ini angka sebenarnya dan memiliki makna 0 yang sebenarnya, maka tingkat pengukurannya adalah rasio. </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Banyaknya perjalanan ke kampus dalam satu pekan </td>
   <td style="text-align:left;"> `frek_jalan_sepekan` </td>
   <td style="text-align:left;"> Nilai-nilai dari banyaknya perjalanan ke kampus dalam satu pekan adalah angka yang merepresentasikan banyaknya perjalanan ke kampus dalam satu pekan. Oleh karena itu, jenis nilai dari variabel ini adalah numerik. Angka 0 merepresentasikan banyaknya perjalanan ke kampus 0 kali, atau tidak pernah ke kampus. Karena ini angka sebenarnya dan memiliki makna 0 yang sebenarnya, maka tingkat pengukurannya adalah rasio. </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Total biaya transportasi selama satu pekan </td>
   <td style="text-align:left;"> `biaya` </td>
   <td style="text-align:left;"> Nilai-nilai dari total biaya transportasi selama satu pekan adalah angka yang merepresentasikan total biaya transportasi selama satu pekan. Oleh karena itu, jenis nilai dari variabel ini adalah numerik. Angka 0 merepresentasikan total biaya transportasi 0 rupiah, atau tidak mengeluarkan biaya transportasi. Karena ini angka sebenarnya dan memiliki makna 0 yang sebenarnya, maka tingkat pengukurannya adalah rasio. </td>
  </tr>
</tbody>
</table>

Setelah menelaah jenis nilai dan tingkat pengukuran variabel, kita perlu menspesifikasikan nilai isian beserta satuannya. Jika menggunakan kodifikasi, aturannya harus diperjelas. Spesifikasi ini disebut **metadata**, yaitu data yang menjelaskan tentang data.

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-2-metadata)Metadata variabel penelitian</caption>
 <thead>
  <tr>
   <th style="text-align:left;"> Variabel </th>
   <th style="text-align:left;"> Nama Panggilan </th>
   <th style="text-align:left;"> Tingkat Pengukuran </th>
   <th style="text-align:left;"> Satuan </th>
   <th style="text-align:left;"> Nilai yang mungkin </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> Moda transportasi yang digunakan responden </td>
   <td style="text-align:left;"> `kend` </td>
   <td style="text-align:left;"> Nominal </td>
   <td style="text-align:left;"> Tidak ada </td>
   <td style="text-align:left;"> Sepeda motor, mobil, angkutan umum, dll </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Jarak tempuh dari rumah ke kampus </td>
   <td style="text-align:left;"> `jarak` </td>
   <td style="text-align:left;"> Metrik </td>
   <td style="text-align:left;"> km </td>
   <td style="text-align:left;"> 0 - ∞ km </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Banyaknya perjalanan ke kampus dalam satu pekan </td>
   <td style="text-align:left;"> `frek_jalan_sepekan` </td>
   <td style="text-align:left;"> Metrik </td>
   <td style="text-align:left;"> kali </td>
   <td style="text-align:left;"> 0 - 7 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Total biaya transportasi selama satu pekan </td>
   <td style="text-align:left;"> `biaya` </td>
   <td style="text-align:left;"> Metrik </td>
   <td style="text-align:left;"> rupiah (Rp) </td>
   <td style="text-align:left;"> 0 - ∞ </td>
  </tr>
</tbody>
</table>

**Mengubah Tingkat Pengukuran Variabel**

Kita sudah menentukan nilai dari telaahan variabel-variabel yang sudah kita buat sebelumnya. Pada hasil telaahan kita sebelumnya, kita memiliki satu variabel nominal dan 3 variabel numerik. Variabel nominal tersebut adalah `kend`, sedangkan variabel numerik tersebut adalah `jarak`, `frek_jalan_sepekan`, dan `biaya`.

Kita bisa mengubah tingkat pengukuran variabel dari satu tingkat ke lainnya. Misalnya, kita bisa mengubah tingkat pengukuran variabel `jarak` dari metrik (rasio) menjadi ordinal. Karena tingkat pengukuran variabel metrik adalah angka, untuk mengubahnya menjadi ordinal maka kita perlu mengubahnya menjadi kategorikal. Artinya, kita perlu membuat kategori baru dari variabel `jarak` tersebut.

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-2-ubah-tingkat-pengukuran)Metadata variabel penelitian yang diubah</caption>
 <thead>
  <tr>
   <th style="text-align:left;"> Variabel </th>
   <th style="text-align:left;"> Nama Panggilan </th>
   <th style="text-align:left;"> Tingkat Pengukuran </th>
   <th style="text-align:left;"> Satuan </th>
   <th style="text-align:left;"> Nilai yang mungkin </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> Moda transportasi yang digunakan responden </td>
   <td style="text-align:left;"> `kend` </td>
   <td style="text-align:left;"> Nominal </td>
   <td style="text-align:left;"> Tidak ada </td>
   <td style="text-align:left;"> Sepeda motor, mobil, angkutan umum, dll </td>
  </tr>
  <tr>
   <td style="text-align:left;background-color: rgba(255, 255, 204, 255) !important;"> Jarak tempuh dari rumah ke kampus </td>
   <td style="text-align:left;background-color: rgba(255, 255, 204, 255) !important;"> `jarak` </td>
   <td style="text-align:left;background-color: rgba(255, 255, 204, 255) !important;"> Ordinal </td>
   <td style="text-align:left;background-color: rgba(255, 255, 204, 255) !important;"> km </td>
   <td style="text-align:left;background-color: rgba(255, 255, 204, 255) !important;"> 0 - 5 km,<br>5 - 10 km,<br>10 - 15 km,<br>dll </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Banyaknya perjalanan ke kampus dalam satu pekan </td>
   <td style="text-align:left;"> `frek_jalan_sepekan` </td>
   <td style="text-align:left;"> Metrik </td>
   <td style="text-align:left;"> kali </td>
   <td style="text-align:left;"> 0 - 7 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Total biaya transportasi selama satu pekan </td>
   <td style="text-align:left;"> `biaya` </td>
   <td style="text-align:left;"> Metrik </td>
   <td style="text-align:left;"> rupiah (Rp) </td>
   <td style="text-align:left;"> 0 - ∞ </td>
  </tr>
</tbody>
</table>
:::


Jawablah soal evaluasi berikut untuk menguji pemahaman Anda tentang tingkat pengukuran variabel.

::: rmdexercise
## Soal Evaluasi 3 {.unnumbered}

Perhatikan cuplikan data hasil survei mahasiswa berikut ini:

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-2-eval-3-preview)Cuplikan data survei mahasiswa</caption>
 <thead>
  <tr>
   <th style="text-align:center;"> KodeResp </th>
   <th style="text-align:center;"> Usia </th>
   <th style="text-align:center;"> Fakultas </th>
   <th style="text-align:center;"> ThnMsk </th>
   <th style="text-align:center;"> UangSaku </th>
   <th style="text-align:center;"> Jarak </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:center;"> 001 </td>
   <td style="text-align:center;"> 22 </td>
   <td style="text-align:center;"> 1 </td>
   <td style="text-align:center;"> 2020 </td>
   <td style="text-align:center;"> 2 </td>
   <td style="text-align:center;"> 19.27 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 002 </td>
   <td style="text-align:center;"> 25 </td>
   <td style="text-align:center;"> 1 </td>
   <td style="text-align:center;"> 2020 </td>
   <td style="text-align:center;"> 1 </td>
   <td style="text-align:center;"> 0.58 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 003 </td>
   <td style="text-align:center;"> 24 </td>
   <td style="text-align:center;"> 2 </td>
   <td style="text-align:center;"> 2021 </td>
   <td style="text-align:center;"> 1 </td>
   <td style="text-align:center;"> 0.56 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 004 </td>
   <td style="text-align:center;"> 19 </td>
   <td style="text-align:center;"> 3 </td>
   <td style="text-align:center;"> 2022 </td>
   <td style="text-align:center;"> 1 </td>
   <td style="text-align:center;"> 1.05 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 005 </td>
   <td style="text-align:center;"> 23 </td>
   <td style="text-align:center;"> 2 </td>
   <td style="text-align:center;"> 2021 </td>
   <td style="text-align:center;"> 1 </td>
   <td style="text-align:center;"> 1.69 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 006 </td>
   <td style="text-align:center;"> 20 </td>
   <td style="text-align:center;"> 1 </td>
   <td style="text-align:center;"> 2020 </td>
   <td style="text-align:center;"> 3 </td>
   <td style="text-align:center;"> 1.37 </td>
  </tr>
</tbody>
</table>

Adapun keterangan dari variabel-variabel tersebut (metadata) adalah sebagai berikut:

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-2-eval-3-metadata)Metadata variabel survei mahasiswa</caption>
 <thead>
  <tr>
   <th style="text-align:left;"> Nama Variabel </th>
   <th style="text-align:left;"> Deskripsi </th>
   <th style="text-align:left;"> Nilai-nilai yang valid </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> `KodeResp` </td>
   <td style="text-align:left;"> Nomor urut responden </td>
   <td style="text-align:left;"> tiga digit angka, hingga jumlah responden minimal </td>
  </tr>
  <tr>
   <td style="text-align:left;"> `Usia` </td>
   <td style="text-align:left;"> Usia responden (tahun) </td>
   <td style="text-align:left;"> 18 - ∞ </td>
  </tr>
  <tr>
   <td style="text-align:left;"> `Fakultas` </td>
   <td style="text-align:left;"> Fakultas mahasiswa </td>
   <td style="text-align:left;"> 1 = Fakultas Syariah,<br>2 = Fakultas Tarbiyah dan Keguruan,<br>3 = Fakultas Dakwah dan Komunikasi </td>
  </tr>
  <tr>
   <td style="text-align:left;"> `ThnMsk` </td>
   <td style="text-align:left;"> Tahun masuk kuliah (Masehi) </td>
   <td style="text-align:left;"> 2018 - 2022 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> `UangSaku` </td>
   <td style="text-align:left;"> Uang saku mahasiswa per bulan </td>
   <td style="text-align:left;"> 1 = &lt;1 juta rupiah,<br>2 = 1-2 juta rupiah,<br>3 = 2-3 juta rupiah,<br>4 = 3-4 juta,<br>5 = &gt;4 juta </td>
  </tr>
  <tr>
   <td style="text-align:left;"> `Jarak` </td>
   <td style="text-align:left;"> Jarak tempat tinggal mahasiswa dari kampus (km) </td>
   <td style="text-align:left;"> 0 - ∞ </td>
  </tr>
</tbody>
</table>

Sebutkan tingkat pengukuran untuk variabel-variabel yang ada dalam set data tersebut dan jelaskan! [STP-2.1]{.capaian}

:::

<!--chapter:end:02-data-terstruktur.Rmd-->

# Analisis Statistik Deskriptif

::: rmdcapaian
### Capaian Pembelajaran {.unnumbered}

Setelah mempelajari bab ini, Anda diharapkan:

1.  mampu memilih statistik deskriptif yang tepat sesuai dengan variabel yang akan disajikan dan informasi yang ingin disampaikan [STP-2.2]{.capaian}
2.  mampu menginterpretasikan informasi dari persentase/proporsi, rasio, laju, ukuran pemusatan, dan ukuran penyebaran suatu data kuantiatif sesuai dengan konteks kasusnya [STP-2.3]{.capaian}
:::

## Makna Analisis Statistik Deskriptif

Statistik deskriptif adalah metode analisis untuk mendeskripsikan data dari sampel atau populasi. Metode ini digunakan untuk membantu kita menghasilkan informasi yang bermakna dan bernilai dari sekadar data mentah. Perlu dicatat bahwa analisis statistik deskriptif dapat digunakan pada data mentah entah berupa sampel atau populasi. Dengan demikian, statistik deskriptif sangat bergantung pada kondisi data mentah yang kita miliki.

Berdasarkan teknik yang digunakan, statistik deskriptif dapat dibagi menjadi 4 kategori: **ukuran frekuensi**, **ukuran kecenderungan memusat**, **ukuran penyebaran**, dan **tabel silang**. Setiap kategori teknik memiliki tingkat pengukuran yang sesuai untuk variabel yang akan dianalisi. Makna yang dihasilkan juga akan berbeda tergantung pada teknik yang digunakan.

::: rmdnote
[⚠️ Penting]{.tajuksaya}

Di sinilah letak krusialnya menentukan tingkat pengukuran variabel, karena akan menentukan teknik analisis statistik deskriptif apa yang akan digunakan. Sebagai contoh, kita tidak bisa menggunakan mean untuk mengukur variabel nominal.
:::

## Ukuran Frekuensi

Ukuran frekuensi adalah cara paling sederhana untuk memaknai satu variabel. Ukuran ini menyatakan frekuensi relatif objek-objek dilihat dari suatu variabel kategorik. Objek-objek dikelompokkan ke dalam kategori-kategori dan dihitung jumlahnya dan dibandingkan dengan jumlah keseluruhan objek tersebut. Untuk dapat menggunakan teknik ini, kita perlu melakukan pengolahan pada data mentah berupa variabel kategorik, yakni mengelompokkan objek berdasarkan kategori-kategori yang ada pada variabel tersebut dan menghitung frekuensi dari setiap kategori tersebut.

Secara matematis, ukuran frekuensi dapat dinyatakan sebagai berikut:

$$
\begin{equation}
\text{FR} = \frac{f}{n}
(\#eq:konsep-frekuensi-relatif)
\end{equation}
$$

dengan:

-   $FR$ = Frekuensi Relatif
-   $f$ = Frekuensi suatu kategori
-   $n$ = Jumlah Observasi

Makna yang dihasilkan dari teknik ini adalah seberapa besar perbandingan jumlah objek pada suatu kategori relatif terhadap jumlah keseluruhan objeknya. Dari besar perbandingan tersebut, kita dapat mengetahui dominasi kategori tertentu pada objek-objek yang diamati serta perbandingan yang adil antar kumpulan objek dengan kategorisasi yang sama.

Karena rumus perhitungan frekuensi relatif melibatkan penghitungan frekuensi atau jumlah objek (Persamaan \@ref(eq:konsep-frekuensi-relatif)), maka teknik ini hanya dapat digunakan pada data nominal dan ordinal. Teknik ini tidak dapat digunakan pada data interval dan rasio karena data interval dan rasio tidak memiliki kategori.

::: rmdkasus
### Studi Kasus: Penerapan Ukuran Frekuensi dari Dataset Hasil Survei {.unnumbered}

Sekarang kita akan membahas teknik analisis statistik dalam set data (dataset) mengenai pola pergerakan mahasiswa di ITERA. Untuk kepentingan kelengkapan ulasan, variabelnya kita tambah dengan satu variabel ordinal: tingkat tahun kuliah (`tingkat`).

Berikut adalah contoh set data hasil kuesioner yang sudah disebarkan beserta metadatanya:

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-3-kasus-dataset)Contoh Set Data Hasil Kuesioner</caption>
 <thead>
  <tr>
   <th style="text-align:center;"> ID </th>
   <th style="text-align:center;"> kend </th>
   <th style="text-align:center;"> tingkat </th>
   <th style="text-align:center;"> jarak </th>
   <th style="text-align:center;"> perjalanan_senin </th>
   <th style="text-align:center;"> biaya_pekan </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:center;"> 117 </td>
   <td style="text-align:center;"> 5 </td>
   <td style="text-align:center;"> 4 </td>
   <td style="text-align:center;"> 2.34 </td>
   <td style="text-align:center;"> 3 </td>
   <td style="text-align:center;"> 0 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 118 </td>
   <td style="text-align:center;"> 1 </td>
   <td style="text-align:center;"> 4 </td>
   <td style="text-align:center;"> 2.66 </td>
   <td style="text-align:center;"> 2 </td>
   <td style="text-align:center;"> 40 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 119 </td>
   <td style="text-align:center;"> 1 </td>
   <td style="text-align:center;"> 4 </td>
   <td style="text-align:center;"> 3.84 </td>
   <td style="text-align:center;"> 2 </td>
   <td style="text-align:center;"> 30 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 120 </td>
   <td style="text-align:center;"> 1 </td>
   <td style="text-align:center;"> 4 </td>
   <td style="text-align:center;"> 3.64 </td>
   <td style="text-align:center;"> 3 </td>
   <td style="text-align:center;"> 40 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 121 </td>
   <td style="text-align:center;"> 1 </td>
   <td style="text-align:center;"> 3 </td>
   <td style="text-align:center;"> 3.17 </td>
   <td style="text-align:center;"> 2 </td>
   <td style="text-align:center;"> 45 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 138 </td>
   <td style="text-align:center;"> 3 </td>
   <td style="text-align:center;"> 4 </td>
   <td style="text-align:center;"> 3.84 </td>
   <td style="text-align:center;"> 3 </td>
   <td style="text-align:center;"> 15 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 139 </td>
   <td style="text-align:center;"> 3 </td>
   <td style="text-align:center;"> 3 </td>
   <td style="text-align:center;"> 3.84 </td>
   <td style="text-align:center;"> 4 </td>
   <td style="text-align:center;"> 60 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 161 </td>
   <td style="text-align:center;"> 5 </td>
   <td style="text-align:center;"> 2 </td>
   <td style="text-align:center;"> 3.52 </td>
   <td style="text-align:center;"> 4 </td>
   <td style="text-align:center;"> 0 </td>
  </tr>
</tbody>
</table>

**Metadata:**

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-3-kasus-metadata)Metadata Variabel</caption>
 <thead>
  <tr>
   <th style="text-align:left;"> Variabel </th>
   <th style="text-align:left;"> Keterangan </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;width: 20%; font-weight: bold;"> ID </td>
   <td style="text-align:left;width: 80%; "> Nomor urut responden </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 20%; font-weight: bold;"> kend </td>
   <td style="text-align:left;width: 80%; "> Jenis kendaraan yang digunakan<br>1 = sepeda motor pribadi<br>2 = mobil pribadi<br>3 = layanan online<br>4 = menumpang kawan<br>5 = sepeda<br>6 = berjalan kaki </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 20%; font-weight: bold;"> tingkat </td>
   <td style="text-align:left;width: 80%; "> Tingkat semester kuliah<br>1 = Tahun pertama<br>2 = Tahun kedua<br>3 = Tahun ketiga<br>4 = Tahun keempat<br>5 = Swasta (mahasiswa tingkat akhir) </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 20%; font-weight: bold;"> jarak </td>
   <td style="text-align:left;width: 80%; "> Jarak tempat tinggal mahasiswa dari kampus (kilometer) </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 20%; font-weight: bold;"> perjalanan_senin </td>
   <td style="text-align:left;width: 80%; "> Frekuensi perjalanan di hari Senin </td>
  </tr>
  <tr>
   <td style="text-align:left;width: 20%; font-weight: bold;"> biaya_pekan </td>
   <td style="text-align:left;width: 80%; "> Biaya perjalanan selama sepekan (ribu rupiah) </td>
  </tr>
</tbody>
</table>

Ukuran frekuensi dapat dilakukan pada variabel kategorik (tingkat pengukuran nominal atau ordinal), seperti `kend` dan `tingkat`. Untuk dapat menghitung analisis ini kita harus membuat terlebih dahulu tabel frekuensi untuk kedua variabel ini. Kemudian, barulah kita dapat menghitung frekuensi relatifnya menggunakan Persamaan \@ref(eq:konsep-frekuensi-relatif)

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-3-tabel-frekuensi-kend)Tabel Distribusi Frekuensi Untuk Variabel `kend`</caption>
 <thead>
  <tr>
   <th style="text-align:center;"> kend </th>
   <th style="text-align:center;"> Jenis kendaraan </th>
   <th style="text-align:center;"> Frekuensi </th>
   <th style="text-align:center;"> Frekuensi Relatif </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:center;"> 1 </td>
   <td style="text-align:center;"> Sepeda motor pribadi </td>
   <td style="text-align:center;"> 4 </td>
   <td style="text-align:center;"> 0.50 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 2 </td>
   <td style="text-align:center;"> Mobil pribadi </td>
   <td style="text-align:center;"> 0 </td>
   <td style="text-align:center;"> 0.00 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 3 </td>
   <td style="text-align:center;"> Layanan online </td>
   <td style="text-align:center;"> 2 </td>
   <td style="text-align:center;"> 0.25 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 4 </td>
   <td style="text-align:center;"> Menumpang kawan </td>
   <td style="text-align:center;"> 0 </td>
   <td style="text-align:center;"> 0.00 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 5 </td>
   <td style="text-align:center;"> Sepeda </td>
   <td style="text-align:center;"> 2 </td>
   <td style="text-align:center;"> 0.25 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 6 </td>
   <td style="text-align:center;"> Berjalan kaki </td>
   <td style="text-align:center;"> 0 </td>
   <td style="text-align:center;"> 0.00 </td>
  </tr>
  <tr>
   <td style="text-align:center;font-weight: bold;"> Total </td>
   <td style="text-align:center;font-weight: bold;">  </td>
   <td style="text-align:center;font-weight: bold;"> 8 </td>
   <td style="text-align:center;font-weight: bold;"> 1.00 </td>
  </tr>
</tbody>
</table>

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-3-tabel-frekuensi-tingkat)Tabel Distribusi Frekuensi Untuk Variabel `tingkat`</caption>
 <thead>
  <tr>
   <th style="text-align:center;"> tingkat </th>
   <th style="text-align:center;"> Tingkat kuliah </th>
   <th style="text-align:center;"> Frekuensi </th>
   <th style="text-align:center;"> Frekuensi Relatif </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:center;"> 1 </td>
   <td style="text-align:center;"> Tahun pertama </td>
   <td style="text-align:center;"> 0 </td>
   <td style="text-align:center;"> 0.000 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 2 </td>
   <td style="text-align:center;"> Tahun kedua </td>
   <td style="text-align:center;"> 1 </td>
   <td style="text-align:center;"> 0.125 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 3 </td>
   <td style="text-align:center;"> Tahun ketiga </td>
   <td style="text-align:center;"> 2 </td>
   <td style="text-align:center;"> 0.250 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 4 </td>
   <td style="text-align:center;"> Tahun keempat </td>
   <td style="text-align:center;"> 5 </td>
   <td style="text-align:center;"> 0.625 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 5 </td>
   <td style="text-align:center;"> Swasta (tingkat akhir) </td>
   <td style="text-align:center;"> 0 </td>
   <td style="text-align:center;"> 0.000 </td>
  </tr>
  <tr>
   <td style="text-align:center;font-weight: bold;"> Total </td>
   <td style="text-align:center;font-weight: bold;">  </td>
   <td style="text-align:center;font-weight: bold;"> 8 </td>
   <td style="text-align:center;font-weight: bold;"> 1.000 </td>
  </tr>
</tbody>
</table>
:::

Teknik-teknik analisis statistik deskriptif yang termasuk ke dalam kelompok ukuran frekuensi di antaranya adalah **persentase/proporsi**, **laju**, **rasio**, dan **perubahan persentase**. Silakan pelajari cara penggunaan masing-masing teknik disertai kasus penerapannya.

### Persentase dan Proporsi

Dua jenis ukuran frekuensi yang paling sering dipakai adalah persentase dan proporsi [@ewing2020basic]. Kedua teknik ini menghasilkan nilai yang sama, hanya saja dinyatakan dalam skala yang berbeda. Persentase dinyatakan dalam skala 0-100 dengan satuan persen (%), sedangkan proporsi dinyatakan dalam skala 0-1. Dengan demikian, dapat dikatakan bahwa sebenarnya Persamaan \@ref(eq:konsep-frekuensi-relatif) adalah proporsi dan persentase adalah proporsi yang dikalikan dengan 100.

$$
\begin{equation}
\text{Persentase} = \frac{f}{n} \times 100\%
(\#eq:konsep-persentase)
\end{equation}
$$

Makna yang bisa kita dapatkan dari analisis ini adalah dominansi suatu kategori terhadap kategori lainnya. Selain itu, ketika membandingkan dua kelompok yang jumlah totalnya berbeda, kita bisa membandingkan satu kategori yang sama pada kelompok tersebut secara adil.

::: rmdnote
[Catatan]{.tajuksaya}

Selain persen (per 100), ada juga satuan 'permil' (per 1000) dengan simbol ‰, yang biasa digunakan pada perhitungan-perhitungan yang melibatkan bilangan yang sangat kecil.
:::

::: rmdkasus
### Studi Kasus: Penerapan Persentase dan Proporsi {.unnumbered}

Salah satu keunggulan persentase adalah kemampuannya untuk membandingkan dominansi suatu kategori pada dua kelompok yang memiliki jumlah total berbeda secara adil. Mari kita bandingkan penggunaan sepeda motor pribadi sebagai kendaraan utama di dua perguruan tinggi: ITERA dan UBL.

Berdasarkan survei pola mobilitas mahasiswa, diperoleh data sebagai berikut:

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-3-perbandingan-kampus)Data Pengguna Sepeda Motor Pribadi di ITERA dan UBL</caption>
 <thead>
  <tr>
   <th style="text-align:center;"> Kampus </th>
   <th style="text-align:center;"> Total Responden </th>
   <th style="text-align:center;"> Pengguna Sepeda Motor Pribadi </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:center;"> ITERA </td>
   <td style="text-align:center;"> 429 </td>
   <td style="text-align:center;"> 276 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> UBL </td>
   <td style="text-align:center;"> 380 </td>
   <td style="text-align:center;"> 195 </td>
  </tr>
</tbody>
</table>

**Perbandingan Menggunakan Frekuensi Absolut:**

Jika kita hanya membandingkan jumlah absolut, ITERA memiliki 276 pengguna sepeda motor sedangkan UBL memiliki 195 pengguna. Apakah ini berarti penggunaan sepeda motor lebih dominan di ITERA? **Belum tentu**, karena total responden di kedua kampus berbeda.

**Perbandingan Menggunakan Persentase:**

Mari kita hitung persentase pengguna sepeda motor di masing-masing kampus menggunakan Persamaan \@ref(eq:konsep-persentase):

**ITERA:**

$$
\text{Persentase sepeda motor ITERA} = \frac{276}{429} \times 100\% = 64,3\%
$$

**UBL:**
$$
\text{Persentase sepeda motor UBL} = \frac{195}{380} \times 100\% = 51,3\%
$$

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-3-hasil-perbandingan)Perbandingan Proporsi dan Persentase Pengguna Sepeda Motor</caption>
 <thead>
  <tr>
   <th style="text-align:center;"> Kampus </th>
   <th style="text-align:center;"> Total Responden </th>
   <th style="text-align:center;"> Pengguna Motor </th>
   <th style="text-align:center;"> Proporsi </th>
   <th style="text-align:center;"> Persentase </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:center;"> ITERA </td>
   <td style="text-align:center;"> 429 </td>
   <td style="text-align:center;"> 276 </td>
   <td style="text-align:center;"> 0.643 </td>
   <td style="text-align:center;font-weight: bold;background-color: rgba(232, 244, 248, 255) !important;"> 64,3% </td>
  </tr>
  <tr>
   <td style="text-align:center;"> UBL </td>
   <td style="text-align:center;"> 380 </td>
   <td style="text-align:center;"> 195 </td>
   <td style="text-align:center;"> 0.513 </td>
   <td style="text-align:center;font-weight: bold;background-color: rgba(232, 244, 248, 255) !important;"> 51,3% </td>
  </tr>
</tbody>
</table>

**Interpretasi:**

Dengan menggunakan persentase, kita dapat membandingkan kedua kampus secara adil meskipun jumlah respondennya berbeda:

1.  **Dominansi di ITERA**: Sebanyak 64,3% mahasiswa ITERA menggunakan sepeda motor pribadi sebagai kendaraan utama
2.  **Dominansi di UBL**: Sebanyak 51,3% mahasiswa UBL menggunakan sepeda motor pribadi sebagai kendaraan utama
3.  **Kesimpulan**: Penggunaan sepeda motor lebih dominan di ITERA dibandingkan UBL, dengan selisih 13 poin persentase

Tanpa persentase, kita akan salah menyimpulkan hanya berdasarkan jumlah absolut (276 vs 195). Persentase memberikan ukuran yang adil untuk membandingkan dominansi kategori pada kelompok dengan ukuran berbeda.

**Implikasi untuk Perencanaan:**

Informasi ini penting bagi perencana transportasi kampus untuk: - ITERA perlu menyediakan area parkir motor yang lebih luas (minimal 64% dari kapasitas mahasiswa) - UBL dapat mengalokasikan lebih banyak ruang untuk moda transportasi alternatif karena dominansi motor lebih rendah
:::

### Laju *(Rate)*

Hampir sama dengan persentase, laju juga merupakan ukuran frekuensi relatif. Perbedaan dengan persentase terletak pada ide dari pembagi (denominator) yang digunakan. Persentase digunakan pada kondisi jumlah keseluruhan objek tidak berubah atau statis. Sementara laju digunakan pada kondisi jumlah keseluruhan objek berubah atau dinamis.

$$
\begin{equation}
\text{Laju} = \frac{f}{n_i} \times 100\%
(\#eq:konsep-laju)
\end{equation}
$$

Pada Persamaan \@ref(eq:konsep-laju), *subscript* $i$ ditambahkan untuk menandakan bahwa jumlah keseluruhan yang menjadi denominator adalah jumlah yang bersifat dinamis.

Makna yang kita dapatkan dari hasil analisis ini sama persis seperti persentase dan proporsi, yakni perbandingan adil suatu kategori dari sejumlah kelompok yang berbeda. Perbedaannya hanya terletak pada ide dari jumlah pembagi yang bisa berubah-ubah sepanjang waktu.

::: rmdkasus
### Studi Kasus: Perhitungan Laju {.unnumbered}

Konsep laju sangat penting dalam analisis transportasi, terutama untuk memahami dinamika perubahan pola pergerakan dari waktu ke waktu. Berbeda dengan persentase yang mengukur bagian dari total yang statis, laju mengukur tingkat perubahan relatif terhadap populasi yang berubah.

Misalkan kita memiliki data survei pola mobilitas mahasiswa dari tiga perguruan tinggi di Lampung (UBL, ITERA, dan UNILA) yang dilakukan pada dua periode berbeda: 2023 dan 2024. Kita tertarik untuk mengetahui laju pertumbuhan penggunaan sepeda motor pribadi sebagai moda transportasi utama.

**Data Tahun 2023:**

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-3-data-laju-2023)Data Pengguna Sepeda Motor Tahun 2023</caption>
 <thead>
  <tr>
   <th style="text-align:center;"> Kampus </th>
   <th style="text-align:center;"> Jumlah Mahasiswa </th>
   <th style="text-align:center;"> Pengguna Sepeda Motor </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:center;"> UBL </td>
   <td style="text-align:center;"> 8500 </td>
   <td style="text-align:center;"> 5100 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> ITERA </td>
   <td style="text-align:center;"> 5200 </td>
   <td style="text-align:center;"> 3380 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> UNILA </td>
   <td style="text-align:center;"> 12000 </td>
   <td style="text-align:center;"> 7800 </td>
  </tr>
</tbody>
</table>

**Data Tahun 2024:**

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-3-data-laju-2024)Data Pengguna Sepeda Motor Tahun 2024</caption>
 <thead>
  <tr>
   <th style="text-align:center;"> Kampus </th>
   <th style="text-align:center;"> Jumlah Mahasiswa </th>
   <th style="text-align:center;"> Pengguna Sepeda Motor </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:center;"> UBL </td>
   <td style="text-align:center;"> 9200 </td>
   <td style="text-align:center;"> 6072 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> ITERA </td>
   <td style="text-align:center;"> 5800 </td>
   <td style="text-align:center;"> 4350 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> UNILA </td>
   <td style="text-align:center;"> 13500 </td>
   <td style="text-align:center;"> 9450 </td>
  </tr>
</tbody>
</table>

Dengan menggunakan Persamaan \@ref(eq:konsep-laju), kita dapat menghitung laju penggunaan sepeda motor untuk masing-masing kampus:

**Perhitungan untuk UBL:**

$$
\text{Laju 2023} = \frac{5.100}{8.500} \times 100\% = 60,0\%
$$

$$
\text{Laju 2024} = \frac{6.072}{9.200} \times 100\% = 66,0\%
$$

**Perhitungan untuk ITERA:**

$$
\text{Laju 2023} = \frac{3.380}{5.200} \times 100\% = 65,0\%
$$

$$
\text{Laju 2024} = \frac{4.350}{5.800} \times 100\% = 75,0\%
$$

**Perhitungan untuk UNILA:**

$$
\text{Laju 2023} = \frac{7.800}{12.000} \times 100\% = 65,0\%
$$

$$
\text{Laju 2024} = \frac{9.450}{13.500} \times 100\% = 70,0\%
$$

**Interpretasi:**

Hasil perhitungan menunjukkan bahwa laju penggunaan sepeda motor meningkat di semua kampus. ITERA mengalami peningkatan laju tertinggi (10 poin persentase, dari 65% menjadi 75%), diikuti oleh UBL (6 poin persentase) dan UNILA (5 poin persentase).

Perhatikan bahwa meskipun jumlah mahasiswa di setiap kampus bertambah dari tahun 2023 ke 2024, kita tetap dapat membandingkan laju penggunaan sepeda motor karena denominatornya disesuaikan dengan jumlah mahasiswa pada setiap periode. Ini berbeda dengan persentase biasa yang menggunakan denominator tetap.

Informasi laju ini sangat berguna bagi perencana transportasi untuk memahami tren penggunaan moda transportasi dan merencanakan infrastruktur yang sesuai, seperti area parkir kendaraan bermotor di kampus.
:::

### Rasio

Jika frekuensi relatif di awal membandingkan frekuensi objek pada suatu kategori dengan jumlah objek keseluruhan, rasio membandingkan frekuensi objek pada suatu kategori **terhadap kategori lain**.

$$
\begin{equation}
\text{Rasio} = \frac{n_i}{n_j}
(\#eq:konsep-rasio)
\end{equation}
$$

dengan:

-   $n_i$ = Jumlah objek pada kategori i
-   $n_j$ = Jumlah objek pada kategori j

Makna yang bisa kita hasilkan dari perhitungan ini adalah ketimpangan dari dua kategori yang dibandingkan. Biasanya dinyatakan dalam bentuk perbandingan "1:n" yang berarti "setiap 1 objek kategori x terdapat n objek kategori y".

::: rmdkasus
### Studi Kasus: Perhitungan Rasio Penggunaan Kendaraan {.unnumbered}

Rasio sangat berguna untuk membandingkan dua kategori yang berbeda dalam suatu variabel. Dalam studi transportasi, kita sering ingin membandingkan penggunaan berbagai jenis moda transportasi untuk memahami preferensi dan pola mobilitas.

Mari kita gunakan data mahasiswa ITERA untuk menghitung rasio penggunaan kendaraan bermotor terhadap kendaraan non-bermotor. Berdasarkan data survei pola mobilitas mahasiswa ITERA, kita dapat mengelompokkan jenis kendaraan menjadi dua kategori besar:

**Kendaraan Bermotor:** - Sepeda Motor Pribadi - Mobil Pribadi\
- Transportasi Online - Kendaraan Bermotor (menumpang dengan keluarga/teman)

**Kendaraan Non-Bermotor:** - Sepeda - Berjalan Kaki

Dari dataset yang berisi 429 responden mahasiswa ITERA, diperoleh distribusi sebagai berikut:

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-3-data-rasio-itera)Distribusi Penggunaan Kendaraan Mahasiswa ITERA</caption>
 <thead>
  <tr>
   <th style="text-align:center;"> Kategori Kendaraan </th>
   <th style="text-align:center;"> Jumlah Mahasiswa </th>
   <th style="text-align:center;"> Persentase </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:center;"> Kendaraan Bermotor </td>
   <td style="text-align:center;"> 398 </td>
   <td style="text-align:center;"> 92,8% </td>
  </tr>
  <tr>
   <td style="text-align:center;"> Kendaraan Non-Bermotor </td>
   <td style="text-align:center;"> 31 </td>
   <td style="text-align:center;"> 7,2% </td>
  </tr>
  <tr>
   <td style="text-align:center;font-weight: bold;"> Total </td>
   <td style="text-align:center;font-weight: bold;"> 429 </td>
   <td style="text-align:center;font-weight: bold;"> 100% </td>
  </tr>
</tbody>
</table>

**Detail per jenis kendaraan:**

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-3-detail-kendaraan-itera)Detail Jenis Kendaraan yang Digunakan</caption>
 <thead>
  <tr>
   <th style="text-align:center;"> Jenis Kendaraan </th>
   <th style="text-align:center;"> Kategori </th>
   <th style="text-align:center;"> Jumlah </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:center;background-color: rgba(232, 244, 248, 255) !important;"> Sepeda Motor Pribadi </td>
   <td style="text-align:center;background-color: rgba(232, 244, 248, 255) !important;"> Bermotor </td>
   <td style="text-align:center;background-color: rgba(232, 244, 248, 255) !important;"> 276 </td>
  </tr>
  <tr>
   <td style="text-align:center;background-color: rgba(232, 244, 248, 255) !important;"> Mobil Pribadi </td>
   <td style="text-align:center;background-color: rgba(232, 244, 248, 255) !important;"> Bermotor </td>
   <td style="text-align:center;background-color: rgba(232, 244, 248, 255) !important;"> 47 </td>
  </tr>
  <tr>
   <td style="text-align:center;background-color: rgba(232, 244, 248, 255) !important;"> Transportasi Online </td>
   <td style="text-align:center;background-color: rgba(232, 244, 248, 255) !important;"> Bermotor </td>
   <td style="text-align:center;background-color: rgba(232, 244, 248, 255) !important;"> 32 </td>
  </tr>
  <tr>
   <td style="text-align:center;background-color: rgba(232, 244, 248, 255) !important;"> Menumpang (Kendaraan Bermotor) </td>
   <td style="text-align:center;background-color: rgba(232, 244, 248, 255) !important;"> Bermotor </td>
   <td style="text-align:center;background-color: rgba(232, 244, 248, 255) !important;"> 43 </td>
  </tr>
  <tr>
   <td style="text-align:center;background-color: rgba(248, 249, 232, 255) !important;"> Sepeda </td>
   <td style="text-align:center;background-color: rgba(248, 249, 232, 255) !important;"> Non-Bermotor </td>
   <td style="text-align:center;background-color: rgba(248, 249, 232, 255) !important;"> 18 </td>
  </tr>
  <tr>
   <td style="text-align:center;background-color: rgba(248, 249, 232, 255) !important;"> Berjalan Kaki </td>
   <td style="text-align:center;background-color: rgba(248, 249, 232, 255) !important;"> Non-Bermotor </td>
   <td style="text-align:center;background-color: rgba(248, 249, 232, 255) !important;"> 13 </td>
  </tr>
</tbody>
</table>

Menggunakan Persamaan \@ref(eq:konsep-rasio), kita dapat menghitung rasio penggunaan kendaraan bermotor terhadap kendaraan non-bermotor:

$$
\text{Rasio} = \frac{n_{\text{bermotor}}}{n_{\text{non-bermotor}}} = \frac{398}{31} = 12,84
$$

**Interpretasi:**

Rasio 12,84 berarti bahwa untuk setiap 1 mahasiswa yang menggunakan kendaraan non-bermotor (sepeda atau berjalan kaki), terdapat sekitar 13 mahasiswa yang menggunakan kendaraan bermotor. Nilai rasio ini dapat juga dinyatakan sebagai **12,84:1** atau dibulatkan menjadi **13:1**.

Rasio yang tinggi ini menunjukkan dominasi penggunaan kendaraan bermotor di kalangan mahasiswa ITERA. Informasi ini penting bagi perencana kampus untuk:

1.  Merencanakan kapasitas area parkir kendaraan bermotor yang memadai
2.  Mempertimbangkan program promosi penggunaan kendaraan non-bermotor demi keberlanjutan
3.  Merancang infrastruktur jalur sepeda dan pejalan kaki yang aman

Kita juga dapat menghitung rasio antar jenis kendaraan bermotor. Misalnya, rasio penggunaan sepeda motor pribadi terhadap mobil pribadi:

$$
\text{Rasio motor:mobil} = \frac{276}{47} = 5,87 \approx 6:1
$$

Artinya, untuk setiap 1 mahasiswa yang menggunakan mobil pribadi, terdapat sekitar 6 mahasiswa yang menggunakan sepeda motor pribadi.
:::

### Perubahan Persentase (*Percentage Change*)

Mengukur perubahan sosial dalam berbagai bentuknya merupakan tugas penting dalam ilmu-ilmu sosial [@healey2021statistics]. Salah satu statistik yang sangat berguna untuk tujuan ini adalah **perubahan persentase** (*percentage change*), yang menunjukkan seberapa besar suatu variabel telah meningkat atau menurun selama periode waktu tertentu.

Untuk menghitung perubahan persentase, kita memerlukan nilai suatu variabel pada dua titik waktu yang berbeda. Nilai-nilai tersebut dapat berupa frekuensi, laju, atau persentase itu sendiri. Perubahan persentase akan memberitahu kita seberapa besar perubahan yang terjadi pada waktu kemudian relatif terhadap waktu sebelumnya.

Rumus perubahan persentase adalah:

$$
\begin{equation}
\text{Perubahan Persentase} = \left(\frac{f_2 - f_1}{f_1}\right) \times 100\%
(\#eq:konsep-percentage-change)
\end{equation}
$$

dengan:

-   $f_1$ = Nilai pertama (waktu awal), frekuensi, atau nilai
-   $f_2$ = Nilai kedua (waktu kemudian), frekuensi, atau nilai

Makna yang dihasilkan dari analisis ini adalah magnitud (besar nilai) dan arah perubahan yang terjadi. Tanda positif menunjukkan peningkatan, sedangkan tanda negatif menunjukkan penurunan.

::: rmdkasus
### Studi Kasus: Perubahan Persentase Penggunaan Transportasi Online {.unnumbered}

Mari kita analisis perubahan pola mobilitas mahasiswa ITERA dari waktu ke waktu. Berdasarkan data survei yang dilakukan pada dua periode berbeda, kita tertarik untuk mengetahui perubahan persentase penggunaan transportasi online sebagai moda transportasi utama.

**Data Survei Periode 1 (Semester Ganjil 2023):** - Total responden: 200 mahasiswa - Pengguna transportasi online: 24 mahasiswa

**Data Survei Periode 2 (Semester Ganjil 2024):** - Total responden: 429 mahasiswa\
- Pengguna transportasi online: 32 mahasiswa

Pertama, kita hitung persentase penggunaan transportasi online pada masing-masing periode:

**Periode 1:**

$$
\text{Persentase TO Periode 1} = \frac{24}{200} \times 100\% = 12,0\%
$$

**Periode 2:**

$$
\text{Persentase TO Periode 2} = \frac{32}{429} \times 100\% = 7,5\%
$$

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-3-data-percentage-change)Data Penggunaan Transportasi Online di ITERA</caption>
 <thead>
  <tr>
   <th style="text-align:center;"> Periode </th>
   <th style="text-align:center;"> Total Responden </th>
   <th style="text-align:center;"> Pengguna Transportasi Online </th>
   <th style="text-align:center;"> Persentase </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:center;"> Semester Ganjil 2023 </td>
   <td style="text-align:center;"> 200 </td>
   <td style="text-align:center;"> 24 </td>
   <td style="text-align:center;font-weight: bold;background-color: rgba(248, 244, 232, 255) !important;"> 12,0% </td>
  </tr>
  <tr>
   <td style="text-align:center;"> Semester Ganjil 2024 </td>
   <td style="text-align:center;"> 429 </td>
   <td style="text-align:center;"> 32 </td>
   <td style="text-align:center;font-weight: bold;background-color: rgba(248, 244, 232, 255) !important;"> 7,5% </td>
  </tr>
</tbody>
</table>

Sekarang kita hitung perubahan persentase menggunakan Persamaan \@ref(eq:konsep-percentage-change):

$$
\text{Perubahan Persentase} = \left(\frac{7,5 - 12,0}{12,0}\right) \times 100\% = \left(\frac{-4,5}{12,0}\right) \times 100\% = -37,5\%
$$

**Interpretasi:**

Terjadi **penurunan sebesar 37,5%** dalam penggunaan transportasi online sebagai moda transportasi utama mahasiswa ITERA dari Semester Ganjil 2023 ke Semester Ganjil 2024.

Perhatikan bahwa meskipun jumlah absolut pengguna transportasi online meningkat dari 24 menjadi 32 orang, magnitudnya justru menurun dari 12,0% menjadi 7,5%. Ini terjadi karena:

1.  Total responden meningkat signifikan (dari 200 ke 429 mahasiswa)
2.  Pertumbuhan jumlah pengguna transportasi online (8 orang) tidak sebanding dengan pertumbuhan total populasi (229 orang)

**Implikasi untuk Perencanaan:**

Penurunan 37,5% ini mengindikasikan bahwa: - Mahasiswa lebih memilih moda transportasi lain seperti sepeda motor pribadi - Kebijakan kampus tentang akses transportasi online mungkin perlu dievaluasi - Perlu investigasi lebih lanjut tentang faktor-faktor yang menyebabkan penurunan ini (biaya, ketersediaan, kenyamanan, dll.)
:::

Simak juga pembahasan kasus terkait perubahan persentase yang sempat hangat di pertengahan tahun 2025, yakni kenaikan tarif pajak pertambahan nilai (PPN) dari 11% hingga 12%.

::: rmdkasus
### Studi Kasus: Kesalahan Umum dalam Menafsirkan Kenaikan Pajak {.unnumbered}

Perhatikan pernyataan berikut yang sering kita dengar di media massa atau percakapan sehari-hari:

> "Pemerintah menaikkan tarif pajak penghasilan (PPh) dari 11% menjadi 12%. Kenaikannya hanya 1% saja, tidak terlalu signifikan."

Benarkah kenaikannya "hanya 1%"? Mari kita analisis dengan cermat menggunakan konsep perubahan persentase.

**Data:** - Tarif pajak awal ($f_1$) = 11% - Tarif pajak baru ($f_2$) = 12% - Selisih absolut = 12% - 11% = 1 poin persentase

**Analisis yang Keliru:**

Banyak orang menyimpulkan bahwa kenaikannya "hanya 1%" karena melihat selisih absolut. Namun, ini adalah **kesalahan interpretasi yang fatal**.

**Analisis yang Benar:**

Kita harusnya menghitung perubahan persentase menggunakan Persamaan \@ref(eq:konsep-percentage-change):

$$
\text{Perubahan Persentase} = \left(\frac{12 - 11}{11}\right) \times 100\% = \left(\frac{1}{11}\right) \times 100\% = 9,09\%
$$

**Sebenarnya, kenaikan pajak tersebut adalah 9,09%, bukan 1%!**

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-3-kasus-pajak)Perbandingan Interpretasi Kenaikan Pajak</caption>
 <thead>
  <tr>
   <th style="text-align:center;"> Jenis Interpretasi </th>
   <th style="text-align:center;"> Perhitungan </th>
   <th style="text-align:center;"> Makna </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:center;background-color: rgba(255, 232, 232, 255) !important;"> Selisih Absolut (KELIRU) </td>
   <td style="text-align:center;background-color: rgba(255, 232, 232, 255) !important;"> 12% - 11% = 1 poin persentase </td>
   <td style="text-align:center;background-color: rgba(255, 232, 232, 255) !important;"> Terkesan kenaikan kecil </td>
  </tr>
  <tr>
   <td style="text-align:center;background-color: rgba(232, 248, 232, 255) !important;"> Perubahan Persentase (BENAR) </td>
   <td style="text-align:center;background-color: rgba(232, 248, 232, 255) !important;"> (12% - 11%) / 11% × 100% = 9,09% </td>
   <td style="text-align:center;background-color: rgba(232, 248, 232, 255) !important;"> Kenaikan hampir 10% dari beban pajak awal </td>
  </tr>
</tbody>
</table>

**Dampak Fatal Kesalahan Interpretasi:**

Mari kita lihat dampak nyata pada ekonomi rumah tangga. Misalkan seorang pekerja dengan penghasilan Rp 10.000.000 per bulan:

**Beban Pajak Sebelum Kenaikan:**

$$
\text{Pajak lama} = 11\% \times \text{Rp 10.000.000} = \text{Rp 1.100.000}
$$

**Beban Pajak Setelah Kenaikan:**

$$
\text{Pajak baru} = 12\% \times \text{Rp 10.000.000} = \text{Rp 1.200.000}
$$

**Tambahan Beban Pajak per Bulan:**

$$
\text{Tambahan} = \text{Rp 1.200.000} - \text{Rp 1.100.000} = \text{Rp 100.000}
$$

**Tambahan Beban Pajak per Tahun:**

$$
\text{Tambahan tahunan} = \text{Rp 100.000} \times 12 = \text{Rp 1.200.000}
$$

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-3-dampak-ekonomi)Dampak Kenaikan Pajak pada Penghasilan Rp 10 Juta/Bulan</caption>
 <thead>
  <tr>
   <th style="text-align:center;"> Periode </th>
   <th style="text-align:center;"> Pajak Lama (11%) </th>
   <th style="text-align:center;"> Pajak Baru (12%) </th>
   <th style="text-align:center;"> Tambahan Beban </th>
   <th style="text-align:center;"> Perubahan % </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:center;"> Per Bulan </td>
   <td style="text-align:center;"> Rp 1.100.000 </td>
   <td style="text-align:center;"> Rp 1.200.000 </td>
   <td style="text-align:center;font-weight: bold;background-color: rgba(255, 244, 232, 255) !important;"> Rp 100.000 </td>
   <td style="text-align:center;font-weight: bold;background-color: rgba(255, 244, 232, 255) !important;"> 9,09% </td>
  </tr>
  <tr>
   <td style="text-align:center;"> Per Tahun </td>
   <td style="text-align:center;"> Rp 13.200.000 </td>
   <td style="text-align:center;"> Rp 14.400.000 </td>
   <td style="text-align:center;font-weight: bold;background-color: rgba(255, 244, 232, 255) !important;"> Rp 1.200.000 </td>
   <td style="text-align:center;font-weight: bold;background-color: rgba(255, 244, 232, 255) !important;"> 9,09% </td>
  </tr>
</tbody>
</table>

**Kesimpulan dan Implikasi:**

1.  **Kesalahan Persepsi**: Mengatakan "hanya naik 1%" membuat masyarakat meremehkan dampak kebijakan tersebut
2.  **Dampak Riil**: Kenaikan 9,09% berarti beban pajak meningkat hampir sepersepuluh dari beban awal
3.  **Akumulasi Tahunan**: Tambahan Rp 1.200.000 per tahun adalah beban yang signifikan bagi rumah tangga
4.  **Kesalahan Kebijakan Publik**: Jika pembuat kebijakan atau masyarakat salah memahami magnitud perubahan ini, bisa terjadi kesalahan dalam:
    -   Perencanaan anggaran rumah tangga
    -   Evaluasi dampak kebijakan fiskal
    -   Negosiasi upah dan tunjangan
    -   Pengambilan keputusan investasi

**Pelajaran Penting:**

Dalam analisis ekonomi dan kebijakan publik, **selalu gunakan perubahan persentase**, bukan selisih absolut, untuk memahami magnitud perubahan yang sebenarnya. Kesalahan interpretasi bisa berakibat fatal pada perencanaan ekonomi baik di tingkat individu, rumah tangga, maupun negara.
:::

## Ukuran Kecenderungan Pemusatan (*Measure Central Tendency*)

Ukuran kecenderungan pemusatan adalah ukuran yang menerangkan *bagaimana karakteristik yang mewakili kebanyakan objek yang kita kumpulkan*. Secara matematis ini disebut juga *kecenderungan pusat dari distribusi nilai objek*.

Makna yang dihasilkan dari analisis kecenderungan memusat adalah *karakteristik kebanyakan untuk kumpulan objek kita*. Karakteristik tersebut ditunjukkan oleh nilai dari teknik ukuran kencenderungan pemusatan yang dipilih. Oleh karena itu, satuan nilai kecenderungan pemusatan ini akan **sama dengan satuan variabelnya**.

Teknik-teknik analisis statistik deskriptif yang termasuk ke dalam kelompok ukuran ukuran kecenderungan pemusatan terdiri atas **rata-rata (*mean*)**, **median**, dan **modus (*mode*)**. Penggunaan setiap teknik harus **memperhatikan tingkat pengukuran variabelnya**.

### Rata-rata (*mean*)

Rata-rata menjumlahkan seluruh nilai yang ada di objek kita lalu membaginya dengan jumlah objek tersebut. Rata-rata hanya dapat dikenakan pada variabel dengan **tingkat pengukuran metrik (interval/rasio) saja** karena rumusnya melibatkan pembagian.

::: rmdnote
[Catatan]{.tajuksaya}

Terminologi (pengistilahan) "rasio" pada tingkat pengukuran variabel juga merujuk pada sifat nilai dengan tingkat pengukuran variabel ini yang selalu konstan jika dibandingkan (dirasiokan). Ini adalah sifat dari angka sebenarnya, yang juga merupakan nilai numerik.
:::

Rumus rata-rata adalah sebagai berikut.

$$
\bar{x} = \frac{\sum_{i=1}^{n} X_i}{n} = \frac{X_1 + X_2 + ... + X_n}{n}
(\#eq:konsep-mean)
$$

dengan:

-   $\bar{x}$ = Rata-rata sampel
-   $X_i$ = Nilai observasi ke-$i$
-   $n$ = Jumlah observasi
-   $\sum_{i=1}^{n} X_i$ = Jumlah seluruh nilai ($X_1 + X_2 + ... + X_n$)

Makna yang dihasilkan teknik analisis ini adalah **pusat dari distribusi nilai variabel sekumpulan objek**. Artinya, nilai rata-rata adalah nilai yang paling mewakili nilai-nilai lainnya dalam distribusi tersebut. Atau dengan kata lain, nilai yang menyatakan "kebanyakan" nilai suatu variabel dalam distribusi tersebut.

### Median

Median sering disebut juga sebagai "nilai tengah" suatu variabel karena nilai median adalah nilai yang menjadi pembagi kumpulan objek kita menjadi dua kumpulan dengan jumlah yang sama (50%-50%).

Cara menghitung nilai median adalah dengan mengurutkan nilai variabel dari objek-objek yang dianalisis dari yang terkecil hingga yang terbesar, kemudian:

-   jika jumlah objek ganjil, maka median adalah nilai yang berada tepat di tengah, yakni objek ke $\frac{n+1}{2}$
-   jika jumlah objek genap, maka median adalah rata-rata dari dua nilai yang berada di tengah, yakni objek ke $\frac{n}{2}$ dan $\frac{n}{2}+1$

Median digunakan pada data yang berurutan, dengan demikian tingkat pengukuran *paling rendah* yang bisa menggunakan adalah **ordinal**. Variabel dengan tingkat pengukuran nominal tidak bisa menggunakan median karena tidak memiliki urutan.

Makna yang dihasilkan teknik analisis ini sama saja dengan *mean*, yakni **pusat dari distribusi nilai variabel sekumpulan objek**. Akan tetapi, median sering disandingkan dengan *mean* karena tidak seperti *mean*, median tidak terpengaruh oleh nilai ekstrem (*outlier*).

::: rmdkasus
### Studi Kasus: Mean dan Median pada Data dengan Pencilan {.unnumbered}

Perhatikan data biaya perjalanan sepekan (ribu rupiah) dari 8 mahasiswa ITERA:

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-3-data-biaya-awal)Biaya Perjalanan Sepekan (Ribu Rupiah)</caption>
 <thead>
  <tr>
   <th style="text-align:center;"> Mahasiswa </th>
   <th style="text-align:center;"> Biaya (Rp) </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:center;"> Mhs 1 </td>
   <td style="text-align:center;"> 50 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> Mhs 2 </td>
   <td style="text-align:center;"> 55 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> Mhs 3 </td>
   <td style="text-align:center;"> 60 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> Mhs 4 </td>
   <td style="text-align:center;"> 65 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> Mhs 5 </td>
   <td style="text-align:center;"> 70 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> Mhs 6 </td>
   <td style="text-align:center;"> 75 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> Mhs 7 </td>
   <td style="text-align:center;"> 80 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> Mhs 8 </td>
   <td style="text-align:center;"> 85 </td>
  </tr>
</tbody>
</table>

**Perhitungan Mean:**

$$
\bar{x} = \frac{50 + 55 + 60 + 65 + 70 + 75 + 80 + 85}{8} = \frac{540}{8} = 67,5
$$

**Perhitungan Median:**

Data sudah terurut, $n=8$ (genap), maka median adalah rata-rata nilai ke-4 dan ke-5:

$$
\text{Median} = \frac{65 + 70}{2} = 67,5
$$

Sekarang misalkan Mhs 8 memiliki biaya ekstrem Rp 500.000 (menggunakan layanan *premium*):

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-3-data-biaya-outlier)Biaya Perjalanan dengan Pencilan</caption>
 <thead>
  <tr>
   <th style="text-align:center;"> Mahasiswa </th>
   <th style="text-align:center;"> Biaya (Rp) </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:center;"> Mhs 1 </td>
   <td style="text-align:center;"> 50 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> Mhs 2 </td>
   <td style="text-align:center;"> 55 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> Mhs 3 </td>
   <td style="text-align:center;"> 60 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> Mhs 4 </td>
   <td style="text-align:center;"> 65 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> Mhs 5 </td>
   <td style="text-align:center;"> 70 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> Mhs 6 </td>
   <td style="text-align:center;"> 75 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> Mhs 7 </td>
   <td style="text-align:center;"> 80 </td>
  </tr>
  <tr>
   <td style="text-align:center;font-weight: bold;background-color: rgba(255, 232, 232, 255) !important;"> Mhs 8 </td>
   <td style="text-align:center;font-weight: bold;background-color: rgba(255, 232, 232, 255) !important;"> 500 </td>
  </tr>
</tbody>
</table>

**Perhitungan Mean Baru:**

$$
\bar{x} = \frac{50 + 55 + 60 + 65 + 70 + 75 + 80 + 500}{8} = \frac{955}{8} = 119,4
$$

**Perhitungan Median Baru:**

$$
\text{Median} = \frac{65 + 70}{2} = 67,5
$$

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-3-perbandingan-mean-median)Perbandingan Mean dan Median</caption>
 <thead>
  <tr>
   <th style="text-align:center;"> Kondisi </th>
   <th style="text-align:center;"> Mean </th>
   <th style="text-align:center;"> Median </th>
   <th style="text-align:center;"> Δ Mean </th>
   <th style="text-align:center;"> Δ Median </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:center;"> Tanpa Pencilan </td>
   <td style="text-align:center;"> 67,5 </td>
   <td style="text-align:center;font-weight: bold;background-color: rgba(232, 248, 232, 255) !important;"> 67,5 </td>
   <td style="text-align:center;"> — </td>
   <td style="text-align:center;font-weight: bold;background-color: rgba(232, 248, 232, 255) !important;"> — </td>
  </tr>
  <tr>
   <td style="text-align:center;"> Dengan Pencilan </td>
   <td style="text-align:center;"> 119,4 </td>
   <td style="text-align:center;font-weight: bold;background-color: rgba(232, 248, 232, 255) !important;"> 67,5 </td>
   <td style="text-align:center;"> +51,9 </td>
   <td style="text-align:center;font-weight: bold;background-color: rgba(232, 248, 232, 255) !important;"> 0 </td>
  </tr>
</tbody>
</table>

**Interpretasi:**

Mean terpengaruh drastis oleh pencilan (naik 77%), sedangkan median tetap 67,5. Median lebih representatif untuk data dengan pencilan karena menunjukkan nilai tengah mayoritas mahasiswa. Ini penting dalam perencanaan: jika menggunakan mean (Rp 119.400), estimasi subsidi transportasi akan terlalu tinggi dan tidak mencerminkan kebutuhan kebanyakan mahasiswa.
:::

### Modus

Modus adalah nilai suatu variabel yang sering muncul dalam set data. Cara perhitungannya tidak rumit sama sekali, kita hanya cukup membuat tabel frekuensi dari data yang kita miliki, kemudian mencari nilai dengan frekuensi terbesar (yang paling sering muncul). Nilai itulah modusnya.

Makna dari analisis modus adalah nilai yang menjadi tren atau paling umum dalam suatu distribusi data.

Modus biasanya digunakan pada **data kategoris**, seperti variabel nominal dan ordinal. Untuk variabel metrik, modus agak sulit dilakukan karena nilai yang sama persis sangat jarang muncul. Kecuali sifat nilainya **diskret**, seperti usia atau jumlah perjalanan.

Modus dapat berjumlah lebih dari satu dalam sebuah set data. Set data dengan satu modus disebut **unimodal**, set data dengan dua modus disebut **bimodal**, dan set data dengan lebih dari dua modus disebut **multimodal**.

::: rmdkasus
### Studi Kasus: Analisis Modus {.unnumbered}

Modus sangat berguna untuk mengidentifikasi nilai yang paling umum dalam data kategoris maupun numerik diskret. Mari kita gunakan data pola mobilitas mahasiswa ITERA untuk menganalisis modus pada dua tipe variabel berbeda.

**Variabel 1: Jenis Kendaraan (`kend`) - Kategoris Nominal**

Dari dataset 8 mahasiswa yang telah digunakan sebelumnya, kita dapat membuat tabel frekuensi untuk variabel `kend`:

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-3-modus-kend)Distribusi Frekuensi Jenis Kendaraan</caption>
 <thead>
  <tr>
   <th style="text-align:center;"> Kode </th>
   <th style="text-align:center;"> Jenis Kendaraan </th>
   <th style="text-align:center;"> Frekuensi </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:center;font-weight: bold;background-color: rgba(232, 244, 248, 255) !important;"> 1 </td>
   <td style="text-align:center;font-weight: bold;background-color: rgba(232, 244, 248, 255) !important;"> Sepeda motor pribadi </td>
   <td style="text-align:center;font-weight: bold;background-color: rgba(232, 244, 248, 255) !important;"> 4 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 3 </td>
   <td style="text-align:center;"> Layanan online </td>
   <td style="text-align:center;"> 2 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 5 </td>
   <td style="text-align:center;"> Sepeda </td>
   <td style="text-align:center;"> 2 </td>
  </tr>
</tbody>
</table>

**Hasil:**

Modus untuk variabel `kend` adalah **sepeda motor pribadi** (kode 1) dengan frekuensi 4. Artinya, jenis kendaraan yang paling umum digunakan mahasiswa adalah sepeda motor pribadi.

**Variabel 2: Frekuensi Perjalanan Senin (`perjalanan_senin`) - Numerik Diskret**

Variabel ini menunjukkan berapa kali mahasiswa melakukan perjalanan di hari Senin. Mari kita buat tabel frekuensinya:

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-3-modus-perjalanan)Distribusi Frekuensi Perjalanan di Hari Senin</caption>
 <thead>
  <tr>
   <th style="text-align:center;"> Jumlah Perjalanan </th>
   <th style="text-align:center;"> Frekuensi </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:center;font-weight: bold;background-color: rgba(255, 244, 232, 255) !important;"> 2 </td>
   <td style="text-align:center;font-weight: bold;background-color: rgba(255, 244, 232, 255) !important;"> 3 </td>
  </tr>
  <tr>
   <td style="text-align:center;font-weight: bold;background-color: rgba(255, 244, 232, 255) !important;"> 3 </td>
   <td style="text-align:center;font-weight: bold;background-color: rgba(255, 244, 232, 255) !important;"> 3 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 4 </td>
   <td style="text-align:center;"> 2 </td>
  </tr>
</tbody>
</table>

**Hasil:**

Data ini **bimodal** karena terdapat dua nilai yang sama-sama memiliki frekuensi tertinggi (3): mahasiswa yang melakukan **2 kali perjalanan** dan **3 kali perjalanan**. Artinya, pola yang paling umum adalah mahasiswa melakukan 2-3 kali perjalanan per hari Senin.

**Interpretasi untuk Perencanaan:**

1.  **Jenis Kendaraan**: Dominasi sepeda motor pribadi (modus) mengindikasikan perlunya penyediaan area parkir motor yang memadai
2.  **Frekuensi Perjalanan**: Pola bimodal 2-3 kali perjalanan menunjukkan bahwa kebanyakan mahasiswa melakukan perjalanan pulang-pergi ditambah satu perjalanan tambahan (ke kantin, perpustakaan, dll). Informasi ini berguna untuk merencanakan jadwal layanan transportasi kampus pada jam-jam tertentu
:::

## Ukuran Penyebaran (*Measure of Dispersion*)

Lain halnya dengan ukuran pemusatan, ukuran penyebaran memberikan informasi tentang **keberagaman nilai** suatu kumpulan objek. Dua set data dapat memiliki ukuran pemusatan yang sama, naman belum tentu variasi atau keberagamannya juga sama. Oleh karena itu kita perlu menyajikan ukuran penyebaran di samping ukuran pemusatannya.

Seperti halnya ukuran kecenderungan memusat, ukuran penyebaran juga dapat digunakan pada seluruh tingkat pengukuran. Tentu saja, untuk setiap tingkat pengukuran terdapat teknik yang berbeda. Teknik-teknik analisis deskriptif yang termasuk ke dalam ukuran penyebaran di antaranya adalah indeks variasi kualitatif (*index of qualitative variance*, IQV), rentang (*range*), variansi (*variance*), dan simpangan baku (*standard deviation*).

### Indeks Variasi Kualitatif (*Index of Qualitative Variance*, IQV)

IQV adalah satu-satunya ukuran penyebaran yang dapat digunakan untuk variabel nominal [@healey2021statistics]. Meskipun demikian, IQV juga dapat digunakan pada variabel dengan tingkat pengukuran apa pun selama sudah dikelompokkan ke dalam distribusi frekuensi.

IQV pada dasarnya adalah rasio antara jumlah variasi yang benar-benar teramati dalam distribusi data dengan variasi maksimum yang mungkin ada dalam distribusi tersebut. Makna dari nilai IQV adalah sebagai berikut:

-   IQV = 0,00: Tidak ada variasi dalam distribusi data sama sekali, semua objek benar-benar seragam
-   IQV = 1,00: Variasi maksimum dalam distribusi data, semua objek benar-benar berbeda satu sama lain

Perhitungan IQV dilakukan dengan rumus:

$$
\begin{equation}
\text{IQV} = \frac{k(1 - \sum p_i^2)}{k - 1}
(\#eq:konsep-iqv)
\end{equation}
$$

dengan:

-   $k$ = Jumlah kategori
-   $p_i$ = Proporsi pada kategori ke-$i$

::: rmdkasus
### Studi Kasus: Keberagaman Distribusi Mahasiswa Antar Fakultas {.unnumbered}

Indeks Variasi Kualitatif (IQV) sangat berguna untuk mengukur tingkat keberagaman distribusi data kategoris. Mari kita gunakan data distribusi mahasiswa UIN Raden Intan Lampung berdasarkan fakultas untuk menghitung IQV.

Dari set data hasil penyebaran kuesioner yang berisi 400 mahasiswa, kita dapat membuat tabel distribusi frekuensi untuk variabel `Fakultas`:

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-3-data-iqv-fakultas)Distribusi Mahasiswa UIN Raden Intan Lampung Berdasarkan Fakultas</caption>
 <thead>
  <tr>
   <th style="text-align:center;"> Fakultas </th>
   <th style="text-align:center;"> Frekuensi </th>
   <th style="text-align:center;"> Proporsi </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:center;"> Ekonomi dan Bisnis Islam </td>
   <td style="text-align:center;"> 44 </td>
   <td style="text-align:center;"> 0.110 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> Syariah </td>
   <td style="text-align:center;"> 118 </td>
   <td style="text-align:center;"> 0.295 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> Ushuluddin dan Studi Agama </td>
   <td style="text-align:center;"> 58 </td>
   <td style="text-align:center;"> 0.145 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> Dakwah dan Ilmu Komunikasi </td>
   <td style="text-align:center;"> 130 </td>
   <td style="text-align:center;"> 0.325 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> Tarbiyah dan Keguruan </td>
   <td style="text-align:center;"> 15 </td>
   <td style="text-align:center;"> 0.038 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> Sains dan Teknologi </td>
   <td style="text-align:center;"> 20 </td>
   <td style="text-align:center;"> 0.050 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> Ilmu Sosial dan Ilmu Politik </td>
   <td style="text-align:center;"> 10 </td>
   <td style="text-align:center;"> 0.025 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> Adab </td>
   <td style="text-align:center;"> 5 </td>
   <td style="text-align:center;"> 0.013 </td>
  </tr>
</tbody>
</table>

Kita mengaplikasikan Persamaan \@ref(eq:konsep-iqv) dengan langkah-langkah seperti berikut. Simak dan bila perlu tulis ulang langkah-langkahnya oleh Anda.

**Langkah 1: Hitung** $\sum p_i^2$

$$
\begin{aligned}
\sum p_i^2 &= (0,110)^2 + (0,295)^2 + (0,145)^2 + (0,325)^2 + (0,038)^2 \\
           &\quad + (0,050)^2 + (0,025)^2 + (0,013)^2 \\
           &= 0,012 + 0,087 + 0,021 + 0,106 + 0,001 + 0,003 + 0,001 + 0,000 \\
           &= 0,231
\end{aligned}
$$

**Langkah 2: Hitung IQV**

Dengan $k = 8$ (jumlah fakultas):

$$
IQV = \frac{8(1 - 0,231)}{8 - 1} = \frac{8 \times 0,769}{7} = \frac{6,152}{7} = 0,879
$$

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-3-hasil-iqv)Hasil Perhitungan IQV</caption>
 <thead>
  <tr>
   <th style="text-align:center;"> Komponen </th>
   <th style="text-align:center;"> Nilai </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:center;"> Jumlah kategori (k) </td>
   <td style="text-align:center;"> 8 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> Σpᵢ² </td>
   <td style="text-align:center;"> 0,231 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 1 - Σpᵢ² </td>
   <td style="text-align:center;"> 0,769 </td>
  </tr>
  <tr>
   <td style="text-align:center;font-weight: bold;background-color: rgba(232, 244, 248, 255) !important;"> IQV </td>
   <td style="text-align:center;font-weight: bold;background-color: rgba(232, 244, 248, 255) !important;"> 0,879 </td>
  </tr>
</tbody>
</table>

**Interpretasi:**

Nilai IQV = 0,879 menunjukkan tingkat keberagaman yang tinggi dalam distribusi mahasiswa antar fakultas. Nilai ini mendekati 1,00, yang berarti distribusi mahasiswa cukup merata di berbagai fakultas (tidak terlalu terkonsentrasi di satu fakultas saja).

Meskipun ada fakultas dengan jumlah mahasiswa yang lebih banyak seperti Dakwah dan Ilmu Komunikasi (32,5%) dan Syariah (29,5%), distribusi secara keseluruhan masih menunjukkan variasi yang baik. Jika semua mahasiswa hanya berada di satu fakultas, maka IQV = 0,00 (tidak ada variasi sama sekali).
:::

### Rentang (*Range*)

Rentang adalah selisih antara nilai tertinggi (maksimum) dan nilai terendah (minimum) dalam suatu distribusi data. Karena itu, rentang hanya dapat digunakan pada variabel interval dan rasio.

Makna dari perhitungan rentang tidak banyak memberikan informasi terkait keberagaman data jika hanya dikenakan pada satu set data saja. Apabila dibandingkan, maka set data yang rentangnya lebih besar dapat dikatakan lebih beragam.

::: rmdkasus
### Studi Kasus: Perbandingan Rentang Biaya Perjalanan Mahasiswa {.unnumbered}

Rentang dapat digunakan untuk membandingkan tingkat keberagaman data antar kelompok alih-alih untuk menjelaskan satu set data saja. Mari kita bandingkan keberagaman biaya perjalanan sepekan mahasiswa dari dua perguruan tinggi: UIN RIL dan UNILA.

Berdasarkan data survei pola mobilitas mahasiswa, kita akan menganalisis variabel `biaya_perjalanan` (biaya perjalanan sepekan dalam rupiah). Perhatikan statistik deskriptif dari kedua kelompok:

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-3-data-rentang)Perbandingan Rentang Biaya Perjalanan Sepekan Mahasiswa UIN RIL dan UNILA</caption>
 <thead>
  <tr>
   <th style="text-align:center;"> Kampus </th>
   <th style="text-align:center;"> Minimum (Rp) </th>
   <th style="text-align:center;"> Maksimum (Rp) </th>
   <th style="text-align:center;"> Rentang (Rp) </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:center;"> UIN RIL </td>
   <td style="text-align:center;"> 0 </td>
   <td style="text-align:center;"> 150 </td>
   <td style="text-align:center;font-weight: bold;background-color: rgba(232, 244, 248, 255) !important;"> 150 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> UNILA </td>
   <td style="text-align:center;"> 0 </td>
   <td style="text-align:center;"> 400 </td>
   <td style="text-align:center;font-weight: bold;background-color: rgba(232, 244, 248, 255) !important;"> 400 </td>
  </tr>
</tbody>
</table>

**Perhitungan Rentang untuk UIN RIL:**

$$
\begin{align}
\text{Rentang}_{\text{UIN RIL}} &= \text{Maks} - \text{Min}\\
&= 150 - 0\\
&= 150
\end{align}
$$

**Perhitungan Rentang untuk UNILA:**

$$
\begin{align}
\text{Rentang}_{\text{UNILA}} &= \text{Maks} - \text{Min}\\
&=400 - 0\\
&=400
\end{align}
$$

Nilai spesifik untuk minimum, maksimum, dan rentang dapat dilihat pada tabel di atas.

**Interpretasi:**

Hasil perhitungan menunjukkan bahwa terdapat variasi yang cukup besar dalam biaya perjalanan sepekan mahasiswa di kedua kampus. Perbandingan rentang biaya perjalanan memberikan informasi penting tentang keberagaman kondisi ekonomi dan pola mobilitas mahasiswa:

1. **Rentang yang Berbeda**: Perbedaan rentang biaya perjalanan antara UIN RIL dan UNILA menunjukkan tingkat keberagaman ekonomi dan pola mobilitas yang berbeda di kedua kampus

2. **Variasi Biaya**: Mahasiswa di kedua kampus memiliki spektrum biaya perjalanan yang luas, dari yang sangat rendah (kemungkinan berjalan kaki atau bersepeda) hingga yang cukup tinggi (menggunakan kendaraan bermotor atau transportasi online)

3. **Implikasi Ekonomi**: Keberagaman biaya perjalanan mencerminkan perbedaan kondisi ekonomi mahasiswa dan pilihan moda transportasi yang tersedia

:::

### Kuartil, Desil, dan Persentil

Kuartil, desil, dan persentil adalah ukuran penyebaran yang digunakan untuk membagi data menjadi beberapa bagian yang sama besar. Kuartil membagi data menjadi **empat** bagian yang sama besar, desil membagi data menjadi **sepuluh** bagian yang sama besar, dan persentil membagi data menjadi **seratus** bagian yang sama besar.

Terdapat tiga jenis kuartil, yaitu kuartil bawah ($Q_1$), kuartil tengah ($Q_2$), dan kuartil atas ($Q_3$).

<div class="figure" style="text-align: center">
<img src="images/bab-3-kuartil.png" alt="Ilustrasi Kuartil" width="647" />
<p class="caption">(\#fig:fig-ilustrasi-kuartil)Ilustrasi Kuartil</p>
</div>

::: rmdkasus
### Studi Kasus: Analisis Posisi Data dengan Kuartil {.unnumbered}

Kuartil membagi distribusi data menjadi empat bagian yang sama. Ini sangat berguna untuk memahami posisi suatu nilai dalam keseluruhan data. Mari kita gunakan kembali data biaya perjalanan mahasiswa UNILA.

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-3-kuartil-unila)Nilai Kuartil Biaya Perjalanan Mahasiswa UNILA (n = 393)</caption>
 <thead>
  <tr>
   <th style="text-align:left;">   </th>
   <th style="text-align:center;"> Statistik </th>
   <th style="text-align:center;"> Posisi Data </th>
   <th style="text-align:center;"> Nilai (Ribu Rp) </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> 25% </td>
   <td style="text-align:center;"> Kuartil Bawah (Q1) </td>
   <td style="text-align:center;font-weight: bold;background-color: rgba(232, 244, 248, 255) !important;"> Membatasi 25% data terbawah </td>
   <td style="text-align:center;"> 35 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> 50% </td>
   <td style="text-align:center;"> Kuartil Tengah (Q2/Median) </td>
   <td style="text-align:center;font-weight: bold;background-color: rgba(232, 244, 248, 255) !important;"> Membatasi 50% data terbawah </td>
   <td style="text-align:center;"> 50 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> 75% </td>
   <td style="text-align:center;"> Kuartil Atas (Q3) </td>
   <td style="text-align:center;font-weight: bold;background-color: rgba(232, 244, 248, 255) !important;"> Membatasi 75% data terbawah </td>
   <td style="text-align:center;"> 100 </td>
  </tr>
</tbody>
</table>

**Cara Menentukan Kuartil:**

1.  **Kuartil Bawah ($Q_1$):**
    *   Urutkan data dari terkecil hingga terbesar.
    *   Cari nilai pada posisi $\frac{1(n+1)}{4}$.
    *   Nilai ini memisahkan 25% data terendah dari sisa 75% data lainnya.

2.  **Kuartil Atas ($Q_3$):**
    *   Data diurutkan dari terkecil hingga terbesar.
    *   Cari nilai pada posisi $\frac{3(n+1)}{4}$.
    *   Nilai ini memisahkan 75% data terendah dari 25% data tertinggi.

**Interpretasi:**

Dari total **393** mahasiswa yang diamati, kita dapat menafsirkan posisi data sebagai berikut:

1.  **Kuartil Bawah ($Q_1$):** Sebesar 25% dari populasi (sekitar **98** mahasiswa) memiliki biaya perjalanan sepekan kurang dari atau sama dengan nilai $Q_1$. Ini menandakan kelompok dengan biaya transportasi paling efisien.
2.  **Kuartil Tengah ($Q_2$):** Sebesar 50% (sekitar **196** mahasiswa) memiliki biaya perjalanan kurang dari atau sama dengan median. Ini adalah titik tengah distribusi.
3.  **Kuartil Atas ($Q_3$):** Sebesar 75% (sekitar **295** mahasiswa) memiliki biaya perjalanan di bawah nilai $Q_3$. Artinya, hanya 25% sisanya (sekitar **98** mahasiswa) yang menghabiskan biaya perjalanan di atas nilai tersebut (kelompok dengan biaya tinggi).

Pemahaman ini penting untuk melihat sebaran beban biaya di kalangan mahasiswa, apakah terkonsentrasi di nilai rendah atau tinggi.
:::

Makna dari hasil perhitungan kuartil adalah nilai-nilai yang menjadi kuartil bawah, kuartil tengah, dan kuartil atas adalah nilai-nilai yang menjadi pembatas jumlah observasi sebanyak masing-masing 25% ketika setelah diurutkan dari kecil ke besar. Dengan begitu pula, maka kuartil **tidak dapat** dikenakan pada variabel dengan **tingkat pengukuran nominal**.

### Variansi (*Variance*) dan Simpangan Baku (*Standard Deviation*)

Variansi dan simpangan baku adalah ukuran penyebaran yang paling memberikan banyak informasi tentang variasi nilai suatu variabel dari sekumpulan objek. Variansi dan simpangan baku dapat dikatakan **ukuran seberapa dekat nilai tiap-tiap objek dengan nilai rata-ratanya.** Ini adalah makna dari variansi dan simpangan baku. Dengan kata lain, ukuran ini adalah rata-rata jarak nilai setiap objek dengan nilai rata-rata seluruh objek tersebut.

Variansi dihitung dengan rumus yang ditampilkan pada Persamaan \@ref(eq:konsep-variansi). Satuan dari nilai variansi sama dengan satuan variabel yang dianalisisnya, tetapi karena dikuadratkan, maka satuannya juga ikut dikuadratkan.

$$
\begin{equation}
\text{Variansi} = \frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n}
\end{equation}
(\#eq:konsep-variansi)
$$

Karena nilai variansi dihasilkan dari kuadrat selisih nilai objek dengan rata-rata, maka satuannya juga ikut dikuadratkan. Ini membuat penafsiran menjadi aneh. Untuk menormalkannya, ditariklah akar kuadrat dari variansi itu yang dinamakan **simpangan baku** (*standard deviation*).

$$
\begin{align}
\text{Simpangan Baku} &= \sqrt{\text{Variansi}}\\
&=\sqrt{\frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n}} (\#eq:konsep-simpangan-baku)
\end{align}
$$ 

Nilai variansi dan simpangan baku yang kecil menunjukkan bahwa nilai tiap-tiap objek cenderung berdekatan dengan nilai rata-ratanya. Sebaliknya, nilai variansi dan simpangan baku yang besar menunjukkan bahwa nilai tiap-tiap objek cenderung berjauhan dengan nilai rata-ratanya.

::: rmdkasus
### Studi Kasus: Menghitung Variansi dan Simpangan Baku Biaya Perjalanan {.unnumbered}

Mari kita hitung variansi dan simpangan baku dari sampel kecil biaya perjalanan sepekan (dalam ribu rupiah) dari 5 mahasiswa. Ini akan membantu kita memahami bagaimana ukuran penyebaran dihitung langkah demi langkah.

Data biaya perjalanan (`X`): 50, 60, 55, 70, 65.

**Langkah 1: Hitung Rata-rata ($\bar{x}$)**

$$
\bar{x} = \frac{50 + 60 + 55 + 70 + 65}{5} = \frac{300}{5} = 60
$$

**Langkah 2: Buat Tabel Perhitungan $(x_i - \bar{x})^2$**

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-3-simulasi-variansi)Perhitungan Selisih Kuadrat</caption>
 <thead>
<tr>
<th style="empty-cells: hide;border-bottom:hidden;" colspan="1"></th>
<th style="border-bottom:hidden;padding-bottom:0; padding-left:3px;padding-right:3px;text-align: center; " colspan="1"><div style="border-bottom: 1px solid #ddd; padding-bottom: 5px; ">Data Asli</div></th>
<th style="border-bottom:hidden;padding-bottom:0; padding-left:3px;padding-right:3px;text-align: center; " colspan="1"><div style="border-bottom: 1px solid #ddd; padding-bottom: 5px; ">Pusat</div></th>
<th style="border-bottom:hidden;padding-bottom:0; padding-left:3px;padding-right:3px;text-align: center; " colspan="2"><div style="border-bottom: 1px solid #ddd; padding-bottom: 5px; ">Deviasi</div></th>
</tr>
  <tr>
   <th style="text-align:center;"> Mahasiswa </th>
   <th style="text-align:center;"> Biaya (X) </th>
   <th style="text-align:center;"> Rata-rata (x̄) </th>
   <th style="text-align:center;"> Selisih (X - x̄) </th>
   <th style="text-align:center;"> Kuadrat (X - x̄)² </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:center;"> A </td>
   <td style="text-align:center;"> 50 </td>
   <td style="text-align:center;"> 60 </td>
   <td style="text-align:center;"> -10 </td>
   <td style="text-align:center;"> 100 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> B </td>
   <td style="text-align:center;"> 60 </td>
   <td style="text-align:center;"> 60 </td>
   <td style="text-align:center;"> 0 </td>
   <td style="text-align:center;"> 0 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> C </td>
   <td style="text-align:center;"> 55 </td>
   <td style="text-align:center;"> 60 </td>
   <td style="text-align:center;"> -5 </td>
   <td style="text-align:center;"> 25 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> D </td>
   <td style="text-align:center;"> 70 </td>
   <td style="text-align:center;"> 60 </td>
   <td style="text-align:center;"> 10 </td>
   <td style="text-align:center;"> 100 </td>
  </tr>
  <tr>
   <td style="text-align:center;border-bottom: 2px solid #000"> E </td>
   <td style="text-align:center;border-bottom: 2px solid #000"> 65 </td>
   <td style="text-align:center;border-bottom: 2px solid #000"> 60 </td>
   <td style="text-align:center;border-bottom: 2px solid #000"> 5 </td>
   <td style="text-align:center;border-bottom: 2px solid #000"> 25 </td>
  </tr>
</tbody>
</table>

**Langkah 3: Hitung Jumlah Kuadrat Selisih**

$$
\sum_{i=1}^{n}(x_i - \bar{x})^2 = 100 + 0 + 25 + 100 + 25 = 250
$$

**Langkah 4: Hitung Variansi dan Simpangan Baku**

Sesuai Persamaan \@ref(eq:konsep-variansi), kita bagi jumlah tersebut dengan $n = 5$:

$$
\text{Variansi} = \frac{250}{5} = 50
$$

Simpangan baku adalah akar kuadrat dari variansi:

$$
\text{Simpangan Baku} = \sqrt{50} \approx 7,07
$$

**Interpretasi:**

Simpangan baku sebesar 7,07 (ribu rupiah) menunjukkan rata-rata penyimpangan biaya perjalanan setiap mahasiswa dari biaya rata-rata kelompoknya.

-   Semakin **kecil** simpangan baku, semakin seragam biaya perjalanan mahasiswa (data mengumpul di sekitar rata-rata).
-   Semakin **besar** simpangan baku, semakin bervariasi biaya perjalanan mahasiswa (data menyebar jauh dari rata-rata).

Dalam bidang PWK, wilayah dengan simpangan baku pendapatan atau pengeluaran yang tinggi menunjukkan ketimpangan yang tinggi, yang mungkin memerlukan intervensi kebijakan yang berbeda dibandingkan wilayah yang cenderung homogen.
:::




### Rangkuman Teknik Analisis Statistik Deskriptif

Pemilihan teknik analisis statistik deskriptif sangat bergantung pada tujuan analisis (apakah melihat pemusatan atau penyebaran) dan tingkat pengukuran variabel yang tersedia. Tabel \@ref(tab:rangkuman-deskriptif) merangkum berbagai teknik yang telah dipelajari beserta syarat penggunaannya.

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:rangkuman-deskriptif)Rangkuman Teknik Analisis Statistik Deskriptif</caption>
 <thead>
  <tr>
   <th style="text-align:center;"> No </th>
   <th style="text-align:left;"> Nama Analisis </th>
   <th style="text-align:left;"> Tingkat Pengukuran </th>
   <th style="text-align:left;"> Makna Singkat Hasil </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:center;font-weight: bold;"> 1 </td>
   <td style="text-align:left;"> Frekuensi &amp; Persentase </td>
   <td style="text-align:left;"> Nominal, Ordinal </td>
   <td style="text-align:left;"> Jumlah atau proporsi kemunculan suatu nilai dalam distribusi </td>
  </tr>
  <tr>
   <td style="text-align:center;font-weight: bold;"> 2 </td>
   <td style="text-align:left;"> Rasio </td>
   <td style="text-align:left;"> Nominal, Ordinal </td>
   <td style="text-align:left;"> Perbandingan relatif jumlah satu kategori terhadap kategori lain </td>
  </tr>
  <tr>
   <td style="text-align:center;font-weight: bold;"> 3 </td>
   <td style="text-align:left;"> Laju (*Rate*) </td>
   <td style="text-align:left;"> Metrik (jumlah kejadian) </td>
   <td style="text-align:left;"> Intensitas kejadian relatif terhadap populasi berisiko atau waktu </td>
  </tr>
  <tr>
   <td style="text-align:center;font-weight: bold;"> 4 </td>
   <td style="text-align:left;"> Modus </td>
   <td style="text-align:left;"> Nominal, Ordinal, Metrik </td>
   <td style="text-align:left;"> Nilai yang paling sering muncul (tren) </td>
  </tr>
  <tr>
   <td style="text-align:center;font-weight: bold;"> 5 </td>
   <td style="text-align:left;"> Median </td>
   <td style="text-align:left;"> Ordinal, Metrik </td>
   <td style="text-align:left;"> Nilai tengah yang membagi data menjadi dua bagian sama besar </td>
  </tr>
  <tr>
   <td style="text-align:center;font-weight: bold;"> 6 </td>
   <td style="text-align:left;"> Rata-rata (*Mean*) </td>
   <td style="text-align:left;"> Metrik </td>
   <td style="text-align:left;"> Pusat aritmatika yang mewakili keseluruhan nilai </td>
  </tr>
  <tr>
   <td style="text-align:center;font-weight: bold;"> 7 </td>
   <td style="text-align:left;"> IQV </td>
   <td style="text-align:left;"> Nominal, Ordinal </td>
   <td style="text-align:left;"> Derajat keberagaman (heterogenitas) data kualitatif </td>
  </tr>
  <tr>
   <td style="text-align:center;font-weight: bold;"> 8 </td>
   <td style="text-align:left;"> Rentang (*Range*) </td>
   <td style="text-align:left;"> Metrik </td>
   <td style="text-align:left;"> Selisih total antara nilai tertinggi dan terendah </td>
  </tr>
  <tr>
   <td style="text-align:center;font-weight: bold;"> 9 </td>
   <td style="text-align:left;"> Kuartil/Persentil </td>
   <td style="text-align:left;"> Ordinal, Metrik </td>
   <td style="text-align:left;"> Posisi nilai yang membagi data terurut menjadi bagian-bagian proporsional </td>
  </tr>
  <tr>
   <td style="text-align:center;font-weight: bold;"> 10 </td>
   <td style="text-align:left;"> Variansi &amp; Simpangan Baku </td>
   <td style="text-align:left;"> Metrik </td>
   <td style="text-align:left;"> Rata-rata jarak penyimpangan setiap data terhadap nilai rata-ratanya </td>
  </tr>
</tbody>
</table>

Kerjakanlah soal-soal evaluasi berikut untuk menguji pemahaman Anda terhadap analisis statistik deskriptif.

::: rmdexercise
## Soal Evaluasi 4 {.unnumbered}

Perhatikan cuplikan set data hasil pengumpulan kuesioner yang terdiri atas 6 responden berikut.

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-3-eval-4-preview)Cuplikan data survei mahasiswa</caption>
 <thead>
  <tr>
   <th style="text-align:center;"> KodeResp </th>
   <th style="text-align:center;"> Usia </th>
   <th style="text-align:center;"> Fakultas </th>
   <th style="text-align:center;"> ThnMsk </th>
   <th style="text-align:center;"> UangSaku </th>
   <th style="text-align:center;"> Jarak </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:center;"> 001 </td>
   <td style="text-align:center;"> 22 </td>
   <td style="text-align:center;"> 1 </td>
   <td style="text-align:center;"> 2020 </td>
   <td style="text-align:center;"> 2 </td>
   <td style="text-align:center;"> 19.27 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 002 </td>
   <td style="text-align:center;"> 25 </td>
   <td style="text-align:center;"> 1 </td>
   <td style="text-align:center;"> 2020 </td>
   <td style="text-align:center;"> 1 </td>
   <td style="text-align:center;"> 0.58 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 003 </td>
   <td style="text-align:center;"> 24 </td>
   <td style="text-align:center;"> 2 </td>
   <td style="text-align:center;"> 2021 </td>
   <td style="text-align:center;"> 1 </td>
   <td style="text-align:center;"> 0.56 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 004 </td>
   <td style="text-align:center;"> 19 </td>
   <td style="text-align:center;"> 3 </td>
   <td style="text-align:center;"> 2022 </td>
   <td style="text-align:center;"> 1 </td>
   <td style="text-align:center;"> 1.05 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 005 </td>
   <td style="text-align:center;"> 23 </td>
   <td style="text-align:center;"> 2 </td>
   <td style="text-align:center;"> 2021 </td>
   <td style="text-align:center;"> 1 </td>
   <td style="text-align:center;"> 1.69 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 006 </td>
   <td style="text-align:center;"> 20 </td>
   <td style="text-align:center;"> 1 </td>
   <td style="text-align:center;"> 2020 </td>
   <td style="text-align:center;"> 3 </td>
   <td style="text-align:center;"> 1.37 </td>
  </tr>
</tbody>
</table>

Adapun keterangan dari variabel-variabel tersebut (metadata) adalah sebagai berikut:

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-3-eval-4-metadata)Metadata variabel survei mahasiswa</caption>
 <thead>
  <tr>
   <th style="text-align:left;"> Nama Variabel </th>
   <th style="text-align:left;"> Deskripsi </th>
   <th style="text-align:left;"> Nilai-nilai yang valid </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> `KodeResp` </td>
   <td style="text-align:left;"> Nomor urut responden </td>
   <td style="text-align:left;"> tiga digit angka, hingga jumlah responden minimal </td>
  </tr>
  <tr>
   <td style="text-align:left;"> `Usia` </td>
   <td style="text-align:left;"> Usia responden (tahun) </td>
   <td style="text-align:left;"> 18 - ∞ </td>
  </tr>
  <tr>
   <td style="text-align:left;"> `Fakultas` </td>
   <td style="text-align:left;"> Fakultas mahasiswa </td>
   <td style="text-align:left;"> 1 = Fakultas Syariah,<br>2 = Fakultas Tarbiyah dan Keguruan,<br>3 = Fakultas Dakwah dan Komunikasi </td>
  </tr>
  <tr>
   <td style="text-align:left;"> `ThnMsk` </td>
   <td style="text-align:left;"> Tahun masuk kuliah (Masehi) </td>
   <td style="text-align:left;"> 2018 - 2022 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> `UangSaku` </td>
   <td style="text-align:left;"> Uang saku mahasiswa per bulan </td>
   <td style="text-align:left;"> 1 = &lt;1 juta rupiah,<br>2 = 1-2 juta rupiah,<br>3 = 2-3 juta rupiah,<br>4 = 3-4 juta,<br>5 = &gt;4 juta </td>
  </tr>
  <tr>
   <td style="text-align:left;"> `Jarak` </td>
   <td style="text-align:left;"> Jarak tempat tinggal mahasiswa dari kampus (km) </td>
   <td style="text-align:left;"> 0 - ∞ </td>
  </tr>
</tbody>
</table>

1. Identifikasilah statistik deskriptif yang dapat dikenakan pada variabel-variabel berikut: [STP-2.2]{.capaian}
  
  a. Fakultas
  b. Uang saku
  c. Jarak
  
  Sertakan juga hasil perhitungan kalian dengan langkah yang dapat dipertanggungjawabkan.
2. Interpretasikan salah satu hasil statistik deskriptif yang telah dihitung pada masing-masing variabel. [STP-2.3]{.capaian}

:::

<!--chapter:end:03-statistik-deskriptif.Rmd-->

# Visualisasi Data Kuantitatif

## Konsep Dasar

Visualisasi data adalah mengubah bentuk penyajian data/presentasi data dari bentuk tabular/tabel menjadi bentuk grafis. Kita sering mendengar pepatah yang berbunyi *"a picture is worth a thousand words"* yang artinya kurang lebih "satu gambar bernilai seribu kata." Pepatah ini menggambarkan bahwa data yang disajikan dalam bentuk gambar/grafis dapat menampilkan banyak sekali informasi kepada audiens.

Sajian data dalam bentuk gambar disebut juga **grafik** atau **diagram** *(chart)*. Jenis grafik atau diagram yang digunakan sangat bergantung pada jenis dan tingkat pengukuran variabel yang akan divisualisasikan.

Banyak sekali panduan-panduan untuk memilih bentuk grafik yang perlu Anda gunakan untuk menyajikan data Anda. Salah satu sumber yang menyediakan panduan tersebut adalah situs @fromdatatoviz atau @Ferdio.


## Jenis-jenis Diagram

Untuk memilih jenis diagram yang tepat, kita perlu menentukan terlebih dahulu jenis dan tingkat pengukuran variabel yang akan kita sajikan. Kemudian, kita dapat mempertimbangkan jenis informasi apa yang ingin kita sajikan dan menyesuaikannya dengan cara menampilkan nilainya, bisa dengan sumbu (tegak/datar; Y/X) atau yang lainnya. Berikut adalah pembahasan sebagian jenis-jenis diagram berdasarkan jenis nilai dan tingkat pengukuran variabel yang sudah kita bahas dan tujuan penggunaanya.

### Variabel Kategorikal

Visualisasi variabel kategorikal bertujuan menampilkan **jumlah (frekuensi) objek** untuk masing-masing kategori. Untuk menentukan jenis diagram yang tepat, kita perlu memperhatikan **jumlah variabel** yang dianalisis dan **hubungan antarvariabel**.

#### Grafik Batang *(Column/Bar Chart)*

Grafik batang adalah grafik yang paling sering digunakan untuk memvisualkan variabel kategorikal. Grafik ini memberikan informasi berupa **sebaran frekuensi** sebuah variabel. 

Bentuk grafik batang tersusun dari dua sumbu tegak (Y) dan datar (X). Tinggi batang sepanjang sumbu Y bermakna frekuensi dari kategori-kategori yang ada dalam variabel, sementara kategori-kategori berada di sepanjang sumbu X.

Terdapat dua jenis grafik batang: tegak dan mendatar. Grafik batang tegak disebut juga *column chart* sementara yang mendatar disebut *bar chart*. Perbedaan column chart dan bar chart hanya terletak di **sumbu yang menunjukkan frekuensi kategori**, yakni tinggi/panjang batang. Grafik batang yang menggunakan sumbu Y untuk menunjukkan jumlah frekuensinya adalah ***column chart***, sementara yang menggunakan sumbu X adalah ***bar chart***.

Untuk lebih memahami bagaimana mengubah data terstruktur menjadi grafik batang, penjelasannya dapat dilihat di Studi Kasus di bawah.


#### Grafik Batang Bertumpuk (Stacked Column/Bar Chart) {.materi-bar-chart}

Grafik batang bertumpuk *(stacked bar/column chart)* digunakan untuk membandingkan komposisi dari beberapa kategori. Setiap batang mewakili nilai total, yang kemudian dipecah menjadi beberapa segmen untuk menunjukkan bagaimana kontribusi masing-masing subkategori membentuk total tersebut. Kategori kedua variabel tersebut dibuat bertumpukan. Misalnya sebaran pengguna kendaraan (mobil, motor, sepeda) berdasarkan jenis kelamin (laki-laki dan perempuan).

Untuk lebih memahami bagaimana mengubah data terstruktur menjadi grafik batang bertumpuk, penjelasannya dapat dilihat di Studi Kasus di bawah. Secara umum, data mentah diubah menjadi tabel distribusi frekuensi, dan tabel distribusi frekuensi itu yang menjadi bahan pembuatan grafik.

::: rmdkasus

### Studi Kasus: Visualisasi Moda Transportasi Mahasiswa dengan Diagram Batang  {.unnumbered}

Untuk memahami pembuatan grafik batang, kita akan menganalisis data moda transportasi mahasiswa UIN Raden Intan Lampung. Langkah pertama adalah mengubah data mentah menjadi tabel distribusi frekuensi, baru kemudian divisualisasikan.


``` r
# Memuat data
data_uinril <- read.csv2("datasets/DataUtama_mhsUINRIL.csv")

# Membuat tabel distribusi frekuensi untuk moda transportasi
tabel_moda <- table(data_uinril$kendaraan.utama)
tabel_moda
```

```
## 
##                  Berjalan Kaki Kendaraan Bermotor (menumpang) 
##                             33                             27 
##                  Mobil Pribadi                         Sepeda 
##                             15                              5 
##           Sepeda Motor Pribadi            Transportasi Online 
##                            290                             30
```

Setelah mendapatkan tabel distribusi frekuensi, kita dapat membuat grafik batang tegak (*column chart*):


``` r
barplot(tabel_moda,
  main = "Distribusi Moda Transportasi Mahasiswa UINRIL",
  xlab = "Moda Transportasi",
  ylab = "Frekuensi",
  col = "#3498db",
  las = 2
)
```

<div class="figure" style="text-align: center">
<img src="_main_files/figure-html/fig-column-moda-1.png" alt="Grafik batang tegak distribusi moda transportasi" width="70%" />
<p class="caption">(\#fig:fig-column-moda)Grafik batang tegak distribusi moda transportasi</p>
</div>

Atau dalam bentuk grafik batang mendatar (*bar chart*):


``` r
barplot(tabel_moda,
  main = "Distribusi Moda Transportasi Mahasiswa UINRIL",
  xlab = "Frekuensi",
  ylab = "Moda Transportasi",
  col = "#e74c3c",
  horiz = TRUE,
  las = 1
)
```

<div class="figure" style="text-align: center">
<img src="_main_files/figure-html/fig-bar-moda-1.png" alt="Grafik batang mendatar distribusi moda transportasi" width="70%" />
<p class="caption">(\#fig:fig-bar-moda)Grafik batang mendatar distribusi moda transportasi</p>
</div>

Untuk **grafik batang bertumpuk**, kita memerlukan dua variabel kategorikal. Kita akan membandingkan moda transportasi berdasarkan jenis kelamin:


``` r
# Membuat tabel kontingensi (distribusi frekuensi dua variabel)
tabel_moda_jk <- table(data_uinril$Jenis.Kelamin, data_uinril$kendaraan.utama)
tabel_moda_jk
```

```
##            
##             Berjalan Kaki Kendaraan Bermotor (menumpang) Mobil Pribadi Sepeda
##   Laki-laki             1                              9             6      2
##   Perempuan            32                             18             9      3
##            
##             Sepeda Motor Pribadi Transportasi Online
##   Laki-laki                  167                   3
##   Perempuan                  123                  27
```

Dari tabel kontingensi tersebut, kita dapat membuat grafik batang bertumpuk:


``` r
barplot(tabel_moda_jk,
  main = "Moda Transportasi Berdasarkan Jenis Kelamin",
  xlab = "Moda Transportasi",
  ylab = "Frekuensi",
  col = c("#9b59b6", "#f39c12"),
  legend = rownames(tabel_moda_jk),
  las = 2,
  args.legend = list(x = "topright")
)
```

<div class="figure" style="text-align: center">
<img src="_main_files/figure-html/fig-stacked-bar-1.png" alt="Grafik batang bertumpuk moda transportasi berdasarkan jenis kelamin" width="75%" />
<p class="caption">(\#fig:fig-stacked-bar)Grafik batang bertumpuk moda transportasi berdasarkan jenis kelamin</p>
</div>

**Interpretasi:** Grafik menunjukkan bahwa sepeda motor merupakan moda transportasi yang paling banyak digunakan oleh mahasiswa UINRIL, diikuti oleh mobil dan angkutan umum. Dari grafik batang bertumpuk terlihat bahwa penggunaan sepeda motor lebih dominan pada mahasiswa laki-laki dibandingkan perempuan, sementara penggunaan angkutan umum relatif seimbang antara kedua jenis kelamin.

:::


#### Grafik Lollipop

Diagram lollipop pada dasarnya serupa dengan diagram batang, hanya saja data direpresentasikan oleh tiang-tiang berujung lingkaran yang menyerupai permen loli. Penggunaannya sangat cocok untuk data berjumlah banyak guna menghindari efek Moiré (dibaca `moarey') @wikipedia2025moire. Efek Moiré adalah ilusi optik pergerakan benda yang posisinya berdekatan dan membentuk sebuah kisi (fringe) seperti yang ditunjukkan Gambar \@ref(fig:contoh-moire), sehingga dapat menyulitkan pembaca grafik.


::: rmdkasus

### Studi Kasus: Perbandingan Grafik Lollipop dengan Grafik Batang {.unnumbered}

Pada dataset dengan banyak kategori, grafik batang konvensional dapat menghasilkan efek Moiré yang mengganggu. Mari kita bandingkan penggunaan grafik batang biasa dengan grafik lollipop menggunakan data fakultas mahasiswa UINRIL.


``` r
# Install package ggplot2 jika belum ada
# install.packages('ggplot2')
library(ggplot2)

# Memuat data dan membuat tabel frekuensi fakultas
data_uinril <- read.csv2("datasets/DataUtama_mhsUINRIL.csv")
tabel_fakultas <- as.data.frame(table(data_uinril$Fakultas))
colnames(tabel_fakultas) <- c("Fakultas", "Frekuensi")

# Mengurutkan berdasarkan frekuensi
tabel_fakultas <- tabel_fakultas[order(tabel_fakultas$Frekuensi, decreasing = TRUE), ]
tabel_fakultas
```

```
##                     Fakultas Frekuensi
## 5      Tarbiyah dan Keguruan       158
## 3   Ekonomi dan Bisnis Islam        85
## 4                    Syariah        59
## 2 Dakwah dan Ilmu Komunikasi        49
## 6 Ushuluddin dan Studi Agama        44
## 1                       Adab         5
```

Berikut adalah visualisasi menggunakan grafik batang biasa:


``` r
ggplot(tabel_fakultas, aes(x = reorder(Fakultas, -Frekuensi), y = Frekuensi)) +
  geom_bar(stat = "identity", fill = "#3498db", width = 0.8) +
  theme_minimal() +
  labs(
    title = "Distribusi Mahasiswa per Fakultas (Grafik Batang)",
    x = "Fakultas",
    y = "Frekuensi"
  ) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1, size = 8))
```

<div class="figure" style="text-align: center">
<img src="_main_files/figure-html/fig-bar-fakultas-1.png" alt="Grafik batang fakultas mahasiswa UINRIL" width="85%" />
<p class="caption">(\#fig:fig-bar-fakultas)Grafik batang fakultas mahasiswa UINRIL</p>
</div>

Sekarang bandingkan dengan grafik lollipop:


``` r
ggplot(tabel_fakultas, aes(x = reorder(Fakultas, -Frekuensi), y = Frekuensi)) +
  geom_segment(aes(x = Fakultas, xend = Fakultas, y = 0, yend = Frekuensi),
    color = "#95a5a6", size = 0.5
  ) +
  geom_point(color = "#e74c3c", size = 3) +
  theme_minimal() +
  labs(
    title = "Distribusi Mahasiswa per Fakultas (Grafik Lollipop)",
    x = "Fakultas",
    y = "Frekuensi"
  ) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1, size = 8))
```

<div class="figure" style="text-align: center">
<img src="_main_files/figure-html/fig-lollipop-fakultas-1.png" alt="Grafik lollipop fakultas mahasiswa UINRIL" width="85%" />
<p class="caption">(\#fig:fig-lollipop-fakultas)Grafik lollipop fakultas mahasiswa UINRIL</p>
</div>

**Perbandingan:** Pada grafik lollipop, setiap kategori lebih mudah dibedakan karena hanya tiang tipis dan titik yang mewakili nilai, sehingga menghindari efek visual yang berlebihan (Moiré). Grafik lollipop sangat cocok untuk dataset dengan banyak kategori seperti ini, karena lebih ringkas dan tetap informatif. Sementara grafik batang biasa terlihat lebih padat dan dapat menimbulkan kesulitan dalam membaca data ketika batang-batangnya berdekatan.

:::

#### Grafik *Treemap*

Secara fungsi, treemap dan *stacked bar chart* sangat mirip karena keduanya menunjukkan distribusi frekuensi objek berdasarkan kategori variabelnya. Jika *stacked chart* memakai panjang segmen pada batang untuk menunjukkan proporsi, *treemap* menggunakan luas area persegi panjang. Frekuensinya diperlihatkan oleh **luas persegi masing-masing kategori**.

Proses pembuatannya sama persis seperti dengan grafik batang bertumpuk.

::: rmdkasus

### Studi Kasus: Membuat Treemap Moda Transportasi {.unnumbered}

Treemap menggunakan luas area persegi untuk menunjukkan proporsi kategori. Seperti pada grafik batang bertumpuk, kita mulai dari tabel distribusi frekuensi dua variabel.


``` r
# Install package treemap jika belum ada
# install.packages('treemap')
library(treemap)

# Memuat data
data_uinril <- read.csv2("datasets/DataUtama_mhsUINRIL.csv")

# Membuat tabel kontingensi dan mengubahnya ke data frame
tabel_moda_jk <- as.data.frame(table(data_uinril$Jenis.Kelamin, data_uinril$kendaraan.utama))
colnames(tabel_moda_jk) <- c("Jenis_Kelamin", "Moda_Transportasi", "Frekuensi")

# Menampilkan tabel
tabel_moda_jk
```

```
##    Jenis_Kelamin              Moda_Transportasi Frekuensi
## 1      Laki-laki                  Berjalan Kaki         1
## 2      Perempuan                  Berjalan Kaki        32
## 3      Laki-laki Kendaraan Bermotor (menumpang)         9
## 4      Perempuan Kendaraan Bermotor (menumpang)        18
## 5      Laki-laki                  Mobil Pribadi         6
## 6      Perempuan                  Mobil Pribadi         9
## 7      Laki-laki                         Sepeda         2
## 8      Perempuan                         Sepeda         3
## 9      Laki-laki           Sepeda Motor Pribadi       167
## 10     Perempuan           Sepeda Motor Pribadi       123
## 11     Laki-laki            Transportasi Online         3
## 12     Perempuan            Transportasi Online        27
```

Dari tabel distribusi frekuensi tersebut, kita dapat membuat treemap:


``` r
treemap(tabel_moda_jk,
  index = c("Moda_Transportasi", "Jenis_Kelamin"),
  vSize = "Frekuensi",
  type = "index",
  title = "Komposisi Moda Transportasi Berdasarkan Jenis Kelamin",
  fontsize.labels = c(12, 10),
  fontcolor.labels = c("white", "white"),
  bg.labels = 0,
  border.col = "white",
  border.lwds = 2,
  palette = "Set2"
)
```

<div class="figure" style="text-align: center">
<img src="_main_files/figure-html/fig-treemap-moda-1.png" alt="Treemap moda transportasi berdasarkan jenis kelamin" width="80%" />
<p class="caption">(\#fig:fig-treemap-moda)Treemap moda transportasi berdasarkan jenis kelamin</p>
</div>

**Interpretasi:** Treemap menunjukkan proporsi penggunaan moda transportasi dengan jelas melalui luas area. Area terbesar dimiliki oleh sepeda motor, menunjukkan dominasinya sebagai moda transportasi utama. Di dalam setiap moda, terdapat sub-area yang menunjukkan pembagian berdasarkan jenis kelamin. Visualisasi ini memudahkan kita untuk membandingkan proporsi secara langsung tanpa perlu membaca angka.

:::

#### Grafik Pai/Donat *(Pie/Donut Chart)*

Grafik jenis ini juga sering digunakan untuk visualisasi variabel kategoris. Perbedaan dengan grafik batang adalah frekuensi tiap kategori tidak diperlihatkan dengan sumbu tegak, tetapi besar juring (sektor) lingkaran.

Proses pembuatannya sama seperti pembuatan grafik batang yang ditunjukkan pada kasus di \@ref(materi-bar-chart), hanya saja jumlah kategori menjadi jumlah sektor, sementara frekuensinya menjadi ukuran sektor.

::: rmdkasus

### Studi Kasus: Membuat Grafik Pai dan Donat {.unnumbered}

Grafik pai dan donat menggunakan juring lingkaran untuk menunjukkan proporsi kategori. Prosesnya sama dengan grafik batang, dimulai dari tabel distribusi frekuensi.


``` r
# Memuat data
data_uinril <- read.csv2("datasets/DataUtama_mhsUINRIL.csv")

# Membuat tabel distribusi frekuensi untuk moda transportasi
tabel_moda <- table(data_uinril$kendaraan.utama)
tabel_moda
```

```
## 
##                  Berjalan Kaki Kendaraan Bermotor (menumpang) 
##                             33                             27 
##                  Mobil Pribadi                         Sepeda 
##                             15                              5 
##           Sepeda Motor Pribadi            Transportasi Online 
##                            290                             30
```

Dari tabel distribusi frekuensi, kita dapat membuat grafik pai (*pie chart*):


``` r
# Menghitung persentase
persentase <- round(100 * tabel_moda / sum(tabel_moda), 1)
label <- paste0(names(tabel_moda), "\n", persentase, "%")

pie(tabel_moda,
  labels = label,
  main = "Distribusi Moda Transportasi Mahasiswa UINRIL",
  col = c("#3498db", "#e74c3c", "#f39c12", "#2ecc71", "#9b59b6"),
  border = "white"
)
```

<div class="figure" style="text-align: center">
<img src="_main_files/figure-html/fig-pie-moda-1.png" alt="Grafik pai moda transportasi mahasiswa UINRIL" width="70%" />
<p class="caption">(\#fig:fig-pie-moda)Grafik pai moda transportasi mahasiswa UINRIL</p>
</div>

Untuk membuat grafik donat (*donut chart*), kita mengubah jenis kategori menjadi juring-juring lingkaran dan sudunya ditentukan dari proporsi frekuensi. Prosesnya sama dengan grafik pai, hanya saja kita di tengahnya ada ruang kosong yang dapat digunakan untuk informasi tambahan.


``` r
library(ggplot2)

# Mengubah tabel menjadi data frame
df_moda <- as.data.frame(tabel_moda)
colnames(df_moda) <- c("Moda", "Frekuensi")

# Menghitung persentase dan posisi label
df_moda$Persentase <- round(100 * df_moda$Frekuensi / sum(df_moda$Frekuensi), 1)
df_moda$Label <- paste0(df_moda$Persentase, "%")

# Membuat donut chart
ggplot(df_moda, aes(x = 2, y = Frekuensi, fill = Moda)) +
  geom_bar(stat = "identity", width = 1, color = "white") +
  coord_polar(theta = "y") +
  xlim(0.5, 2.5) +
  theme_void() +
  labs(title = "Distribusi Moda Transportasi (Donut Chart)") +
  geom_text(aes(label = Label),
    position = position_stack(vjust = 0.5),
    color = "white", size = 4
  ) +
  scale_fill_manual(values = c("#3498db", "#e74c3c", "#f39c12", "#2ecc71", "#9b59b6", "#34495e"))
```

<div class="figure" style="text-align: center">
<img src="_main_files/figure-html/fig-donut-moda-1.png" alt="Grafik donat moda transportasi mahasiswa UINRIL" width="70%" />
<p class="caption">(\#fig:fig-donut-moda)Grafik donat moda transportasi mahasiswa UINRIL</p>
</div>

**Interpretasi:** Baik grafik pai maupun donat menunjukkan proporsi penggunaan moda transportasi dengan jelas. Sepeda motor mendominasi dengan proporsi terbesar, diikuti oleh mobil dan angkutan umum. Grafik donat memberikan tampilan yang lebih modern dengan ruang kosong di tengahnya yang dapat digunakan untuk informasi tambahan.

:::


### Variabel Numerik

Berbeda dengan visualisasi variabel kategorikal yang memperlihatkan frekuensi masing-masing kategori dalam variabel, grafik data dengan variabel numerik merepresentasikan nilai yang sebenarnya. 

Persamaan dengan visualisasi pada data kategorikal adalah perlunya pertimbangan **jumlah variabel** dan cara menyajikan nilianya dengan sumbu atau bukan. Selain itu juga perlu dipertimbangkan **keterurutan objek/observasi *(order)***.

Berikut adalah tinjauan beberapa jenis grafik visualisasi data variabel numerik dengan masing-masing ilustrasi data terstrukturnya.

#### Histogram

Histogram menunjukkan distribusi nilai-nilai yang berada pada rentang tertentu. Rentang nilai ditunjukkan di sumbu X-nya, sementara sumbu Y adalah frekuensinya. Istilah untuk rentang-rentang ini disebut ***bin***, sementara lebar/ukurannya disebut ***bin size*** atau ***bin width***.


::: rmdnote

[Penting!]{.tajuksaya}

Jangan tertukar antara histogram dengan grafik batang! Perbedaan mendasar keduanya terletak pada sumbu X-nya. Sumbu X pada histogram menunjukkan angka, sementara pada grafik batang menunjukkan kategorinya.

Satu karakteristik lain yang membedakan histogram dengan grafik batang adalah **jarak antarbatangnya**. Grafik batang biasanya memiliki celah di antara batangnya, sementara histogram tidak memiliki celah.

:::


Proses pembuatan histogram dari tabel data terstruktur diilustrasikan oleh kasus berikut. Dalam proses ini, variabel numerik dikelompokkan ke dalam interval atau rentang tertentu. Selanjutnya, frekuensi merepresentasikan jumlah total objek yang nilainya berada di dalam masing-masing rentang tersebut.

::: rmdkasus

### Studi Kasus: Membuat Histogram Biaya Perjalanan {.unnumbered}

Histogram menunjukkan distribusi nilai numerik dengan mengelompokkannya ke dalam interval (bin). Mari kita visualisasikan biaya perjalanan mahasiswa ITERA.


``` r
# Memuat data
data_itera <- read.csv2("datasets/DataUtama_mhsITERA.csv")

# Melihat statistik deskriptif
summary(data_itera$biaya.dalam.sepekan)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##       0   20000   30000   38666   45000  400000
```

Sebelum membuat histogram, kita perlu mengelompokkan nilai-nilai ke dalam interval (bin). R melakukan ini secara otomatis, tetapi kita juga bisa mengatur sendiri. Mari kita buat histogram dengan pengaturan bin otomatis:


``` r
hist(data_itera$biaya.dalam.sepekan,
  main = "Distribusi Biaya Perjalanan Mahasiswa ITERA",
  xlab = "Biaya Perjalanan (Rp ribu)",
  ylab = "Frekuensi",
  col = "#3498db",
  border = "white",
  las = 1
)
```

<div class="figure" style="text-align: center">
<img src="_main_files/figure-html/fig-hist-biaya-auto-1.png" alt="Histogram biaya perjalanan (bin otomatis)" width="75%" />
<p class="caption">(\#fig:fig-hist-biaya-auto)Histogram biaya perjalanan (bin otomatis)</p>
</div>

Kita juga dapat mengatur jumlah bin secara manual untuk melihat distribusi dengan lebih detail:


``` r
# Membuat histogram dengan 15 bin
hist(data_itera$biaya.dalam.sepekan,
  breaks = 15,
  main = "Distribusi Biaya Perjalanan (15 Bin)",
  xlab = "Biaya Perjalanan (Rp ribu)",
  ylab = "Frekuensi",
  col = "#e74c3c",
  border = "white",
  las = 1
)
```

<div class="figure" style="text-align: center">
<img src="_main_files/figure-html/fig-hist-biaya-manual-1.png" alt="Histogram biaya perjalanan (bin manual)" width="75%" />
<p class="caption">(\#fig:fig-hist-biaya-manual)Histogram biaya perjalanan (bin manual)</p>
</div>

Untuk lebih memahami proses binning, mari kita buat tabel frekuensi manual:


``` r
# Membuat interval bin
bins <- seq(0, max(data_itera$biaya.dalam.sepekan, na.rm = TRUE), length.out = 10)

# Mengelompokkan data ke dalam bin
data_itera$bin <- cut(data_itera$biaya.dalam.sepekan, breaks = bins, include.lowest = TRUE)

# Membuat tabel frekuensi
tabel_freq <- table(data_itera$bin)
head(tabel_freq)
```

```
## 
##        [0,4.44e+04] (4.44e+04,8.89e+04] (8.89e+04,1.33e+05] (1.33e+05,1.78e+05] 
##                 318                  80                  13                   7 
## (1.78e+05,2.22e+05] (2.22e+05,2.67e+05] 
##                   7                   1
```

**Interpretasi:** Histogram menunjukkan bahwa sebagian besar mahasiswa ITERA memiliki biaya perjalanan dalam rentang rendah hingga menengah, dengan konsentrasi terbesar pada rentang 0-50 ribu rupiah. Distribusi menunjukkan pola miring ke kanan (*right-skewed*), yang berarti terdapat beberapa mahasiswa dengan biaya perjalanan yang sangat tinggi. Informasi ini penting untuk perencanaan transportasi kampus, misalnya dalam menentukan subsidi atau rute angkutan kampus.

:::


#### *Boxplot*

Boxplot adalah grafik berbentuk kotak dan garis yang menampilkan ukuran penyebaran suatu variabel numerik secara grafis (Gambar \@ref(fig:jenis-boxplot)). Sebagaimana yang ditunjukkan oleh gambar tersebut, kotak dan garis pada boxplot dapat berjumlah satu atau lebih. Satu kotak dan garis menandakan hanya ada satu kategori objek dengan variabel numerik yang ditampilkan.

Sementara itu, variabel numerik tersebut dikategorikan lagi berdasarkan suatu variabel kategoris, maka jumlah kotak dan garisnya bisa lebih dari satu.

Setiap elemen pada boxplot memiliki makna ukuran penyebaran. Ini dijelaskan pada kasus berikut.

::: rmdkasus

### Studi Kasus: Membuat Boxplot Biaya Perjalanan Mahasiswa {.unnumbered}

Boxplot menampilkan ukuran penyebaran data numerik secara grafis. Mari kita buat boxplot untuk menganalisis distribusi biaya perjalanan mahasiswa dari berbagai universitas.





































