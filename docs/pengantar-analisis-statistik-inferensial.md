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

Buku ini dirancang untuk membantu mahasiswa dalam memahami konsep statistika dan penggunaan R dalam pengolahan data kuantitatif, terutama dalam perencanaan wilayah dan kota. Buku ini terdiri atas 15 bab yang terdiri atas beberapa bagian:

1. Konsep Dasar Statistika
    1. Konsep Dasar Statistika dalam Perencanaan
    1. Data Terstruktur
2. Statistika Univariat
    1. Analisis Statistik Deskriptif
    1. Visualisasi Data Kuantitatif
    1. Pengantar Statistik Inferensial
    1. Estimasi Parameter
    1. Uji Hipotesis Satu Populasi
    1. Uji Hipotesis Dua Populasi
    1. Uji Hipotesis Lebih dari Dua Populasi
3. Statistika Bivariat
    1. Korelasi Antarvariabel Nominal
    1. Korelasi Antarvariabel Ordinal
    1. Korelasi Antarvariabel Metrik
    1. Regresi Linear Sederhana
4. Statistika Multivariat
    1. Regresi Linear Berganda
    1. Analisis Statistik Multivariat Interdependensi


------------------------------------

# Pengantar {.unnumbered}

Puji dan syukur kami panjatkan ke hadirat Tuhan Yang Maha Esa, Allah *subhanahu wa ta’aala*, yang tanpa rahmat, izin, dan kekuatan dari-Nya modul ini tidak akan pernah bisa dirampungkan. Kami juga memanjatkan salawat dan permohonan keselamatan untuk Rasul junjungan kami dan seluruh alam, Nabi Muhammad *shallallahu alaihi wa sallam*, pembawa risalah kebenaran dan transformator peradaban terbesar sepanjang sejarah.

Buku ajar ini kami rancang sebagai media pembelajaran sekaligus instrumen evaluasinya untuk mahasiswa yang mempelajari statistika, khususnya di bidang Perencanaan Wilayah dan Kota. Kasus-kasus yang digunakan dalam pembahasannya diambil dari dataset yang diupayakan oleh delapan orang mahasiswa PWK ITERA angkatan 2020: Alvian Syah Syaidina Muhammad, Muhammad Gilang Ramadhan, Assa Bangsa Putra, Fachrian Noor Kusnadi, Bonafasius Geoffrey Titawanno, dan Ramli Indran Alif di bawah bimbingan penulis.

Buku ajar ini pastinya masih jauh dari kesempurnaan. Untuk itu, kami sangat terbuka akan masukan dan kritikan demi kesempurnaan modul ini ke depannya. Segala masukan dan kritikan akan kami tampung melalui surel [muhammad.bindar@pwk.itera.ac.id](mailto:muhammad.bindar@pwk.itera.ac.id) dan jadikan pembelajaran untuk perbaikan selanjutnya.

Lampung Selatan, 2025

Tim Penulis


------------------------------------

# Lembar Persembahan

Buku ini kami dedikasikan untuk guru-guru kami, Ibu **Dewi Sawitri Tjokropandojo** dan Ibu **Sri Maryati**, atas ilmu dan teladan yang tak ternilai

<!--chapter:end:index.Rmd-->

# Konsep Dasar Statistika dalam Perencanaan

::: rmdcapaian
### Capaian Pembelajaran {.unnumbered}

Setelah mempelajari bab ini, Anda diharapkan:

-   Mampu menjelaskan kedudukan dan peran analisis statistik dalam perencanaan [STP-1.1]{.capaian}
-   Mampu menjelaskan perbedaan analisis kuantitatif dan kualitatif dengan tepat [STP-1.2]{.capaian}
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
### Studi Kasus: Analisis Data dalam Perencanaan Transportasi Berkelanjutan di Kampus ITERA {#kasus-analisis-data-dalam-perencanaan .unnumbered}

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

Berdasarkan pertanyaan penelitian *sudah sejauh mana keberlanjutan pada pola pergerakan pada mahasiswa dan pegawai kampus ITERA saat ini?*, kita akan mengumpulkan data terkait pola pergerakan mahasiswa dan pegawai di ITERA dengan menyebarkan kuesioner kepada para mahasiswa dan pegawai kampus ITERA tentang pola pergerakan mereka. Berikut adalah analisis tentang perbandingan antara analisis kuantitatif dan analisis kualitatif.

| Aspek | Analisis Kuantitatif | Analisis Kualitatif |
|:---------------|:--------------------------|:----------------------------|
| **Fokus** | Luas (*Breadth*), mencari generalisasi. | Dalam (*Depth*), mencari makna/alasan. |
| **Pertanyaan Utama** | Berapa banyak emisi yang dihasilkan? | Mengapa orang enggan naik shuttle? |
| **Alat Analisis** | Statistik (SPSS, Excel, Pemodelan Transportasi). | Transkrip wawancara, observasi lapangan, analisis tema. |
| **Kelebihan** | Akurat untuk menghitung target penurunan emisi karbon secara matematis. | Sangat baik untuk merancang kebijakan yang sesuai dengan psikologi pengguna. |
| **Kelemahan** | Tidak bisa menjelaskan alasan personal di balik angka. | Hasilnya tidak bisa digeneralisasi untuk seluruh populasi secara kaku. |
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
2.  Ceritakan perbedaan analisis kuantitatif dan kualitatif yang mungkin digunakan dalam perencanaan acara tersebut. [STP-1.2]{.capaian}
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
### Studi Kasus: Elemen Data Terstruktur {.unnumbered} 

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
<caption>(\#tab:bab-3-kuartil-unila)Nilai Kuartil Biaya Perjalanan Mahasiswa UNILA (n = 394)</caption>
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

Dari total **394** mahasiswa yang diamati, kita dapat menafsirkan posisi data sebagai berikut:

1.  **Kuartil Bawah ($Q_1$):** Sebesar 25% dari populasi (sekitar **98** mahasiswa) memiliki biaya perjalanan sepekan kurang dari atau sama dengan nilai $Q_1$. Ini menandakan kelompok dengan biaya transportasi paling efisien.
2.  **Kuartil Tengah ($Q_2$):** Sebesar 50% (sekitar **197** mahasiswa) memiliki biaya perjalanan kurang dari atau sama dengan median. Ini adalah titik tengah distribusi.
3.  **Kuartil Atas ($Q_3$):** Sebesar 75% (sekitar **296** mahasiswa) memiliki biaya perjalanan di bawah nilai $Q_3$. Artinya, hanya 25% sisanya (sekitar **98** mahasiswa) yang menghabiskan biaya perjalanan di atas nilai tersebut (kelompok dengan biaya tinggi).

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

::: rmdcapaian
### Capaian Pembelajaran {.unnumbered}

Setelah mempelajari bab ini, Anda diharapkan:

1. mampu memilih visualisasi yang tepat sesuai dengan variabel yang akan disajikan dan informasi yang ingin disampaikan [STP-3.1]{.capaian}
2. mampu menginterpretasikan suatu visualisasi data kuantitatif secara mendalam [STP-3.2]{.capaian}
3. mampu menjelaskan pentingnya menentukan tingkat pengukuran untuk sebuah variabel dari kaitannya dengan analisis statistik deskriptif dan diagram yang dipilih untuk menyajikan informasi [STP-3.4]{.capaian}
:::


## Konsep Dasar

Visualisasi data adalah mengubah bentuk penyajian data/presentasi data dari bentuk tabular/tabel menjadi bentuk grafis. Kita sering mendengar pepatah yang berbunyi *"a picture is worth a thousand words"* yang artinya kurang lebih "satu gambar bernilai seribu kata." Pepatah ini menggambarkan bahwa data yang disajikan dalam bentuk gambar/grafis dapat menampilkan banyak sekali informasi kepada audiens.

Sajian data dalam bentuk gambar disebut juga **grafik** atau **diagram** *(chart)*. Jenis grafik atau diagram yang digunakan sangat bergantung pada jenis dan tingkat pengukuran variabel yang akan divisualisasikan.

Banyak sekali panduan-panduan untuk memilih bentuk grafik yang perlu Anda gunakan untuk menyajikan data Anda. Salah satu sumber yang menyediakan panduan tersebut adalah situs [From data to Viz](https://www.data-to-viz.com/) atau [Data Viz Project](https://datavizproject.com/).


## Jenis-jenis Diagram

Untuk memilih jenis diagram yang tepat, kita perlu menentukan terlebih dahulu jenis dan tingkat pengukuran variabel yang akan kita sajikan. Kemudian, kita dapat mempertimbangkan jenis informasi apa yang ingin kita sajikan dan menyesuaikannya dengan cara menampilkan nilainya, bisa dengan sumbu (tegak/datar; Y/X) atau yang lainnya. Berikut adalah pembahasan sebagian jenis-jenis diagram berdasarkan jenis nilai dan tingkat pengukuran variabel yang sudah kita bahas dan tujuan penggunaanya.

### Variabel Kategorikal

Visualisasi variabel kategorikal bertujuan menampilkan **jumlah (frekuensi) objek** untuk masing-masing kategori. Untuk menentukan jenis diagram yang tepat, kita perlu memperhatikan **jumlah variabel** yang dianalisis dan **hubungan antarvariabel**.

#### Grafik Batang *(Column/Bar Chart)*

Grafik batang adalah grafik yang paling sering digunakan untuk memvisualkan variabel kategorikal. Grafik ini memberikan informasi berupa **sebaran frekuensi** sebuah variabel. 

Bentuk grafik batang tersusun dari dua sumbu tegak (Y) dan datar (X). Tinggi batang sepanjang sumbu Y bermakna frekuensi dari kategori-kategori yang ada dalam variabel, sementara kategori-kategori berada di sepanjang sumbu X.

Terdapat dua jenis grafik batang: tegak dan mendatar. Grafik batang tegak disebut juga *column chart* sementara yang mendatar disebut *bar chart*. Perbedaan column chart dan bar chart hanya terletak di **sumbu yang menunjukkan frekuensi kategori**, yakni tinggi/panjang batang. Grafik batang yang menggunakan sumbu Y untuk menunjukkan jumlah frekuensinya adalah ***column chart***, sementara yang menggunakan sumbu X adalah ***bar chart***.

Untuk lebih memahami bagaimana mengubah data terstruktur menjadi grafik batang, penjelasannya dapat dilihat di Studi Kasus di bawah.


#### Grafik Batang Bertumpuk (Stacked Column/Bar Chart) {#materi-bar-chart}

Grafik batang bertumpuk *(stacked bar/column chart)* digunakan untuk membandingkan komposisi dari beberapa kategori. Setiap batang mewakili nilai total, yang kemudian dipecah menjadi beberapa segmen untuk menunjukkan bagaimana kontribusi masing-masing subkategori membentuk total tersebut. Kategori kedua variabel tersebut dibuat bertumpukan. Misalnya sebaran pengguna kendaraan (mobil, motor, sepeda) berdasarkan jenis kelamin (laki-laki dan perempuan).

Untuk lebih memahami bagaimana mengubah data terstruktur menjadi grafik batang bertumpuk, penjelasannya dapat dilihat di Studi Kasus di bawah. Secara umum, data mentah diubah menjadi tabel distribusi frekuensi, dan tabel distribusi frekuensi itu yang menjadi bahan pembuatan grafik.

::: rmdkasus

#### Studi Kasus: Visualisasi Moda Transportasi Mahasiswa dengan Diagram Batang  {.unnumbered}

Untuk memahami pembuatan grafik batang, kita akan menganalisis data moda transportasi mahasiswa UIN Raden Intan Lampung. Langkah pertama adalah mengubah data mentah menjadi tabel distribusi frekuensi (Tabel \@ref(tab:bab-4-diagram-batang)), baru kemudian divisualisasikan.

<table class="table table-striped table-hover table-condensed" style="width: auto !important; margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-4-diagram-batang)Distribusi Frekuensi Moda Transportasi Mahasiswa UIN Raden Intan Lampung</caption>
 <thead>
  <tr>
   <th style="text-align:left;"> Moda Transportasi </th>
   <th style="text-align:right;"> Frekuensi </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> Berjalan kaki </td>
   <td style="text-align:right;"> 38 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Menumpang kendaraan bermotor teman/keluarga </td>
   <td style="text-align:right;"> 27 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Mobil pribadi </td>
   <td style="text-align:right;"> 15 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Sepeda motor pribadi </td>
   <td style="text-align:right;"> 290 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Transportasi daring </td>
   <td style="text-align:right;"> 30 </td>
  </tr>
</tbody>
</table>

Setelah mendapatkan tabel distribusi frekuensi, kita dapat membuat grafik batang tegak (*column chart*)

<div class="figure" style="text-align: center">
<img src="figures/fig-column-moda-1.png" alt="Grafik batang tegak distribusi moda transportasi" width="75%" />
<p class="caption">(\#fig:fig-column-moda)Grafik batang tegak distribusi moda transportasi</p>
</div>

Atau dalam bentuk grafik batang mendatar (*bar chart*):

<div class="figure" style="text-align: center">
<img src="figures/fig-bar-moda-1.png" alt="Grafik batang mendatar distribusi moda transportasi" width="75%" />
<p class="caption">(\#fig:fig-bar-moda)Grafik batang mendatar distribusi moda transportasi</p>
</div>

Untuk **grafik batang bertumpuk**, kita memerlukan dua variabel kategorikal. Kita akan membandingkan moda transportasi berdasarkan jenis kelamin (Tabel \@ref(tab:tab-distribusi-2-var)).

<table class="table table-striped table-hover table-condensed" style="width: auto !important; margin-left: auto; margin-right: auto;">
<caption>(\#tab:tab-distribusi-2-var)Distribusi Frekuensi Moda Transportasi Mahasiswa UIN Raden Intan Lampung berdasarkan Jenis Kelamin</caption>
 <thead>
  <tr>
   <th style="text-align:left;"> Jenis Kelamin </th>
   <th style="text-align:right;"> Berjalan Kaki </th>
   <th style="text-align:right;"> Menumpang </th>
   <th style="text-align:right;"> Mobil Pribadi </th>
   <th style="text-align:right;"> Sepeda </th>
   <th style="text-align:right;"> Sepeda Motor </th>
   <th style="text-align:right;"> Transportasi Online </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> Laki-laki </td>
   <td style="text-align:right;"> 3 </td>
   <td style="text-align:right;"> 9 </td>
   <td style="text-align:right;"> 6 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 167 </td>
   <td style="text-align:right;"> 3 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Perempuan </td>
   <td style="text-align:right;"> 35 </td>
   <td style="text-align:right;"> 18 </td>
   <td style="text-align:right;"> 9 </td>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 123 </td>
   <td style="text-align:right;"> 27 </td>
  </tr>
</tbody>
</table>

Dari tabel kontingensi tersebut, kita dapat membuat grafik batang bertumpuk:

<div class="figure" style="text-align: center">
<img src="figures/fig-stacked-bar-1.png" alt="Grafik batang bertumpuk moda transportasi berdasarkan jenis kelamin" width="75%" />
<p class="caption">(\#fig:fig-stacked-bar)Grafik batang bertumpuk moda transportasi berdasarkan jenis kelamin</p>
</div>

**Interpretasi:** Grafik menunjukkan bahwa sepeda motor merupakan moda transportasi yang paling banyak digunakan oleh mahasiswa UINRIL, diikuti oleh mobil dan angkutan umum. Dari grafik batang bertumpuk terlihat bahwa penggunaan sepeda motor lebih dominan pada mahasiswa laki-laki dibandingkan perempuan, sementara penggunaan angkutan umum relatif seimbang antara kedua jenis kelamin.

:::


#### Grafik Lollipop

Diagram lollipop pada dasarnya serupa dengan diagram batang, hanya saja data direpresentasikan oleh tiang-tiang berujung lingkaran yang menyerupai permen loli. Penggunaannya sangat cocok untuk data berjumlah banyak guna menghindari efek Moiré (dibaca `moarey') @wikipedia2025moire. Efek Moiré adalah ilusi optik pergerakan benda yang posisinya berdekatan dan membentuk sebuah kisi (fringe) seperti yang ditunjukkan Gambar \@ref(fig:contoh-moire), sehingga dapat menyulitkan pembaca grafik.

<div class="figure" style="text-align: center">
<img src="images/contoh-moire.png" alt="Contoh efek Moiré pada grafik batang" width="60%" />
<p class="caption">(\#fig:contoh-moire)Contoh efek Moiré pada grafik batang</p>
</div>


::: rmdkasus

#### Studi Kasus: Perbandingan Grafik Lollipop dengan Grafik Batang {.unnumbered}

Pada dataset dengan banyak kategori, grafik batang konvensional dapat menghasilkan efek Moiré yang mengganggu. Mari kita bandingkan penggunaan grafik batang biasa dengan grafik lollipop menggunakan data program studi mahasiswa UINRIL.

<table class="table table-striped table-hover table-condensed" style="width: auto !important; margin-left: auto; margin-right: auto;border-bottom: 0;">
<caption>(\#tab:bab-4-distribusi-per-prodi)Distribusi Frekuensi Mahasiswa UIN Raden Intan Lampung Per Program Studi</caption>
 <thead>
  <tr>
   <th style="text-align:left;"> Nama Program Studi </th>
   <th style="text-align:right;"> Frekuensi </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> Hukum Keluarga </td>
   <td style="text-align:right;"> 31 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Ekonomi Syariah </td>
   <td style="text-align:right;"> 28 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Pendidikan Bahasa Inggris </td>
   <td style="text-align:right;"> 24 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Pendidikan Biologi </td>
   <td style="text-align:right;"> 23 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Manajemen Bisnis Syariah </td>
   <td style="text-align:right;"> 21 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Akuntansi Syariah </td>
   <td style="text-align:right;"> 19 </td>
  </tr>
</tbody>
<tfoot><tr><td style="padding: 0; " colspan="100%">
<span style="font-style: italic;">Catatan:</span> <sup></sup> Menampilkan 6 dari 32 program studi</td></tr></tfoot>
</table>

Berikut adalah visualisasi menggunakan grafik batang biasa:

<div class="figure" style="text-align: center">
<img src="figures/fig-bar-prodi-1.png" alt="Grafik batang program studi mahasiswa UINRIL" width="85%" />
<p class="caption">(\#fig:fig-bar-prodi)Grafik batang program studi mahasiswa UINRIL</p>
</div>

Sekarang bandingkan dengan grafik lollipop:

<div class="figure" style="text-align: center">
<img src="figures/fig-lollipop-prodi-1.png" alt="Grafik lollipop program studi mahasiswa UINRIL" width="85%" />
<p class="caption">(\#fig:fig-lollipop-prodi)Grafik lollipop program studi mahasiswa UINRIL</p>
</div>

**Perbandingan:** Pada grafik lollipop, setiap kategori lebih mudah dibedakan karena hanya tiang tipis dan titik yang mewakili nilai, sehingga menghindari efek visual yang berlebihan (Moiré). Grafik lollipop sangat cocok untuk dataset dengan banyak kategori seperti ini, karena lebih ringkas dan tetap informatif. Sementara grafik batang biasa terlihat lebih padat dan dapat menimbulkan kesulitan dalam membaca data ketika batang-batangnya berdekatan.

:::

#### Grafik *Treemap*

Secara fungsi, treemap dan *stacked bar chart* sangat mirip karena keduanya menunjukkan distribusi frekuensi objek berdasarkan kategori variabelnya. Jika *stacked chart* memakai panjang segmen pada batang untuk menunjukkan proporsi, *treemap* menggunakan luas area persegi panjang. Frekuensinya diperlihatkan oleh **luas persegi masing-masing kategori**.

Proses pembuatannya sama persis seperti dengan grafik batang bertumpuk.

::: rmdkasus

#### Studi Kasus: Membuat Treemap Moda Transportasi {.unnumbered}

Treemap menggunakan luas area persegi untuk menunjukkan proporsi kategori. Seperti pada grafik batang bertumpuk, kita mulai dari tabel distribusi frekuensi dua variabel.

<table class="table table-striped table-hover table-condensed" style="width: auto !important; margin-left: auto; margin-right: auto;">
<caption>(\#tab:tab-treemap-data)Distribusi Frekuensi Moda Transportasi berdasarkan Jenis Kelamin untuk Treemap</caption>
 <thead>
  <tr>
   <th style="text-align:left;"> Jenis Kelamin </th>
   <th style="text-align:left;"> Moda Transportasi </th>
   <th style="text-align:right;"> Frekuensi </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> Laki-laki </td>
   <td style="text-align:left;"> Berjalan kaki </td>
   <td style="text-align:right;"> 3 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Laki-laki </td>
   <td style="text-align:left;"> Menumpang kendaraan bermotor teman/keluarga </td>
   <td style="text-align:right;"> 9 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Laki-laki </td>
   <td style="text-align:left;"> Mobil pribadi </td>
   <td style="text-align:right;"> 6 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Laki-laki </td>
   <td style="text-align:left;"> Sepeda motor pribadi </td>
   <td style="text-align:right;"> 167 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Laki-laki </td>
   <td style="text-align:left;"> Transportasi daring </td>
   <td style="text-align:right;"> 3 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Perempuan </td>
   <td style="text-align:left;"> Berjalan kaki </td>
   <td style="text-align:right;"> 35 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Perempuan </td>
   <td style="text-align:left;"> Menumpang kendaraan bermotor teman/keluarga </td>
   <td style="text-align:right;"> 18 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Perempuan </td>
   <td style="text-align:left;"> Mobil pribadi </td>
   <td style="text-align:right;"> 9 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Perempuan </td>
   <td style="text-align:left;"> Sepeda motor pribadi </td>
   <td style="text-align:right;"> 123 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Perempuan </td>
   <td style="text-align:left;"> Transportasi daring </td>
   <td style="text-align:right;"> 27 </td>
  </tr>
</tbody>
</table>

Dari tabel distribusi frekuensi tersebut, kita dapat membuat treemap:

<div class="figure" style="text-align: center">
<img src="figures/fig-treemap-moda-1.png" alt="Treemap moda transportasi berdasarkan jenis kelamin" width="80%" />
<p class="caption">(\#fig:fig-treemap-moda)Treemap moda transportasi berdasarkan jenis kelamin</p>
</div>

**Interpretasi:** Treemap menunjukkan proporsi penggunaan moda transportasi dengan jelas melalui luas area. Area terbesar dimiliki oleh sepeda motor, menunjukkan dominasinya sebagai moda transportasi utama. Di dalam setiap moda, terdapat sub-area yang menunjukkan pembagian berdasarkan jenis kelamin. Visualisasi ini memudahkan kita untuk membandingkan proporsi secara langsung tanpa perlu membaca angka.

:::

#### Grafik Pai/Donat *(Pie/Donut Chart)*

Grafik jenis ini juga sering digunakan untuk visualisasi variabel kategoris. Perbedaan dengan grafik batang adalah frekuensi tiap kategori tidak diperlihatkan dengan sumbu tegak, tetapi besar juring (sektor) lingkaran.

Proses pembuatannya sama seperti pembuatan grafik batang yang ditunjukkan pada kasus di \@ref(materi-bar-chart), hanya saja jumlah kategori menjadi jumlah sektor, sementara frekuensinya menjadi ukuran sektor.

::: rmdkasus

#### Studi Kasus: Membuat Grafik Pai dan Donat {.unnumbered}

Grafik pai dan donat menggunakan juring lingkaran untuk menunjukkan proporsi kategori. Prosesnya sama dengan grafik batang, dimulai dari tabel distribusi frekuensi.

<table class="table table-striped table-hover table-condensed" style="width: auto !important; margin-left: auto; margin-right: auto;">
<caption>(\#tab:tab-pie-data)Distribusi Frekuensi Moda Transportasi untuk Grafik Pai</caption>
 <thead>
  <tr>
   <th style="text-align:left;"> Moda Transportasi </th>
   <th style="text-align:right;"> Frekuensi </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> Berjalan kaki </td>
   <td style="text-align:right;"> 38 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Menumpang kendaraan bermotor teman/keluarga </td>
   <td style="text-align:right;"> 27 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Mobil pribadi </td>
   <td style="text-align:right;"> 15 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Sepeda motor pribadi </td>
   <td style="text-align:right;"> 290 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Transportasi daring </td>
   <td style="text-align:right;"> 30 </td>
  </tr>
</tbody>
</table>

Dari tabel distribusi frekuensi, kita dapat membuat grafik pai (*pie chart*):

<div class="figure" style="text-align: center">
<img src="figures/fig-pie-moda-1.png" alt="Grafik pai moda transportasi mahasiswa UINRIL" width="70%" />
<p class="caption">(\#fig:fig-pie-moda)Grafik pai moda transportasi mahasiswa UINRIL</p>
</div>

Untuk membuat grafik donat (*donut chart*), kita mengubah jenis kategori menjadi juring-juring lingkaran dan sudunya ditentukan dari proporsi frekuensi. Prosesnya sama dengan grafik pai, hanya saja kita di tengahnya ada ruang kosong yang dapat digunakan untuk informasi tambahan.

<div class="figure" style="text-align: center">
<img src="figures/fig-donut-moda-1.png" alt="Grafik donat moda transportasi mahasiswa UINRIL" width="70%" />
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

#### Studi Kasus: Membuat Histogram Biaya Perjalanan {.unnumbered}

Histogram menunjukkan distribusi nilai numerik dengan mengelompokkannya ke dalam interval (bin). Mari kita visualisasikan biaya perjalanan mahasiswa ITERA.

<table class="table table-striped table-hover table-condensed" style="width: auto !important; margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-4-hist-biaya-prep)Statistik Deskriptif Biaya Perjalanan Mahasiswa ITERA (dalam ribuan rupiah)</caption>
 <thead>
  <tr>
   <th style="text-align:left;"> Statistik </th>
   <th style="text-align:right;"> Nilai (Rp ribu) </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> Min </td>
   <td style="text-align:right;"> 0.00 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Q1 </td>
   <td style="text-align:right;"> 20000.00 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Median </td>
   <td style="text-align:right;"> 30000.00 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Mean </td>
   <td style="text-align:right;"> 38665.89 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Q3 </td>
   <td style="text-align:right;"> 45000.00 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Max </td>
   <td style="text-align:right;"> 400000.00 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:right;"> 0.00 </td>
  </tr>
</tbody>
</table>

Sebelum membuat histogram, kita perlu mengelompokkan nilai-nilai ke dalam interval (*bin*). Perangkat lunak pengolah data statistik, contohnya bahasa pemrograman R, melakukan ini secara otomatis. Berikut adalah contoh pembuatan histogram dengan pengaturan *bin* otomatis:

<div class="figure" style="text-align: center">
<img src="figures/fig-hist-biaya-auto-1.png" alt="Histogram biaya perjalanan (bin otomatis) dalam ribuan rupiah" width="75%" />
<p class="caption">(\#fig:fig-hist-biaya-auto)Histogram biaya perjalanan (bin otomatis) dalam ribuan rupiah</p>
</div>

Kita juga dapat mengatur jumlah bin secara manual untuk melihat distribusi dengan lebih detail:

<div class="figure" style="text-align: center">
<img src="figures/fig-hist-biaya-manual-1.png" alt="Histogram biaya perjalanan (bin manual) dalam ribuan rupiah" width="75%" />
<p class="caption">(\#fig:fig-hist-biaya-manual)Histogram biaya perjalanan (bin manual) dalam ribuan rupiah</p>
</div>

Untuk lebih memahami proses *binning*, mari kita buat tabel frekuensi manual:

<table class="table table-striped table-hover table-condensed" style="width: auto !important; margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-4-tab-freq-manual)Tabel Frekuensi Biaya Perjalanan dalam Ribuan Rupiah (6 Interval Pertama)</caption>
 <thead>
  <tr>
   <th style="text-align:left;"> Interval Biaya (Rp ribu) </th>
   <th style="text-align:right;"> Frekuensi </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> [0,4.44e+04] </td>
   <td style="text-align:right;"> 318 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> (4.44e+04,8.89e+04] </td>
   <td style="text-align:right;"> 80 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> (8.89e+04,1.33e+05] </td>
   <td style="text-align:right;"> 13 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> (1.33e+05,1.78e+05] </td>
   <td style="text-align:right;"> 7 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> (1.78e+05,2.22e+05] </td>
   <td style="text-align:right;"> 7 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> (2.22e+05,2.67e+05] </td>
   <td style="text-align:right;"> 1 </td>
  </tr>
</tbody>
</table>

**Interpretasi:** Histogram menunjukkan bahwa sebagian besar mahasiswa ITERA memiliki biaya perjalanan dalam rentang rendah hingga menengah, dengan konsentrasi terbesar pada rentang 0-50 ribu rupiah (perhatikan bahwa nilai biaya sudah dalam satuan ribu rupiah). Distribusi menunjukkan pola miring ke kanan (*right-skewed*), yang berarti terdapat beberapa mahasiswa dengan biaya perjalanan yang sangat tinggi. Informasi ini penting untuk perencanaan transportasi kampus, misalnya dalam menentukan subsidi atau rute angkutan kampus.

:::


#### *Boxplot*

Boxplot adalah grafik berbentuk kotak dan garis yang menampilkan ukuran penyebaran suatu variabel numerik secara grafis (Gambar \@ref(fig:jenis-boxplot)). Sebagaimana yang ditunjukkan oleh gambar tersebut, kotak dan garis pada boxplot dapat berjumlah satu atau lebih. Satu kotak dan garis menandakan hanya ada satu kategori objek dengan variabel numerik yang ditampilkan.

Sementara itu, jika variabel numerik tersebut dikategorikan lagi berdasarkan suatu variabel kategoris, maka jumlah kotak dan garisnya bisa lebih dari satu dan berjumlah sesuai dengan jumlah kategori objeknya.


<div class="figure" style="text-align: center">
<img src="figures/jenis-boxplot.png" alt="*Boxplot* yang terdiri atas dua kategori objek: A dan B" width="40%" />
<p class="caption">(\#fig:jenis-boxplot)*Boxplot* yang terdiri atas dua kategori objek: A dan B</p>
</div>

Setiap elemen pada boxplot memiliki makna ukuran penyebaran. Ini dijelaskan pada kasus berikut.

::: rmdkasus

#### Studi Kasus: Membuat Boxplot Biaya Perjalanan Mahasiswa {.unnumbered}

Boxplot menampilkan ukuran penyebaran data numerik secara grafis. Mari kita buat boxplot untuk menganalisis distribusi biaya perjalanan mahasiswa dari berbagai universitas.

<table class="table table-striped table-hover table-condensed" style="width: auto !important; margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-4-boxplot-prep)Statistik Deskriptif Biaya Perjalanan Gabungan (UINRIL &amp; UNILA)</caption>
 <thead>
  <tr>
   <th style="text-align:left;"> Statistik </th>
   <th style="text-align:right;"> Nilai </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> Min </td>
   <td style="text-align:right;"> 0.00 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Q1 </td>
   <td style="text-align:right;"> 30.00 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Median </td>
   <td style="text-align:right;"> 50.00 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Mean </td>
   <td style="text-align:right;"> 56.54 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Q3 </td>
   <td style="text-align:right;"> 65.00 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> Max </td>
   <td style="text-align:right;"> 400.00 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> NA </td>
   <td style="text-align:right;"> 0.00 </td>
  </tr>
</tbody>
</table>

Mari kita buat boxplot tunggal untuk biaya perjalanan UINRIL terlebih dahulu:

<div class="figure" style="text-align: center">
<img src="figures/fig-boxplot-single-1.png" alt="Boxplot biaya perjalanan mahasiswa UINRIL" width="60%" />
<p class="caption">(\#fig:fig-boxplot-single)Boxplot biaya perjalanan mahasiswa UINRIL</p>
</div>

Sekarang mari kita buat boxplot ganda untuk membandingkan distribusi biaya perjalanan antar kampus:

<div class="figure" style="text-align: center">
<img src="figures/fig-boxplot-multiple-1.png" alt="Boxplot biaya perjalanan mahasiswa berdasarkan kampus" width="75%" />
<p class="caption">(\#fig:fig-boxplot-multiple)Boxplot biaya perjalanan mahasiswa berdasarkan kampus</p>
</div>

**Penjelasan elemen boxplot:**

- **Garis tengah kotak (median/Q2)**: Nilai tengah data yang membagi data menjadi dua bagian sama besar
- **Kotak bagian bawah (Q1)**: Kuartil pertama, 25% data berada di bawah nilai ini
- **Kotak bagian atas (Q3)**: Kuartil ketiga, 75% data berada di bawah nilai ini
- **Tinggi kotak (IQR)**: Jarak interkuartil, menunjukkan rentang 50% data tengah
- ***Whiskers* (garis atas dan bawah)**: Menunjukkan rentang data yang masih dalam batas normal (1,5 × IQR)
- **Titik-titik di luar *whiskers***: *Outlier* atau pencilan, yakni nilai-nilai ekstrem yang jauh dari sebagian besar data

**Interpretasi:** Dari boxplot ganda terlihat bahwa distribusi biaya perjalanan mahasiswa UNILA memiliki median yang sedikit lebih tinggi dibandingkan UINRIL. Rentang interkuartil (tinggi kotak) UNILA juga lebih besar, menunjukkan variasi biaya perjalanan yang lebih beragam. Terdapat beberapa outlier pada kedua kampus yang menunjukkan ada mahasiswa dengan biaya perjalanan yang jauh lebih tinggi dari mayoritas. Informasi ini berguna untuk perencanaan fasilitas kampus seperti kantin atau transportasi yang disesuaikan dengan daya beli mahasiswa.

:::

#### Grafik Garis *(Line Plot)* dan Area *(Area Plot)*

Grafik ini memetakan nilai variabel angka yang masuk akal bisa diurutkan, yakni biasanya yang berupa deret waktu (time series). Garis menghubungkan masing-masing titik nilai pada tiap-tiap posisi untuk menegaskan perubahan nilainya. Gambar \@ref(fig:line-plot-area-plot) berikut mengilustrasikan data terstruktur yang membentuk line atau area plot.

<div class="figure" style="text-align: center">
<img src="figures/diagram-garis-area.png" alt="Ilustrasi line plot dan area plot serta data terstruktur yang membentuknya" width="3745" />
<p class="caption">(\#fig:line-plot-area-plot)Ilustrasi line plot dan area plot serta data terstruktur yang membentuknya</p>
</div>

Area plot secara prinsip sama saja dengan line plot, hanya saja ruang di bawah garisnya diisi dengan warna yang sama dengan garis. Area plot biasanya digunakan untuk data numerik dengan dimensi waktu yang terdiri atas kategori-kategori seperti yang ditunjukkan Gambar \@ref(fig:fig-area-plot-multi).

<div class="figure" style="text-align: center">
<img src="figures/area-plot-lebih-dari-1.png" alt="Ilustrasi area plot dengan tiga variabel" width="60%" />
<p class="caption">(\#fig:fig-area-plot-multi)Ilustrasi area plot dengan tiga variabel</p>
</div>

#### Grafik Pencar *(Scatterplot)*

*Scatterplot* dapat memperlihatkan pemetaan nilai dua variabel numerik yang berkaitan. Sumbu tegak dan datar menunjukkan nilai-nilai dua variabel tersebut sementara tiap titik dibentuk dari perpotongan nilai dari kedua variabel untuk tiap-tiap objek.

::: rmdkasus

#### Studi Kasus: Membuat *Scatterplot* Hubungan Biaya Perjalanan dan Jarak Tempuh {.unnumbered}

*Scatterplot* memperlihatkan hubungan antara dua variabel numerik. Setiap titik mewakili satu observasi dengan nilai pada sumbu X dan Y. Mari kita analisis hubungan antara biaya perjalanan dan jarak tempuh mahasiswa ITERA.

<table class="table table-striped table-hover table-condensed" style="width: auto !important; margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-4-scatter-prep)Contoh Data Biaya Perjalanan dan Jarak Tempuh dalam Ribuan Rupiah (10 Observasi Pertama)</caption>
 <thead>
  <tr>
   <th style="text-align:right;"> Biaya Perjalanan (Rp ribu) </th>
   <th style="text-align:right;"> Jarak Tempuh (km) </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:right;"> 10000 </td>
   <td style="text-align:right;"> 6.69 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 21000 </td>
   <td style="text-align:right;"> 2.82 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 40000 </td>
   <td style="text-align:right;"> 5.17 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 30000 </td>
   <td style="text-align:right;"> 6.95 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 25000 </td>
   <td style="text-align:right;"> 5.57 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 40000 </td>
   <td style="text-align:right;"> 4.75 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 30000 </td>
   <td style="text-align:right;"> 8.27 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 0 </td>
   <td style="text-align:right;"> 3.70 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 100000 </td>
   <td style="text-align:right;"> 3.77 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 30000 </td>
   <td style="text-align:right;"> 2.08 </td>
  </tr>
</tbody>
</table>

Tabel di atas menunjukkan pasangan nilai untuk setiap mahasiswa. Kolom pertama (`biaya.dalam.sepekan`) akan menjadi sumbu X, dan kolom kedua (`jarak`) menjadi sumbu Y. Setiap baris akan menjadi satu titik pada scatterplot.

Mari kita buat *scatterplot* menggunakan `ggplot2`:

<div class="figure" style="text-align: center">
<img src="figures/fig-scatter-ggplot-1.png" alt="Scatterplot jarak tempuh vs biaya perjalanan dalam ribuan rupiah" width="75%" />
<p class="caption">(\#fig:fig-scatter-ggplot)Scatterplot jarak tempuh vs biaya perjalanan dalam ribuan rupiah</p>
</div>

**Hubungan data terstruktur dengan scatterplot:**

- Setiap **baris** dalam tabel data menjadi **satu titik** pada grafik
- Nilai **kolom pertama** (biaya perjalanan) menentukan **posisi horizontal (X)** titik
- Nilai **kolom kedua** (jarak tempuh) menentukan **posisi vertikal (Y)** titik
- Titik di koordinat (50, 10) artinya mahasiswa tersebut memiliki biaya perjalanan 50 ribu rupiah (nilai sudah dalam satuan ribu) dan jarak tempuh 10 km

**Interpretasi:** Scatterplot menunjukkan adanya hubungan positif antara biaya perjalanan (dalam ribuan rupiah) dan jarak tempuh mahasiswa ITERA. Mahasiswa yang tinggal lebih jauh dari kampus cenderung memiliki biaya perjalanan yang lebih tinggi, yang masuk akal karena mereka memerlukan lebih banyak bahan bakar atau biaya transportasi umum. Garis tren (garis putus-putus merah) menunjukkan arah umum hubungan ini. Informasi ini berguna untuk perencanaan kebijakan kampus terkait subsidi transportasi yang mungkin lebih diprioritaskan untuk mahasiswa yang tinggal jauh dari kampus.

:::



## Penggunaan dan Interpretasi Diagram

Memilih diagram yang tepat adalah kunci dalam menghasilkan analisis yang baik dan tajam. Setiap diagram memiliki karakteristik yang berbeda satu sama lain, sehingga penggunaannya harus disesuaikan dengan jenis variabel dan pesan yang ingin ditekankan.

Untuk memilih visualisasi yang paling efektif, mulailah dengan menjawab beberapa pertanyaan mendasar berikut:

* **Apa tujuan utama Anda?** Apakah Anda ingin menunjukkan perbandingan, distribusi, komposisi, atau hubungan antarvariabel?
* **Ada berapa variabel yang ingin Anda tampilkan?** Apakah hanya satu, dua, atau lebih?
* **Apa jenis nilai dan tingkat pengukuran dari variabel-variabel tersebut?** Apakah kategorikal (nominal, ordinal) atau numerik (metrik)?

Jawaban dari pertanyaan-pertanyaan ini akan menuntun Anda pada pilihan diagram yang paling sesuai.

### Pemilihan Diagram Berdasarkan Tujuan

Secara umum, tujuan visualisasi data dalam statistik dapat dikelompokkan menjadi beberapa empat kategori, yang masing-masing memiliki jenis diagram yang cocok. Berikut adalan penjelasan keempat kategori tersebut.

1. **Menampilkan Distribusi Frekuensi**. Ini paling cocok untuk variabel kategorikal (nominal atau ordinal). Pilihan utamanya adalah **grafik batang** atau **grafik lollipop**, di mana panjang atau tinggi batang merepresentasikan jumlah atau frekuensi setiap kategori.
2. **Menampilkan Komposisi**. Ketika Anda ingin menunjukkan bagian-bagian dari suatu keseluruhan, Anda sedang menampilkan komposisi. **Grafik pai** atau **donat** dapat dipakai untuk tujuan ini.
3. **Menampilkan Distribusi Nilai Numerik**. Ketika Anda ingin menampilkan distribusi nilai numerik, Anda dapat menggunakan **histogram** atau **boxplot**. Untuk menampilkan ukuran-ukuran statistik penyebaran dengan lebih tegas, Anda dapat menggunakan *boxplot*.
4. **Menampilkan Hubungan Antar Variabel**. Ketika Anda ingin menunjukkan hubungan antar variabel, Anda dapat menggunakan **scatterplot** atau **line plot**.

### Pemilihan Diagram Berdasarkan Jumlah Variabel

Pemilihan diagram juga dapat Anda lakukan dengan melihat jumlah variabel yang ingin Anda tampilkan. Jika hanya satu variabel, Anda dapat menggunakan **grafik batang** atau **grafik lollipop**. Jika ada dua variabel, Anda dapat menggunakan **scatterplot** atau **line plot**.

Grafik batang juga dapat digunakan untuk menampilkan distribusi frekuensi dari dua variabel kategorikal dengan menggunakan **grafik batang bertumpuk** atau **grafik batang berjejer**.


### Pemilihan Diagram Berdasarkan Tingkat Pengukuran Variabel

Secara umum, diagram yang digunakan untuk menampilkan data kategorikal adalah **grafik batang** atau **grafik lollipop**, sedangkan diagram yang digunakan untuk menampilkan data numerik adalah **histogram** atau **boxplot**.

Beberapa contoh pertimbangan dalam memilih diagram berdasarkan tingkat pengukuran variabel adalah sebagai berikut:

1. **Data Ordinal**. Untuk data ordinal, Anda sangat disarankan untuk menggunakan **grafik batang** atau **grafik lollipop** yang diurutkan berdasarkan urutan kategori.
2. **Data Metrik**. Histogram, *boxplot*, dan *scatterplot* adalah pilihan standar untuk visualisasi.

Ringkasan dari pemilihan diagram berdasarkan tujuan, jumlah variabel, dan tingkat pengukuran variabel tersebut dapat dilihat pada Gambar \@ref(fig:simpulan-memilih-visualisasi) berikut yang diambil dari @Crazyegg_2017.

<div class="figure" style="text-align: center">
<img src="images/CrazyEgg-Diagram.webp" alt="Panduan memilih jenis visualisasi"  />
<p class="caption">(\#fig:simpulan-memilih-visualisasi)Panduan memilih jenis visualisasi</p>
</div>

Silakan kerjakan soal-soal evaluasi berikut terkait visualisasi data kuantitatif untuk menguji pemahaman Anda terhadap penjelasan-penjelasan yang telah Anda pelajari.

::: rmdexercise

## Soal Evaluasi 5 {.unnumbered}

Perhatikan cuplikan data hasil survei mahasiswa berikut ini:

<table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:bab-4-eval-5-preview)Cuplikan data survei mahasiswa</caption>
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
<caption>(\#tab:bab-4-eval-5-metadata)Metadata variabel survei mahasiswa</caption>
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

1. Analisislah tiap-tiap variabel berdasarkan tingkat pengukuran variabelnya untuk menentukan jenis grafik apa yang bisa digunakan untuk memvisualkan variabel-variabel tersebut! [STP-3.1]{.capaian}

  <table class="table table-striped table-hover" style="margin-left: auto; margin-right: auto;">
   <thead>
    <tr>
     <th style="text-align:center;"> # </th>
     <th style="text-align:center;"> Nama Variabel </th>
     <th style="text-align:center;"> Tingkat Pengukuran </th>
     <th style="text-align:center;"> Jenis Grafik yang Bisa Digunakan (bisa lebih dari 1) </th>
    </tr>
   </thead>
  <tbody>
    <tr>
     <td style="text-align:center;"> a </td>
     <td style="text-align:center;"> `Usia` </td>
     <td style="text-align:center;"> ... </td>
     <td style="text-align:center;"> ... </td>
    </tr>
    <tr>
     <td style="text-align:center;"> b </td>
     <td style="text-align:center;"> `Fakultas` </td>
     <td style="text-align:center;"> ... </td>
     <td style="text-align:center;"> ... </td>
    </tr>
    <tr>
     <td style="text-align:center;"> c </td>
     <td style="text-align:center;"> `UangSaku` </td>
     <td style="text-align:center;"> ... </td>
     <td style="text-align:center;"> ... </td>
    </tr>
    <tr>
     <td style="text-align:center;"> d </td>
     <td style="text-align:center;"> `ThnMsk` </td>
     <td style="text-align:center;"> ... </td>
     <td style="text-align:center;"> ... </td>
    </tr>
    <tr>
     <td style="text-align:center;"> e </td>
     <td style="text-align:center;"> `Jarak` </td>
     <td style="text-align:center;"> ... </td>
     <td style="text-align:center;"> ... </td>
    </tr>
  </tbody>
  </table>

2. Tentukan jenis grafik yang sesuai untuk beberapa tujuan visualisasi berikut [STP-3.2]{.capaian}:
    a. menampilkan distribusi frekuensi dari variabel `Fakultas`
    a. menampilkan distribusi frekuensi mahasiswa per `ThnMsk` dan `Fakultas`
    a. memperlihatkan median, kuartil atas, dan kuartil bawah variabel `Usia` 
    a. memperlihatkan sebaran mahasiswa berdasarkan `Jarak` tempat tinggal mereka

3. Analisislah mengapa grafik histogram tidak bisa digunakan untuk menampilkan distribusi frekuensi dari variabel `Fakultas` dan `UangSaku`! [STP-3.4]{.capaian}

:::




<!--chapter:end:04-visualisasi-data.Rmd-->

# Pengantar Analisis Statistik Inferensial

::: rmdcapaian
## Capaian Pembelajaran {.unnumbered}

Setelah mempelajari bab ini, Anda diharapkan:

1.  mampu memilih jenis-jenis pengambilan sampel dalam statistik untuk sebuah kasus. [STP-4.1]{.capaian}
2.  mampu menjelaskan hasil perhitungan probabilitas dari suatu nilai sampel dalam distribusi statistik sampel menggunakan *standard error*. [STP-4.2]{.capaian}
:::

## Konsep Dasar Statistika Inferensial

Statistika inferensial adalah cabang statistika yang mempelajari **penarikan kesimpulan tentang populasi berdasarkan data dari sampel**. Konsep-konsep dasar yang perlu dipahami dalam analisis statistika ini meliputi **perbedaan antara populasi dan sampel**, **teknik pengambilan sampel**, **distribusi sampel dan distribusi statistik sampel**, serta prinsip-prinsip terkait distribusi statistik, yakni beberapa di antaranya adalah **teorema limit sentral** dan **distribusi normal**.

Setelah memahami konsep-konsep tersebut, kita dapat melanjutkan pembahasan ke penarikan kesimpulan karakteristik populasi dari hasil sampel, yang mencakup pembuatan **estimasi parameter** dan **pengujian hipotesis** yang menyatakan karakteristik seluruh populasi dari hasil sampel.

## Populasi vs. Sampel

**Populasi** adalah seluruh kelompok objek (baik orang, benda, maupun kejadian) yang menjadi target penelitian kita. Ukuran statistik deskriptif dari populasi, seperti rata-rata ($\mu$) atau simpangan baku ($\sigma$), disebut **parameter**. Parameter inilah yang sebenarnya ingin diketahui oleh peneliti. Namun, karena jumlah populasi biasanya sangat besar, sering kali kita tidak mungkin mengukur seluruh anggota populasi secara langsung.

Sebaliknya, **sampel** adalah sebagian kecil dari populasi yang kita ambil untuk diamati. Sampel yang baik harus bisa mewakili sifat keseluruhan populasinya **(representatif)**. Ukuran statistik deskriptif dari sampel inilah yang disebut **statistik** (seperti rata-rata $\bar{x}$ atau simpangan baku $s$). Nilai statistik ini digunakan untuk menduga nilai parameter populasi.

**Mengapa kita mengambil sampel?** Alasan utamanya adalah **efisiensi** dan **kelayakan**. Menurut @saunders2023, melakukan sensus terhadap populasi yang besar sering kali tidak praktis karena membutuhkan **biaya** yang sangat mahal dan **waktu** yang lama. Selain itu, @devaus2014surveys menekankan bahwa sensus tidak menjamin data yang lebih akurat. Sebaliknya, sampel yang dipilih dengan hati-hati memungkinkan peneliti untuk mengontrol kualitas data dengan lebih ketat (misalnya melalui pelatihan pewawancara yang lebih intensif), sehingga justru dapat menghasilkan tingkat **akurasi** yang lebih tinggi dibandingkan sensus yang rentan terhadap *non-sampling error*.

::: rmdkasus
### Studi Kasus: Populasi vs. Sampel {.unnumbered}

Kita ingin menganalisis data karakteristik perjalanan mahasiswa di ITERA. Oleh karena itu, kita mengumpulkan data terstruktur yang mengukur variabel-variabel terkait pola perjalanan mahasiswa di ITERA.

Berdasarkan data tahun 2023 pertengahan, tercatat sebanyak **18.877** mahasiswa aktif di ITERA. Jika kita mengumpulkan seluruh mahasiswa aktif dengan jumlah tersebut, maka kita akan mendapatkan data populasi. Namun, karena jumlah mahasiswa yang sangat banyak, kita tidak mungkin mengumpulkan data seluruh mahasiswa aktif di ITERA. Oleh karena itu, kita mengumpulkan data sebagian mahasiswa aktif di ITERA, yaitu sebanyak **428** mahasiswa.

<div class="figure" style="text-align: center">
<img src="images/populasi_vs_sampel_itera.png" alt="Ilustrasi Perbandingan Populasi Mahasiswa ITERA dan Sampel" width="80%" />
<p class="caption">(\#fig:05-inferensia-populasi-sampel-viz)Ilustrasi Perbandingan Populasi Mahasiswa ITERA dan Sampel</p>
</div>

Keputusan mengambil 428 sampel ini didasarkan pada pertimbangan **efisiensi** dan **akurasi** yang telah kita bahas sebelumnya. Melakukan sensus terhadap 18.877 mahasiswa tentu membutuhkan biaya dan waktu yang sangat besar. Selain itu, dengan jumlah yang jauh lebih sedikit, peneliti dapat lebih fokus menjamin kualitas data (misalnya meminimalisir kesalahan input atau bias wawancara), sehingga data sampel ini diharapkan memiliki kualitas yang lebih baik daripada sensus yang dilakukan secara terburu-buru.
:::

## Teknik-Teknik Pengambilan Sampel *(Sampling Techniques)*

Teknik pengambilan sampel bertujuan memastikan bahwa sampel yang dipilih benar-benar dapat mewakili populasinya. @healey2021statistics menekankan prinsip EPSEM (*Equal Probability of Selection Method*), yakni prinsip yang menekankan bahwa **setiap anggota populasi memiliki kesempatan yang sama untuk dipilih**. Hal ini penting untuk menghasilkan sampel yang representatif.

Teknik probabilitas adalah teknik yang menggunakan prinsip EPSEM. Untuk dapat menggunakannya, kita harus memiliki **kerangka sampel**. Kerangka sampel adalah daftar seluruh anggota populasi yang akan menjadi acuan kita untuk memilih sampel nantinya. Ada empat jenis teknik yang termasuk ke dalam teknik pengambilan sampel probabilitas [@tjokropandojo2021pengantar, @saunders2023]: *simple random sampling*, *systematic sampling*, *stratified sampling*, dan *multi-stage cluster sampling*.

::: rmdkasus
### Studi Kasus: Pengambilan Sampel dengan Populasi Kecil {.unnumbered}

Untuk mempermudah pemahaman, bayangkan kita memiliki **populasi kecil** yang terdiri dari **16 orang** saja. Setiap orang memiliki atribut **Kelompok** (A/B/C/D) dan tinggal di **Blok** tertentu (1/2/3/4).

Berikut adalah data lengkap ke-16 orang tersebut:


Table: (\#tab:05-inferensia-setup-toy-populasi)Daftar Lengkap Populasi (N=16)

| ID| Jarak|Kelompok |Blok   | ID| Jarak|Kelompok |Blok   |
|--:|-----:|:--------|:------|--:|-----:|:--------|:------|
|  1|   2.5|A        |Blok 1 |  9|  10.5|A        |Blok 3 |
|  2|   1.0|B        |Blok 1 | 10|  11.2|B        |Blok 3 |
|  3|   5.2|C        |Blok 1 | 11|   9.8|C        |Blok 3 |
|  4|   3.8|D        |Blok 1 | 12|   8.5|D        |Blok 3 |
|  5|   0.5|A        |Blok 2 | 13|  15.0|A        |Blok 4 |
|  6|   1.2|B        |Blok 2 | 14|  14.2|B        |Blok 4 |
|  7|   4.0|C        |Blok 2 | 15|  16.5|C        |Blok 4 |
|  8|   6.1|D        |Blok 2 | 16|  13.8|D        |Blok 4 |

Mari kita terapkan keempat teknik *sampling* untuk memilih sampel dari 16 orang ini.
:::

### *Simple Random Sampling*

*Simple random sampling* merupakan teknik paling dasar dalam pengambilan sampel probabilistik. Kita mengambil secara acak nomor yang merepresentasikan nomor urut sampel. Ini memungkinkan setiap anggota populasi memiliki peluang yang sama untuk dipilih. Pemilihan anggota sampel secara acak ini dapat dilakukan dengan bantuan sistem eksternal dari peneliti, misalnya melalui tabel angka acak atau program komputer yang menghasilkan angka acak (*random number generator*) (Gambar \@ref(fig:05-inferensia-img-srs)).

<div class="figure" style="text-align: center">
<img src="images/bab-5-srs.png" alt="Ilustrasi Simple Random Sampling" width="80%" />
<p class="caption">(\#fig:05-inferensia-img-srs)Ilustrasi Simple Random Sampling</p>
</div>

::: rmdnote
### Catatan: Miskonsepsi tentang Istilah Random {.unnumbered}

Banyak yang salah kaprah dengan istilah *random* pada *simple random sampling*. Keacakan (*random*) di sini maksudnya bukan asal mengambil sampel secara acak **langsung di dunia nyata**, akan tetapi kita mengambil sampel tersebut dari **sebuah kerangka sampel**, elemen vital dalam teknik *sampling* probabilitas.
:::

::: rmdkasus
### Studi Kasus: *Simple Random Sampling* dengan Populasi Kecil {.unnumbered}

Misalkan kita menggunakan *random number generator* yang ada di hampir semua program *spreadsheet* untuk memilih 4 sampel. *Hasilnya adalah 4 orang yang terpilih secara acak tanpa pola tertentu.*


Table: (\#tab:05-inferensia-toy-srs)Hasil SRS (n=4)

| ID| Jarak|Kelompok |Blok   |
|--:|-----:|:--------|:------|
|  9|  10.5|A        |Blok 3 |
| 16|  13.8|D        |Blok 4 |
| 14|  14.2|B        |Blok 4 |
|  7|   4.0|C        |Blok 2 |
:::

### *Systematic Random Sampling*

Berbeda dengan *simple random sampling*, *systematic random sampling* menggunakan sistem pemilihan berdasarkan interval tertentu. Langkah pertama adalah menentukan angka acak awal, kemudian memilih sampel berikutnya berdasarkan kelipatan dari angka tersebut.

<div class="figure" style="text-align: center">
<img src="images/bab-5-systematic.png" alt="Ilustrasi Systematic Random Sampling" width="60%" />
<p class="caption">(\#fig:05-inferensia-img-systematic)Ilustrasi Systematic Random Sampling</p>
</div>

::: rmdkasus
### Studi Kasus: *Systematic Sampling* dengan Populasi Kecil {.unnumbered}

Kita ingin mengambil sampel dengan interval **k=4**. Kita urutkan berdasarkan ID, lalu ambil setiap kelipatan 4 (4, 8, 12, 16).


Table: (\#tab:05-inferensia-toy-systematic)Hasil Systematic Sampling (Interval k=4)

| ID| Jarak|Kelompok |Blok   |
|--:|-----:|:--------|:------|
|  4|   3.8|D        |Blok 1 |
|  8|   6.1|D        |Blok 2 |
| 12|   8.5|D        |Blok 3 |
| 16|  13.8|D        |Blok 4 |

*Perhatikan pola ID yang terpilih selalu berjarak 4 angka.*
:::

### *Stratified Random Sampling*

Dalam beberapa kasus, populasi terdiri atas kelompok-kelompok, disebut **strata**, yang memiliki karakteristik yang sama didalamnya, misalnya jumlah anggota rumah tangga, tingkat pendidikan, atau status sosial ekonomi. Agar setiap kelompok terwakili, digunakanlah teknik *stratified random sampling*. Caranya adalah dengan membagi populasi ke dalam beberapa strata sesuai karakteristik yang relevan, kemudian mengambil sampel secara proporsional dari setiap strata.

<div class="figure" style="text-align: center">
<img src="images/bab-5-stratified.png" alt="Ilustrasi Stratified Random Sampling" width="60%" />
<p class="caption">(\#fig:05-inferensia-img-stratified)Ilustrasi Stratified Random Sampling</p>
</div>

::: rmdkasus
### Studi Kasus: *Stratified Random Sampling* dengan Populasi Kecil {.unnumbered}

Kita ingin memastikan setiap **Kelompok** (A, B, C, D) terwakili. Kita bagi populasi menjadi 4 strata (Kelompok), lalu ambil **1 orang acak** dari setiap strata.


Table: (\#tab:05-inferensia-toy-stratified)Hasil Stratified Sampling (1 wakil per Kelompok)

| ID| Jarak|Kelompok |Blok   |
|--:|-----:|:--------|:------|
|  9|  10.5|A        |Blok 3 |
|  6|   1.2|B        |Blok 2 |
|  3|   5.2|C        |Blok 1 |
| 16|  13.8|D        |Blok 4 |

*Hasilnya menjamin ada masing-masing satu perwakilan dari Kelompok A, B, C, dan D.*
:::

### *Multi-Stage Cluster Sampling*

Teknik ini digunakan ketika kerangka sampel individu tidak tersedia, tetapi kerangka sampel untuk kelompok (klaster) tersedia. Misalnya, kita tidak punya daftar nama seluruh penduduk kota, tetapi kita punya kerangka sampel nama-nama kelurahan. Kita bisa memilih beberapa kelurahan secara acak (tahap 1), kemudian menghasilkan kerangka sampel baru dari kelurahan yang terpilih tersebut, misalnya berdasarkan batas administratif (RW/lingkungan), atau berdasarkan batas fisik, seperti blok-blok jalan (tahap 2). Dari kerangka sampel tersebut kita pilih lagi secara acak anggota kerangka sampel tersebut.

<div class="figure" style="text-align: center">
<img src="images/bab-5-msc-sampling.png" alt="Ilustrasi Multi-Stage Cluster Sampling" width="60%" />
<p class="caption">(\#fig:05-inferensia-img-cluster)Ilustrasi Multi-Stage Cluster Sampling</p>
</div>

::: rmdkasus
### Studi Kasus: *Multi-Stage Cluster Sampling* dengan Populasi Kecil {.unnumbered}

Kita ingin menghemat tenaga dengan hanya mendatangi satu lokasi saja. Kita pilih secara acak **1 Blok** (Cluster), lalu ambil **semua orang** di blok tersebut.


Table: (\#tab:05-inferensia-toy-cluster)Hasil Cluster Sampling (Terpilih: Blok 4 )

| ID| Jarak|Kelompok |Blok   |
|--:|-----:|:--------|:------|
| 13|  15.0|A        |Blok 4 |
| 14|  14.2|B        |Blok 4 |
| 15|  16.5|C        |Blok 4 |
| 16|  13.8|D        |Blok 4 |

*Kita hanya perlu mendatangi satu lokasi (Blok), tapi mendapatkan 4 responden sekaligus.*
:::

## Menentukan Ukuran Sampel

Jika selama ini kita masih berpikir bahwa ukuran sampel (jumlah sampel yang menjadi bahan data kita) ditentukan berdasarkan ukuran populasinya, maka kita salah kaprah. Menurut @devaus2014surveys, ukuran sampel menentukan galat dari perkiraan kita terhadap populasi, tapi ukuran sampel **bukan ditentukan dari ukuran populasi**. @devaus2014surveys juga menjabarkan jumlah-jumlah sampel yang berbeda untuk setiap galat dari perkiraan kita. Galat perkiraan ini disebut juga dengan *sampling error*. Tabel \@ref(tab:tabel-ukuran-sampel-sampling-error) menunjukkan ukuran sampel minimum berdasarkan *sampling error* pada varians 50/50, tingkat kepercayaan 95%. Ini akan kita pelajari lebih dalam di Bab \@ref(bab-6-estimasi-parameter).

<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">
<caption>(\#tab:tabel-ukuran-sampel-sampling-error)Ukuran sampel minimum berdasarkan *sampling error* pada varians 50/50, tingkat kepercayaan 95%</caption>
 <thead>
  <tr>
   <th style="text-align:center;"> _Sampling error_ </th>
   <th style="text-align:center;"> Ukuran Sampel Min. </th>
   <th style="text-align:center;"> _Sampling error_ </th>
   <th style="text-align:center;"> Ukuran Sampel Min. </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:center;"> 1,0% </td>
   <td style="text-align:center;"> 10.000 </td>
   <td style="text-align:center;"> 5,5% </td>
   <td style="text-align:center;"> 330 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 1,5% </td>
   <td style="text-align:center;"> 4.500 </td>
   <td style="text-align:center;"> 6,0% </td>
   <td style="text-align:center;"> 277 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 2,0% </td>
   <td style="text-align:center;"> 2.500 </td>
   <td style="text-align:center;"> 6,5% </td>
   <td style="text-align:center;"> 237 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 2,5% </td>
   <td style="text-align:center;"> 1.600 </td>
   <td style="text-align:center;"> 7,0% </td>
   <td style="text-align:center;"> 204 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 3,0% </td>
   <td style="text-align:center;"> 1.100 </td>
   <td style="text-align:center;"> 7,5% </td>
   <td style="text-align:center;"> 178 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 3,5% </td>
   <td style="text-align:center;"> 816 </td>
   <td style="text-align:center;"> 8,0% </td>
   <td style="text-align:center;"> 156 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 4,0% </td>
   <td style="text-align:center;"> 625 </td>
   <td style="text-align:center;"> 8,5% </td>
   <td style="text-align:center;"> 138 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 4,5% </td>
   <td style="text-align:center;"> 494 </td>
   <td style="text-align:center;"> 9,0% </td>
   <td style="text-align:center;"> 123 </td>
  </tr>
  <tr>
   <td style="text-align:center;"> 5,0% </td>
   <td style="text-align:center;"> 400 </td>
   <td style="text-align:center;"> 9,5% </td>
   <td style="text-align:center;"> 110 </td>
  </tr>
  <tr>
   <td style="text-align:center;">  </td>
   <td style="text-align:center;">  </td>
   <td style="text-align:center;"> 10,0% </td>
   <td style="text-align:center;"> 100 </td>
  </tr>
</tbody>
</table>

::: rmdkasus
### Studi Kasus: Menentukan Jumlah Sampel dari Tabel {.unnumbered}

Seorang mahasiswa ingin meneliti **proporsi mahasiswa ITERA yang menggunakan kendaraan bermotor** sebagai moda utama perjalanan ke kampus. Ia merancang survei dan perlu menentukan berapa responden yang harus ia kumpulkan.

Karena ia belum tahu berapa proporsi sesungguhnya di populasi, ia menggunakan asumsi terburuk: 50% menggunakan kendaraan bermotor dan 50% tidak (varians 50/50). Ia juga menetapkan bahwa *sampling error* yang masih dapat ia tolerir adalah **5%** pada tingkat kepercayaan 95%.

Dengan membaca Tabel \@ref(tab:tabel-ukuran-sampel-sampling-error) pada baris *sampling error* 5,0%, ia menemukan bahwa **sampel minimum yang dibutuhkan adalah 400 responden**. Jumlah inilah yang ia jadikan target pengumpulan data.

Perhatikan bahwa angka ini tidak bergantung pada seberapa besar populasi mahasiswa ITERA (yang berjumlah lebih dari 18.000 orang). Cukup 400 responden, dan hasil surveinya akan memiliki akurasi dalam batas ±5% pada tingkat kepercayaan 95%.
:::




## Konsep Distribusi dalam Statistik

Dalam stastistika inferensial, kita harus menguasai konsep mengenai **distribusi**. Distribusi adalah penyebaran suatu nilai yang memiliki karakteristik tertentu. Di sini, tujuan kita adalah mengenali apa yang kami akan sebut dengan **distribusi objek** dan **distribusi statistik**, atau yang dalam @healey2021statistics dan @ewing2020basic disebut **distribusi sampel** dan **distribusi hasil sampel** (*sampling distribution*).

### Model-model Distribusi Statistik

Terdapat banyak jenis model distribusi dalam statistik yang sering dipakai. Beberapa jenis model statisik yang populer misalnya adalah distribusi *uniform* (seragam), distribusi binomial, distribusi Poisson, dan distribusi normal atau Gaussian [@ModernStatR-Home]. Namun, dalam pembahasan statistika inferensial di buku ini kita hanya akan fokus pada **distribusi normal** dan turunannya, distribusi Student's t, beserta distribusi binomial, distribusi F, dan distribusi *Chi-square*.

Seperti yang ditampilkan oleh Gambar \@ref(fig:fig-ragam-distribusi) berikut, setiap jenis distribusi statistik mempunyai berbagai bentuknya. Bentuk-bentuk ini pada hakikatnya adalah **histogram-histogram** representasi sebaran nilai-nilai sekumpulan objek.

<div class="figure" style="text-align: center">
<img src="figures/fig-ragam-distribusi-1.png" alt="Ragam Bentuk Distribusi Statistik" width="80%" />
<p class="caption">(\#fig:fig-ragam-distribusi)Ragam Bentuk Distribusi Statistik</p>
</div>

**Interpretasi Bentuk Distribusi**

Seperti yang sudah dijelaskan bahwa bentuk distribusi sebenarnya adalah histogram, kita sudah belajar bahwa histogram memiliki 2 sumbu: sumbu X dan Y/mendatar dan tegak, yang masing-masing artinya adalah rentang nilai dan frekuensi kemunculan nilai tersebut secara berturut-turut. 

Begitu juga gambar-gambar distribusi tersebut. Sumbu X mencerminkan **nilai-nilai yang terdapat dalam objek-objek** yang dinyatakan distribusinya, sumbu Y jumlah kemunculan nilai-nilai tersebut. Selain dipahami sebagai jumlah, sumbu Y juga bisa diinterpretasikan sebagai **probabilitas** kemunculan nilai-nilai tersebut.

### Distribusi Normal {#bab-5-distribusi-normal}

Distribusi normal adalah salah satu jenis distribusi nilai yang memiliki karakteristik berbentuk seperti lonceng, simetris, dan membentang tanpa batas di kedua sisi sumbu horizontal [@tjokropandojo2021pengantar]. Oleh karena itu, model distribusi ini juga disebut *bell curve* atau kurva lonceng [@healey2021statistics] (Gambar \@ref(fig:fig-bab-5-hist-normal)).

<div class="figure" style="text-align: center">
<img src="figures/fig-bab-5-hist-normal-1.png" alt="Distribusi Normal" width="80%" />
<p class="caption">(\#fig:fig-bab-5-hist-normal)Distribusi Normal</p>
</div>

Dari Gambar \@ref(fig:fig-bab-5-hist-normal), kita dapat melihat bahwa distribusi normal memiliki beberapa karakteristik utama berikut:

1.  **Parameter Utama:** Distribusi normal ditentukan sepenuhnya oleh dua parameter: rata-rata (*mean* atau $\mu$) dan varians ($\sigma^2$) [@Chan-IntroProb]. Rata-rata menentukan lokasi tengah distribusi, sedangkan varians (atau standar deviasi) menentukan lebar atau penyebaran kurva [@healey2021statistics; @Hair-Multivariate].

<div class="figure" style="text-align: center">
<img src="figures/fig-bab-5-parameter-normal-1.png" alt="Perbandingan Distribusi Normal dengan Rata-rata Sama namun Standar Deviasi Berbeda" width="80%" />
<p class="caption">(\#fig:fig-bab-5-parameter-normal)Perbandingan Distribusi Normal dengan Rata-rata Sama namun Standar Deviasi Berbeda</p>
</div>

2.  **Simetri Sempurna:** Pada distribusi normal yang sempurna, nilai *mean* (rata-rata), *median* (nilai tengah), dan *mode* (nilai yang paling sering muncul) adalah identik dan berada **tepat di tengah distribusi** [@healey2021statistics; @devaus2014surveys].

3.  **Skewness dan Kurtosis:**

      - **Skewness (Kemencengan):** Distribusi normal memiliki nilai *skewness* 0, yang menunjukkan simetri sempurna. Jika data menumpuk di kiri, itu disebut *positive skew*, dan jika di kanan disebut *negative skew* [@devaus2014surveys; @ewing2020basic].

      - **Kurtosis (Keruncingan):** Mengukur keruncingan atau kedataran puncak distribusi relatif terhadap distribusi normal. Distribusi normal memiliki nilai kurtosis 3. Distribusi yang lebih runcing disebut leptokurtik (>3), dan yang lebih datar disebut platikurtik (<3) [@Chan-IntroProb; @ewing2020basic].

<div class="figure">
<img src="figures/05-inferensia-viz-skewness-1.png" alt="Ilustrasi Positive dan Negative Skewness" width="49%" />
<p class="caption">(\#fig:05-inferensia-viz-skewness)Ilustrasi Positive dan Negative Skewness</p>
</div>
<div class="figure">
<img src="figures/05-inferensia-viz-kurtosis-1.png" alt="Perbandingan Kurtosis: Normal (3) vs Platikurtik (&lt;3)" width="49%" />
<p class="caption">(\#fig:05-inferensia-viz-kurtosis)Perbandingan Kurtosis: Normal (3) vs Platikurtik (<3)</p>
</div>

4.  **Area di Bawah Kurva (Aturan 68-95-99, Aturan Empiris):** Salah satu karakteristik paling berguna adalah **proporsi area di bawah kurva yang tetap** berdasarkan jarak standar deviasi (SD) dari rata-rata [@healey2021statistics]:

    -   $\pm$ 1 SD mencakup sekitar 68,26% dari total kasus.
    -   $\pm$ 2 SD mencakup sekitar 95,44% dari total kasus.
    -   $\pm$ 3 SD mencakup sekitar 99,72% dari total kasus.

    Ini mengimplikasikan bahwa kejadian yang berada jauh di luar 3 standar deviasi dari rata-rata sangat jarang terjadi.

<div class="figure" style="text-align: center">
<img src="figures/fig-bab-5-aturan-689599-1.png" alt="Ilustrasi Aturan 68-95-99 (Aturan Empiris)" width="80%" />
<p class="caption">(\#fig:fig-bab-5-aturan-689599)Ilustrasi Aturan 68-95-99 (Aturan Empiris)</p>
</div>


### Distribusi Objek dan Distribusi Statistik

**Distribusi objek** atau **distribusi sampel** merujuk pada **sebaran nilai data** dari objek-objek yang menjadi sampel yang kita ambil. Dengan kata lain, distribusi ini menggambarkan variasi data individual setiap objek.

Di sisi lain, **distribusi statistik** atau **distribusi hasil sampel** *(sampling distribution)* adalah **sebaran nilai statistik** (misalnya rata-rata) dari suatu populasi yang berasal dari perhitungan statistik sampel-sampel yang diambil berulang kali dari populasi tersebut. Statistik yang dihitung biasanya dapat berupa proporsi atau rata-rata.

Mari pelajari kasus berikut untuk lebih memahami perbedaan antara distribusi objek dengan distribusi statistik.

::: rmdkasus
### Studi Kasus: Distribusi Objek vs Distribusi Statistik {.unnumbered}

Agar lebih mudah membayangkan perbedaan antara distribusi objek dan distribusi statistik, mari kita gunakan **populasi kecil** yang hanya terdiri dari **30 mahasiswa** (diambil dari data ITERA). Kita akan melihat variabel **Jarak Tempuh (km)**.

**1. Distribusi Objek (Sebaran Data Individu)**

Berikut adalah data populasi lengkap (N=30):

<table class="table" style="margin-left: auto; margin-right: auto;">
<caption>(\#tab:05-inferensia-populasi-30)Data Populasi (N=30)</caption>
 <thead>
  <tr>
   <th style="text-align:right;"> ID </th>
   <th style="text-align:right;"> Jarak </th>
   <th style="text-align:right;"> ID </th>
   <th style="text-align:right;"> Jarak </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:right;"> 18 </td>
   <td style="text-align:right;"> 0.44 </td>
   <td style="text-align:right;"> 4 </td>
   <td style="text-align:right;"> 5.01 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 2 </td>
   <td style="text-align:right;"> 0.72 </td>
   <td style="text-align:right;"> 12 </td>
   <td style="text-align:right;"> 5.19 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 17 </td>
   <td style="text-align:right;"> 1.76 </td>
   <td style="text-align:right;"> 21 </td>
   <td style="text-align:right;"> 5.24 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 28 </td>
   <td style="text-align:right;"> 2.05 </td>
   <td style="text-align:right;"> 15 </td>
   <td style="text-align:right;"> 5.30 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 7 </td>
   <td style="text-align:right;"> 2.24 </td>
   <td style="text-align:right;"> 20 </td>
   <td style="text-align:right;"> 5.40 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 23 </td>
   <td style="text-align:right;"> 2.75 </td>
   <td style="text-align:right;"> 26 </td>
   <td style="text-align:right;"> 5.57 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 22 </td>
   <td style="text-align:right;"> 2.78 </td>
   <td style="text-align:right;"> 24 </td>
   <td style="text-align:right;"> 5.99 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 9 </td>
   <td style="text-align:right;"> 2.79 </td>
   <td style="text-align:right;"> 10 </td>
   <td style="text-align:right;"> 6.50 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 29 </td>
   <td style="text-align:right;"> 3.57 </td>
   <td style="text-align:right;"> 5 </td>
   <td style="text-align:right;"> 6.59 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 19 </td>
   <td style="text-align:right;"> 3.77 </td>
   <td style="text-align:right;"> 6 </td>
   <td style="text-align:right;"> 6.78 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 30 </td>
   <td style="text-align:right;"> 3.77 </td>
   <td style="text-align:right;"> 14 </td>
   <td style="text-align:right;"> 7.07 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 27 </td>
   <td style="text-align:right;"> 4.47 </td>
   <td style="text-align:right;"> 13 </td>
   <td style="text-align:right;"> 7.82 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 8 </td>
   <td style="text-align:right;"> 4.85 </td>
   <td style="text-align:right;"> 3 </td>
   <td style="text-align:right;"> 8.70 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 16 </td>
   <td style="text-align:right;"> 4.88 </td>
   <td style="text-align:right;"> 11 </td>
   <td style="text-align:right;"> 10.44 </td>
  </tr>
  <tr>
   <td style="text-align:right;"> 25 </td>
   <td style="text-align:right;"> 4.88 </td>
   <td style="text-align:right;"> 1 </td>
   <td style="text-align:right;"> 12.41 </td>
  </tr>
</tbody>
</table>

Rata-rata populasi adalah $\mu = 4.99$ km dengan simpangan baku $\sigma = 2.67$ km.

Sekarang, kita ambil **1 sampel** berukuran $n=10$ secara acak (*Simple Random Sampling*). Pengambilan menghasilkan sampel dengan ID 3, 9, 14, 17, 22, 23, 24, 25, 27, dan 30.

<div class="figure" style="text-align: center">
<img src="figures/05-inferensia-sampel-satu-1.png" alt="Histogram Distribusi Objek (n=10)" width="80%" />
<p class="caption">(\#fig:05-inferensia-sampel-satu)Histogram Distribusi Objek (n=10)</p>
</div>

Pada histogram di atas, sumbu Y ("Frekuensi") menunjukkan **jumlah mahasiswa** yang memiliki jarak tempuh tertentu. Variasi datanya menggambarkan seberapa berbeda jarak antar individu.

**2. Distribusi Statistik (Sebaran Rata-rata)**

Sekarang, kita lakukan simulasi: kita mengambil sampel ($n=10$) dari populasi tersebut sebanyak **200 kali**. Setiap kali ambil, kita catat rata-ratanya.

Berikut adalah 8 hasil pertama dari 200 pengambilan sampel:

<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">
<caption>(\#tab:05-inferensia-simulasi-200)Hasil Simulasi Distribusi Sampling (8 Teratas dari 200)</caption>
 <thead>
  <tr>
   <th style="text-align:left;"> Pengambilan_Ke </th>
   <th style="text-align:left;"> Rata_Rata_Sampel </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> 1 </td>
   <td style="text-align:left;"> 3.79 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> 2 </td>
   <td style="text-align:left;"> 4.72 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> 3 </td>
   <td style="text-align:left;"> 4.7 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> 4 </td>
   <td style="text-align:left;"> 4.62 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> 5 </td>
   <td style="text-align:left;"> 6.76 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> 6 </td>
   <td style="text-align:left;"> 5.94 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> 7 </td>
   <td style="text-align:left;"> 3.89 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> 8 </td>
   <td style="text-align:left;"> 3.82 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> ... </td>
   <td style="text-align:left;"> ... </td>
  </tr>
</tbody>
</table>

Mari kita lihat histogram dari 200 rata-rata ini:

<div class="figure" style="text-align: center">
<img src="figures/05-inferensia-hist-sampling-1.png" alt="Distribusi Statistik (200 Rata-rata)" width="80%" />
<p class="caption">(\#fig:05-inferensia-hist-sampling)Distribusi Statistik (200 Rata-rata)</p>
</div>

Perhatikan perbedaan kedua histogram tersebut:

1.  **Distribusi objek**: Pada distribusi objek, tinggi batang (nilai di sumbu Y) mencerminkan "jumlah orang atau **frekuensi objek** yang memiliki nilai-nilai yang ada di sumbu X". Misalnya, objek yang memiliki nilai di antara 2,5 sampai 4,0 ada 4 buah (ID 23, 22, 9, dan 30), sementara 4,0 sampai 6,0 ada 2 objek (ID 27 dan 25).

2.  **Distribusi statistik**: Pada distribusi statistik, tinggi batang mencerminkan **frekuensi munculnya nilai rata-rata** dari 200 kali pengambilan sampel sebanyak 10 objek. Jika kita kaitkan dengan probabilitas, maka tinggi batang mewakili tingkat kemungkinan suatu nilai rata-rata dihasilkan dari sampel yang berjumlah 10 objek.
:::

## Teorema Limit Sentral

Tentu saja, di kehidupan nyata distribusi statistik dapat dikatakan tidak pernah ada. Sangat sulit untuk bisa mengambil sampel berkali-kali hingga sangat banyak. Ia hanyalah konsep teoritis untuk menjelaskan bagaimana suatu sampel bisa memiliki *pola statistik sampel yang dapat memprediksi populasi*. Dengan memahami pola prediksi tersebut, **kita tidak perlu lagi menghimpun semua anggota populasi** untuk menghitung parameter populasi. Cukup dengan mengumpulkan sampel tersebut, menghitung statistiknya, dan memperkirakan parameternya berdasarkan statistik tersebut.

Pola prediksi inilah yang dijelaskan oleh **Teorema Limit Sentral *(Central Limit Theorem)***. Teorema ini menjadi pijakan analisis inferensial karena memberikan dua jaminan penting:

1. jika ukuran sampel cukup besar (biasanya $n \ge 30$), **distribusi statistik sampel akan berbentuk normal** (lonceng simetris) apa pun bentuk populasi asalnya.

2. rata-rata dari distribusi statistik ini akan **tepat sama dengan rata-rata populasi sebenarnya**, dengan variasi yang semakin kecil seiring bertambahnya ukuran sampel. Ini adalah jaminan yang paling krusial dari teorema ini.

Kombinasi bentuk normal dan akurasi inilah yang memungkinkan kita melakukan estimasi dan uji statistik dengan percaya diri.

Berdasarkan teorema ini, kita dapat membagi analisis statistika inferensial menjadi analisis statistik inferensial **parametrik** dan **nonparametrik**. Analisis inferensial parametrik adalah analisis inferensial yang mengasumsikan bahwa populasi kita berdistribusi normal. Asumsi ini diuji dengan teknik pengujian kenormalan seperti [uji Shapiro-Wilk]('https://www.statistikian.com/2013/01/saphiro-wilk.html') atau [P-P plot]('https://online.stat.psu.edu/stat501/lesson/4/4.6').

::: rmdkasus
### Studi Kasus: Simulasi Teorema Limit Sentral {.unnumbered}

Mari kita buktikan CLT dengan melakukan simulasi pengambilan sampel berulang. Katakanlah kita memiliki **428 mahasiswa** sebagai populasi. Kita akan mengambil 1000 kali sampel berukuran 50 orang, lalu menghitung rata-ratanya dan memplot histogramnya.

Berikut adalah baris perintah untuk melakukan simulasi tersebut dalam R. Dataset yang digunakan dapat diakses pada [tautan ini]('https://github.com/abdulmubdibindar/buku-ajar-stp/blob/main/datasets/DataUtama_mhsITERA.csv').


``` r
library(ggplot2)
library(gridExtra)
library(dplyr)

# Setup Ulang Populasi Besar (N=428) untuk CLT
data_itera <- read.csv("datasets/DataUtama_mhsITERA.csv", sep = ";")
data_populasi <- data_itera |>
  mutate(jarak = jarak.km) |>
  filter(!is.na(jarak))

# Hitung parameter populasi
mu <- mean(data_populasi$jarak)
N <- nrow(data_populasi)

# 1. Distribusi Populasi (Data Asli)
p1 <- ggplot(data_populasi, aes(x = jarak)) +
  geom_histogram(bins = 30, fill = "gray", color = "black", alpha = 0.7) +
  geom_vline(xintercept = mu, color = "red", size = 1) +
  labs(title = paste0("Distribusi Populasi (N=", N, ")"), x = "Jarak (km)") +
  theme_minimal()

# 2. Distribusi Sampling (Rata-rata dari 1000 sampel)  --> SIMULASI
set.seed(999)
means_1000 <- replicate(1000, mean(sample(data_populasi$jarak, 50)))
df_means <- data.frame(means = means_1000)

p2 <- ggplot(df_means, aes(x = means)) +
  geom_histogram(bins = 30, fill = "steelblue", color = "white", alpha = 0.9) +
  geom_vline(xintercept = mean(means_1000), color = "red", size = 1) +
  labs(title = "Distribusi Sampling (n=50, 1000x)", x = "Rata-rata Sampel") +
  theme_minimal()

grid.arrange(p1, p2, ncol = 2)
```

<div class="figure">
<img src="figures/fig-05-inferensia-2-clt-studi-kasus-simulasi-1.png" alt="Perbandingan Distribusi Populasi (Kiri) dan Distribusi Sampling (Kanan)"  />
<p class="caption">(\#fig:fig-05-inferensia-2-clt-studi-kasus-simulasi)Perbandingan Distribusi Populasi (Kiri) dan Distribusi Sampling (Kanan)</p>
</div>

Gambar \@ref(fig:fig-05-inferensia-2-clt-studi-kasus-simulasi) menunjukkan distribusi objek populasi. Distribusi populasi (kiri) terlihat "miring" (*skewed*) ke kanan, artinya tidak normal. Namun, distribusi rata-rata sampelnya (kanan) berbentuk lonceng simetris yang hampir sempurna **normal**. Rata-rata dari distribusi statistik ini juga sangat dekat dengan rata-rata populasi sebenarnya ($\mu = 5.01$).
:::

::: rmdkasus
### Studi Kasus: Efek Ukuran Sampel terhadap Variasi {.unnumbered}

Mari kita lanjutkan eksperimen kita. Apa yang terjadi jika kita mengubah ukuran sampel ($n$) yang kita ambil berulang-ulang tersebut? Kali ini kita akan membandingkan distribusi statistik yang dihasilkan dari pengambilan sampel berukuran **$n=30$** dengan **$n=100$**.

<div class="figure">
<img src="figures/fig-05-inferensia-3-clt-sample-size-1.png" alt="Perbandingan Distribusi Statistik dengan Ukuran Sampel Berbeda"  />
<p class="caption">(\#fig:fig-05-inferensia-3-clt-sample-size)Perbandingan Distribusi Statistik dengan Ukuran Sampel Berbeda</p>
</div>

Perhatikan Gambar \@ref(fig:fig-05-inferensia-3-clt-sample-size). Meskipun kedua kurva sama-sama berbentuk lonceng dan berpusat di rata-rata populasi (garis merah), kurva distribusi statistik untuk **$n=100$ (biru)** jauh lebih "kurus" dan tinggi dibandingkan kurva **$n=30$ (kuning)**.

Ini menunjukkan bahwa semakin banyak sampel yang kita ambil dalam satu kali pengambilan ($n$ semakin besar), maka **variasi** dari rata-rata yang kita peroleh akan semakin kecil. Artinya, rata-rata sampel kita akan semakin jarang meleset jauh dari rata-rata populasi sebenarnya. Dengan kata lain, memperbesar ukuran sampel akan meningkatkan peluang kita untuk mendapatkan hasil yang sangat mendekati kondisi populasi yang sebenarnya.
:::



## Menghitung Peluang Kemunculan Nilai Tertentu dari Distribusi Statistik yang Berbentuk Normal.

Pada subbab \@ref(bab-5-distribusi-normal), kita telah belajar bahwa distribusi normal mempunyai aturan empiris atau aturan 68-95-99. Aturan ini berbicara tentang besar area di bawah kurva yang tetap berdasarkan jarak standar deviasi (SD) dari rata-rata [@healey2021statistics]:

  -   $\pm$ 1 SD mencakup sekitar 68,26% dari total kasus.
  -   $\pm$ 2 SD mencakup sekitar 95,44% dari total kasus.
  -   $\pm$ 3 SD mencakup sekitar 99,72% dari total kasus.

Sekarang kita akan menerapkan aturan empiris ini pada distribusi statistik yang berbentuk normal. Kita akan banyak menggunakan distribusi normal ini untuk menghitung **probabilitas**--yang diwakili oleh besar area di bawah kurva distribusi normal--**dari suatu nilai yang diminta**, atau menentukan **besar probabilitas terjadinya suatu nilai**. 

Untuk itu, kita perlu memahami konsep tentang standard error dan nilai standar atau nilai Z (*Z-score*). Kedua konsep ini sangat krusial bagi kita untuk memudahkan kita membaca tabel nilai Z yang beguna untuk 

### *Standard Error* (SE)

Sebagaimana yang sudah kita pelajari, distribusi statistik berbeda dengan distribusi objek dalam hal nilai yang diukur. Jika **distribusi objek mengukur nilai dari objek**, maka **distribusi statistik mengukur nilai dari sekumpulan objek yang diambil berulang-ulang dari populasi**.

Dalam distribusi objek, lebar distribusi berkaitan dengan ukuran statistik deskriptif yang disebut **standar deviasi** atau **simpangan baku**. Simpangan baku menunjukkan ukuran jarak rata-rata penyimpangan nilai-nilai dalam distribusi terhadap rata-ratanya. Untuk penyegaran, rumusnya adalah sebagai berikut.

$$
\begin{align}
\text{Simpangan Baku} &= \sqrt{\text{Variansi}}\\
&=\sqrt{\frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n}} (\#eq:konsep-simpangan-baku-bab5)
\end{align}
$$ 

Di sisi lain, dalam distribusi statistik simpangan bakunya punya sebutan lain, yakni ***standard error*** (SE). *Standard error* pada hakikatnya adalah adalah **ukuran jarak statistik sampel dari parameter populasi**. Ingat kembali bahwa **rata-rata dari distribusi statistik adalah nilai parameter populasinya**. Semakin kecil SE, semakin presisi estimasi sampel kita terhadap parameter populasi. Secara matematis, standard error dihitung dari simpangan baku sampel kita dengan rumus berikut.

$$
\begin{align}
\text{SE} &=\frac{\sigma}{\sqrt{n}} (\#eq:konsep-standard-error-bab5)
\end{align}
$$ 

Dengan $\sigma$ adalah simpangan baku populasi dan $n$ adalah ukuran sampel.

Jika $\sigma$ tidak diketahui, kita gunakan simpangan baku sampel ($s$) sebagai estimasi, sehingga Persamaan \@ref(eq:konsep-standard-error-bab5) menjadi:

$$
\begin{align}
\text{SE} &=\frac{s}{\sqrt{n}} (\#eq:konsep-se-pake-sd)
\end{align}
$$ 


::: rmdnote

**PENTING**

Dalam beberapa sumber, seperti @healey2021statistics, perhitungan *standard error* yang menggunakan estimasi dari simpangan baku seperti Persamaan \@ref(eq:konsep-se-pake-sd) menggunakan bentuk yang dikoreksi, yakni dengan cara mengurangkan 1 dari nilai ukuran sampelnya, sehingga persamaannya menjadi:

$$
\begin{align}
\text{SE} &=\frac{s}{\sqrt{n-1}} (\#eq:konsep-se-pake-sd-healey)
\end{align}
$$ 

Yang mana yang betul? Karena keduanya sama-sama disebutkan dalam banyak literatur, di sini yang perlu kita perhatikan adalah **konsistensi kita** dalam penggunaan salah satunya.

:::

::: rmdkasus
### Studi Kasus: Menghitung Standard Error {.unnumbered}

Misalkan kita mengambil **satu sampel** acak berukuran $n=100$ mahasiswa dari populasi.



Dari sampel ini, kita peroleh rata-rata jarak $\bar{x} = 5.16$ km. Kita tahu simpangan baku populasi $\sigma = 2.82$ km. Maka *Standard error* adalah:

$$
\begin{align}
SE &=\frac{s}{\sqrt{n}}\\
&= \frac{2.82}{\sqrt{100}} \\
&= 0.2817
\end{align}
$$

Nilai ini memberitahu kita bahwa rata-rata sampel kita (5.16) diperkirakan menyimpang sekitar $\pm 0.28$ km dari rata-rata populasi sebenarnya.
:::

### Nilai Standar (*Z-Score*)

*Z-score* menunjukkan posisi suatu nilai dalam sumbu X distribusi normal **jika rata-rata distribusi tersebut dibuat 0** dan **simpangan bakunya dibuat 1**. Untuk distribusi objek, rumusnya adalah:

$$
\begin{align}
Z = \frac{x - \mu}{\sigma} (\#eq:z-score)
\end{align}
$$

Dengan $x$ adalah nilai dalam distribusi normal yang akan kita konversi, $\mu$ melambangkan rata-rata distribusi, dan $\sigma$ melambangkan simpangan baku distribusi.


::: rmdkasus
### Studi Kasus: Menghitung Z-Score dan Peluang {.unnumbered}

Jika kita mempunyai distribusi biaya perjalanan .
:::

Jika kita menggunakan konsep *Z-Score* tersebut pada distribusi statistik, persamaan \@ref(eq:z-score) akan berubah menjadi:

$$
\begin{align}
Z = \frac{\bar{x} - \mu}{SE}
(\#eq:z-score-sampling-distribution)
\end{align}
$$.

Dengan $\bar{x}$ adalah rata-rata sampel yang kita miliki, $\mu$ adalah rata-rata populasi (parameter) yang kita jadikan sebagai patokan, dan $SE$ adalah *standard error* yang dihitung dengan persamaan \@ref(eq:konsep-se-pake-sd) atau \@ref(eq:konsep-se-pake-sd-healey), sehingga persamaan \@ref(eq:z-score-sampling-distribution) menjadi:

$$
\begin{equation}
Z = \frac{\bar{x} - \mu}{s/\sqrt{n}}
(\#eq:z-score-sampling-distribution)
\end{equation}
$$.



::: rmdexercise
## Soal Evaluasi 5 {.unnumbered}

1.  **Studi Kasus Survei Keakraban**. [STP-4.1]{.capaian} Sebuah acara keakraban angkatan Anda akan dilakukan di suatu tempat yang memerlukan biaya sewa tempat. Agar acara Anda dihadiri sebanyak mungkin orang, Anda menanyakan kesediaan kawan-kawan Anda. Anda pun merancang sebuah survei untuk mengetahui persentase kawan Anda yang setuju acara keakraban diadakan di tempat tersebut. Untuk itu Anda menanyakan sebagian kawan Anda sebagai sampel.

    a.  Apabila Anda memiliki daftar nama seluruh kawan Anda, apa nama teknik pengambilan sampel yang Anda bisa lakukan?
    b.  Jelaskan bagaimana metode Anda memilih sampel kawan Anda berdasarkan kondisi di soal ke-1 tersebut.
    c.  Apabila Anda tidak memiliki daftar nama seluruh kawan Anda, apa nama teknik pengambilan sampel yang Anda bisa lakukan?
    d.  Jelaskan bagaimana metode Anda memilih sampel kawan Anda berdasarkan kondisi di soal ke-3 tersebut.

2.  Jelaskan perbedaan antara simpangan baku (*standard deviation*) dengan *standard error*! [STP-4.2]{.capaian}

3.  **Kasus Jarak Tempat Tinggal**. [STP-4.2]{.capaian} Suatu sampel pegawai ITERA berjumlah 286 orang yang mengukur jarak tempat tinggal mereka ke kampus menghasilkan rata-rata 7,90 km dan simpangan baku 6,42 km.

    a.  Jelaskan perbedaan distribusi sampel dengan distribusi statistik sampel menggunakan kasus ini.
    b.  Apakah kita dapat menggunakan teorema limit sentral dalam perhitungan probabilitas distribusi statistik sampel kita tersebut? Jelaskan jawaban Anda.
    c.  Katakanlah parameternya (rata-rata jarak tempat tinggal seluruh pegawai ITERA) diketahui sebesar 7,5 km, Hitunglah nilai standar (z-score) sampel kita.
    d.  Hitunglah probabilitas kita mendapatkan nilai rata-rata seperti yang ditanyakan dalam 3.c tersebut dan jelaskan maknanya.
:::

<!--chapter:end:05-pengantar-inferensial.Rmd-->

# Estimasi Parameter {#bab-6-estimasi-parameter}

## Konsep Dasar

Dalam statistik inferensial, kita menggunakan statistik sampel (seperti $\bar{x}$) untuk mengestimasi parameter populasi (seperti $\mu$).

Ada dua jenis estimasi:
1.  **Estimasi Titik (Point Estimation)**. Menggunakan satu nilai tunggal. Contoh: "Rata-rata pendapatan adalah 5 juta". Kelemahannya: akurasinya diragukan.
2.  **Estimasi Rentang (Interval Estimation)**. Menggunakan rentang nilai dengan tingkat kepercayaan tertentu. Contoh: "Rata-rata pendapatan ada di antara 4,8 juta hingga 5,2 juta dengan tingkat kepercayaan 95%". Inilah yang disebut **Confidence Interval (CI)**.

## Estimasi Rentang Kepercayaan (Confidence Interval)

Rumus umum untuk CI rata-rata adalah:
$$ \bar{x} \pm Z_{\alpha/2} \times SE $$
Atau:
$$ \bar{x} - Z_{\alpha/2} \frac{\sigma}{\sqrt{n}} < \mu < \bar{x} + Z_{\alpha/2} \frac{\sigma}{\sqrt{n}} $$

Nilai $Z_{\alpha/2}$ bergantung pada tingkat kepercayaan (Confidence Level, $1-\alpha$):
*   Tingkat Kepercayaan 90% ($\alpha=10\%$) $\rightarrow Z = 1.645$
*   Tingkat Kepercayaan 95% ($\alpha=5\%$) $\rightarrow Z = 1.96$
*   Tingkat Kepercayaan 99% ($\alpha=1\%$) $\rightarrow Z = 2.575$

### Studi Kasus

Seorang peneliti ingin mengestimasi rata-rata pengeluaran bulanan mahasiswa. Dari sampel 100 mahasiswa, diperoleh rata-rata 1,5 juta rupiah dengan simpangan baku 500 ribu rupiah. Buatlah selang kepercayaan 95%.

Diketahui:
*   $n = 100$
*   $\bar{x} = 1.500.000$
*   $s = 500.000$ (menggantikan $\sigma$)
*   $Z_{0.025} = 1.96$

Standard Error: $SE = 500.000 / \sqrt{100} = 50.000$.

Batas Bawah: $1.500.000 - (1.96 \times 50.000) = 1.402.000$.
Batas Atas: $1.500.000 + (1.96 \times 50.000) = 1.598.000$.

Jadi, dengan tingkat kepercayaan 95%, rata-rata pengeluaran mahasiswa berada di antara Rp1.402.000 dan Rp1.598.000.

::: rmdexercise
## Soal Evaluasi 7 {.unnumbered}

1.  Apa yang dimaksud dengan tingkat kepercayaan (confidence level)? [STP-5.1]{.capaian}
2.  Hitunglah Confidence Interval 95% untuk rata-rata jika $\bar{x}=100$, $s=15$, dan $n=36$. [STP-5.2]{.capaian}

:::

<!--chapter:end:06-estimasi-parameter.Rmd-->

# Uji Hipotesis Satu Populasi

## Konsep Dasar

Uji hipotesis adalah prosedur statistik yang menggunakan data sampel untuk mengevaluasi suatu dugaan (hipotesis) mengenai populasi.

### Hipotesis Nol dan Alternatif

*   **Hipotesis Nol ($H_0$)**: Pernyataan tentang status quo, tidak ada perbedaan, atau tidak ada efek. Biasanya mengandung tanda sama dengan ($=, \le, \ge$).
*   **Hipotesis Alternatif ($H_1$)**: Pernyataan yang bertentangan dengan $H_0$, biasanya merupakan dugaan yang ingin dibuktikan oleh peneliti. Mengandung tanda ketidaksamaan ($\ne, <, >$).

### Langkah-langkah Pengujian Hipotesis

1.  **Rumuskan Hipotesis ($H_0$ dan $H_1$)**.
2.  **Tentukan Tingkat Signifikansi ($\alpha$)**. Biasanya 0,05.
3.  **Pilih Statistik Uji**. (Z-test jika $\sigma$ diketahui atau $n > 30$, t-test jika $\sigma$ tidak diketahui dan $n < 30$).
4.  **Hitung Statistik Hitung dan P-value**.
5.  **Ambil Keputusan**. Tolak $H_0$ jika P-value $< \alpha$.
6.  **Tarik Kesimpulan**.

## Studi Kasus dengan R

Seorang perencana kota menduga bahwa rata-rata waktu tempuh warga ke tempat kerja adalah **lebih dari 45 menit**. Dari survei terhadap 35 warga, diperoleh rata-rata 48 menit dengan simpangan baku 10 menit. Ujilah hipotesis tersebut dengan $\alpha = 0.05$.

Hipotesis:
*   $H_0: \mu \le 45$ (Rata-rata tidak lebih dari 45 menit)
*   $H_1: \mu > 45$ (Rata-rata lebih dari 45 menit)


``` r
# Data Sampel (Simulasi)
set.seed(123)
waktu_tempuh <- rnorm(35, mean = 48, sd = 10)

# Uji T Satu Sampel
t.test(waktu_tempuh, mu = 45, alternative = "greater")
```

```
## 
## 	One Sample t-test
## 
## data:  waktu_tempuh
## t = 2.1102, df = 34, p-value = 0.02114
## alternative hypothesis: true mean is greater than 45
## 95 percent confidence interval:
##  45.67059      Inf
## sample estimates:
## mean of x 
##  48.37518
```

**Interpretasi**:
Jika p-value < 0,05, maka kita menolak $H_0$ dan menyimpulkan bahwa rata-rata waktu tempuh secara signifikan lebih dari 45 menit.

::: rmdexercise
## Soal Evaluasi 8 {.unnumbered}

1.  Jelaskan perbedaan antara Hipotesis Nol dan Hipotesis Alternatif. [STP-6.1]{.capaian}
2.  Apa makna P-value dalam pengambilan keputusan uji hipotesis? [STP-6.2]{.capaian}

:::

<!--chapter:end:07-uji-hipotesis-satu-populasi.Rmd-->

# Uji Hipotesis Dua Populasi

## Konsep Dasar

Uji ini digunakan untuk membandingkan parameter (rata-rata atau proporsi) dari dua populasi yang berbeda. Tujuannya adalah untuk mengetahui apakah ada perbedaan yang signifikan di antara keduanya.

### Uji Beda Rata-rata (Independent Samples t-test)

Digunakan untuk dua kelompok sampel yang tidak saling berhubungan (independen). Contoh: Membandingkan rata-rata pendapatan warga di Kota A dan Kota B.

Hipotesis:
*   $H_0: \mu_A = \mu_B$
*   $H_1: \mu_A \ne \mu_B$

### Uji Beda Rata-rata Berpasangan (Paired Samples t-test)

Digunakan untuk dua kelompok sampel yang saling berhubungan (berpasangan). Contoh: Membandingkan kemacetan di jalan yang sama **sebelum** dan **sesudah** penerapan kebijakan ganjil-genap.

## Studi Kasus dengan R

### Independent t-test

Membandingkan pendapatan (dalam juta) antara pria dan wanita.


``` r
# Data Contoh
pria <- c(5, 6, 5, 7, 6, 8, 5)
wanita <- c(4, 5, 4, 6, 5, 5, 4)

# Uji t independen
t.test(pria, wanita, var.equal = TRUE)
```

```
## 
## 	Two Sample t-test
## 
## data:  pria and wanita
## t = 2.4648, df = 12, p-value = 0.02978
## alternative hypothesis: true difference in means is not equal to 0
## 95 percent confidence interval:
##  0.1491572 2.4222714
## sample estimates:
## mean of x mean of y 
##  6.000000  4.714286
```

### Paired t-test

Membandingkan waktu tempuh (menit) sebelum dan sesudah pembangunan tol.


``` r
sebelum <- c(60, 55, 70, 65, 80)
sesudah <- c(40, 45, 50, 55, 60)

# Uji t berpasangan
t.test(sebelum, sesudah, paired = TRUE)
```

```
## 
## 	Paired t-test
## 
## data:  sebelum and sesudah
## t = 6.532, df = 4, p-value = 0.002838
## alternative hypothesis: true mean difference is not equal to 0
## 95 percent confidence interval:
##   9.199126 22.800874
## sample estimates:
## mean difference 
##              16
```

::: rmdexercise
## Soal Evaluasi 9 {.unnumbered}

1.  Kapan kita menggunakan uji t independen dan kapan menggunakan uji t berpasangan? Berikan contoh kasus perencanaannya! [STP-7.1]{.capaian}
2.  Lakukan uji beda rata-rata untuk data berikut... [STP-7.2]{.capaian}

:::

<!--chapter:end:08-uji-hipotesis-dua-populasi.Rmd-->

# Uji Hipotesis Lebih dari Dua Populasi

## Analisis Variansi (ANOVA)

Ketika kita ingin membandingkan rata-rata dari **lebih dari dua** kelompok populasi, kita menggunakan **Analysis of Variance (ANOVA)**. Jika kita menggunakan uji t berulang kali untuk setiap pasangan kelompok, risiko kesalahan Tipe I (False Positive) akan meningkat. ANOVA mengatasi masalah ini dengan menguji perbedaan secara simultan.

Hipotesis ANOVA Satu Arah (One-Way ANOVA):
*   $H_0: \mu_1 = \mu_2 = \dots = \mu_k$ (Semua rata-rata kelompok sama)
*   $H_1$: Setidaknya ada satu pasang rata-rata yang berbeda.

## Studi Kasus dengan R

Kita ingin membandingkan rata-rata harga tanah di tiga zona: Pusat Kota, Suburban, dan Rural.


``` r
# Data Contoh
harga_tanah <- c(10, 12, 11, 13, 15, # Pusat
                 8, 9, 7, 8, 10,       # Suburban
                 4, 5, 3, 5, 4)        # Rural
zona <- factor(rep(c("Pusat", "Suburban", "Rural"), each = 5))

data_tanah <- data.frame(harga = harga_tanah, zona = zona)

# ANOVA Satu Arah
model_anova <- aov(harga ~ zona, data = data_tanah)
summary(model_anova)
```

```
##             Df Sum Sq Mean Sq F value   Pr(>F)    
## zona         2  160.1   80.07   42.14 3.75e-06 ***
## Residuals   12   22.8    1.90                     
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
```

**Interpretasi**:
Jika nilai Pr(>F) pada tabel ANOVA kurang dari 0,05, maka tolak $H_0$. Artinya, terdapat perbedaan signifikan rata-rata harga tanah antar zona tersebut. Untuk mengetahui zona mana yang berbeda, dapat dilanjutkan dengan uji lanjut (Post Hoc Test) seperti Tukey HSD.


``` r
TukeyHSD(model_anova)
```

```
##   Tukey multiple comparisons of means
##     95% family-wise confidence level
## 
## Fit: aov(formula = harga ~ zona, data = data_tanah)
## 
## $zona
##                diff       lwr      upr     p adj
## Rural-Pusat    -8.0 -10.32579 -5.67421 0.0000025
## Suburban-Pusat -3.8  -6.12579 -1.47421 0.0024733
## Suburban-Rural  4.2   1.87421  6.52579 0.0011306
```

::: rmdexercise
## Soal Evaluasi 10 {.unnumbered}

1.  Mengapa kita tidak dianjurkan menggunakan uji t berulang kali untuk membandingkan 3 kelompok atau lebih? [STP-7.3]{.capaian}
2.  Apa kesimpulan jika P-value ANOVA > 0,05? [STP-7.4]{.capaian}

:::

<!--chapter:end:09-uji-hipotesis-lebih-dua-populasi.Rmd-->

# Korelasi Antarvariabel Nominal

## Konsep Dasar

Analisis ini digunakan untuk mengukur kekuatan hubungan antara dua variabel kategori (nominal). Teknik yang umum digunakan adalah **Chi-Square ($X^2$)** untuk signifikansi dan **Cramer's V**, **Phi**, atau **Lambda** untuk kekuatan hubungan.

## Studi Kasus dengan R

Apakah ada hubungan antara **Fakultas** dengan **Moda Transportasi** yang digunakan?


``` r
# Data Contoh
fakultas <- c("Saintek", "Soshum", "Saintek", "Soshum", "Saintek", "Saintek")
moda <- c("Motor", "Mobil", "Motor", "Jalan Kaki", "Mobil", "Motor")

# Membuat Tabel Kontingensi
tabel <- table(fakultas, moda)
print(tabel)
```

```
##          moda
## fakultas  Jalan Kaki Mobil Motor
##   Saintek          0     1     3
##   Soshum           1     1     0
```

``` r
# Uji Chi-Square
chisq.test(tabel)
```

```
## 
## 	Pearson's Chi-squared test
## 
## data:  tabel
## X-squared = 3.75, df = 2, p-value = 0.1534
```

**Interpretasi**:
Jika P-value < 0,05, maka ada hubungan signifikan antara Fakultas dan Moda Transportasi.

::: rmdexercise
## Soal Evaluasi 11 {.unnumbered}

1.  Apa perbedaan Chi-Square Test dengan Lambda sebagai ukuran asosiasi? [STP-8.1]{.capaian}
2.  Hitunglah nilai Cramer's V untuk tabel kontingensi berikut... [STP-8.2]{.capaian}

:::

<!--chapter:end:10-korelasi-nominal.Rmd-->

# Korelasi Antarvariabel Ordinal

## Konsep Dasar

Untuk data ordinal (berjenjang/ranking), kita menggunakan korelasi berbasis peringkat. Dua yang paling populer adalah **Spearman's Rho ($\rho$)** dan **Kendall's Tau ($\tau$)**.

## Studi Kasus dengan R

Apakah ada hubungan antara **Tingkat Pendidikan** (SD, SMP, SMA) dengan **Kepuasan Layanan** (Rendah, Sedang, Tinggi)?


``` r
# Data Ordinal (sebagai angka peringkat)
pendidikan <- c(1, 2, 3, 2, 3, 1, 2)
kepuasan <- c(1, 1, 3, 2, 3, 1, 2)

# Korelasi Spearman
cor.test(pendidikan, kepuasan, method = "spearman")
```

```
## 
## 	Spearman's rank correlation rho
## 
## data:  pendidikan and kepuasan
## S = 5.6, p-value = 0.005752
## alternative hypothesis: true rho is not equal to 0
## sample estimates:
## rho 
## 0.9
```

``` r
# Korelasi Kendall
cor.test(pendidikan, kepuasan, method = "kendall")
```

```
## 
## 	Kendall's rank correlation tau
## 
## data:  pendidikan and kepuasan
## z = 2.3936, p-value = 0.01668
## alternative hypothesis: true tau is not equal to 0
## sample estimates:
##   tau 
## 0.875
```

**Interpretasi**:
Nilai korelasi mendekati +1 menunjukkan hubungan positif kuat (semakin tinggi pendidikan, semakin tinggi kepuasan).

::: rmdexercise
## Soal Evaluasi 12 {.unnumbered}

1.  Kapan kita sebaiknya menggunakan Kendall's Tau dibandingkan Spearman's Rho? [STP-9.1]{.capaian}
2.  Jelaskan makna korelasi negatif pada variabel ordinal! [STP-9.2]{.capaian}

:::

<!--chapter:end:11-korelasi-ordinal.Rmd-->

# Korelasi Antarvariabel Metrik

## Konsep Dasar

Untuk dua variabel numerik (interval/rasio), ukuran asosiasi yang paling umum adalah **Pearson Product-Moment Correlation ($r$)**. Nilai $r$ berkisar antara -1 hingga +1.

## Studi Kasus dengan R

Hubungan antara **Pendapatan** dan **Pengeluaran**.


``` r
pendapatan <- c(5, 6, 7, 8, 9, 10, 11)
pengeluaran <- c(3, 4, 3.5, 5, 6, 6.5, 7)

# Scatterplot
plot(pendapatan, pengeluaran)
```

![](figures/bab-12-korelasi-pearson-1.png)<!-- -->

``` r
# Korelasi Pearson
cor.test(pendapatan, pengeluaran, method = "pearson")
```

```
## 
## 	Pearson's product-moment correlation
## 
## data:  pendapatan and pengeluaran
## t = 8.5927, df = 5, p-value = 0.0003521
## alternative hypothesis: true correlation is not equal to 0
## 95 percent confidence interval:
##  0.7916653 0.9953960
## sample estimates:
##       cor 
## 0.9677688
```

::: rmdexercise
## Soal Evaluasi 13 {.unnumbered}

1.  Apa syarat utama penggunaan korelasi Pearson? [STP-10.1]{.capaian}
2.  Jika $r = 0$, apakah artinya tidak ada hubungan sama sekali? Jelaskan! [STP-10.2]{.capaian}

:::

<!--chapter:end:12-korelasi-metrik.Rmd-->

# Regresi Linear Sederhana

## Konsep Dasar

Regresi linear sederhana digunakan untuk memprediksi nilai satu variabel dependen ($Y$) berdasarkan satu variabel independen ($X$). Persamaannya:
$$ Y = a + bX + \epsilon $$

## Studi Kasus dengan R

Memprediksi **Pengeluaran** berdasarkan **Pendapatan**.


``` r
pendapatan <- c(5, 6, 7, 8, 9, 10, 11)
pengeluaran <- c(3, 4, 3.5, 5, 6, 6.5, 7)

# Membuat Model Regresi
model <- lm(pengeluaran ~ pendapatan)
summary(model)
```

```
## 
## Call:
## lm(formula = pengeluaran ~ pendapatan)
## 
## Residuals:
##          1          2          3          4          5          6 
##  8.929e-02  3.929e-01 -8.036e-01 -1.804e-16  3.036e-01  1.071e-01 
##          7 
## -8.929e-02 
## 
## Coefficients:
##             Estimate Std. Error t value Pr(>|t|)    
## (Intercept) -0.57143    0.66834  -0.855 0.431606    
## pendapatan   0.69643    0.08105   8.593 0.000352 ***
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
## 
## Residual standard error: 0.4289 on 5 degrees of freedom
## Multiple R-squared:  0.9366,	Adjusted R-squared:  0.9239 
## F-statistic: 73.83 on 1 and 5 DF,  p-value: 0.0003521
```

``` r
# Melihat koefisien
coef(model)
```

```
## (Intercept)  pendapatan 
##  -0.5714286   0.6964286
```

**Interpretasi**:
Nilai Intercept ($a$) dan Slope ($b$) menentukan persamaan garis prediksi. $R^2$ menunjukkan seberapa baik model menjelaskan variasi data.

::: rmdexercise
## Soal Evaluasi 14 {.unnumbered}

1.  Apa perbedaan antara korelasi dan regresi? [STP-11.1]{.capaian}
2.  Jelaskan makna $R^2$ (Koefisien Determinasi)! [STP-11.2]{.capaian}

:::

<!--chapter:end:13-regresi-sederhana.Rmd-->

# Regresi Linear Berganda

## Konsep Dasar

Regresi linear berganda melibatkan **lebih dari satu** variabel independen untuk memprediksi variabel dependen.
$$ Y = a + b_1X_1 + b_2X_2 + \dots + \epsilon $$

## Studi Kasus dengan R

Memprediksi **Harga Rumah** berdasarkan **Luas Tanah** dan **Jumlah Kamar**.


``` r
harga <- c(500, 700, 600, 800, 900)
luas <- c(100, 150, 120, 160, 200)
kamar <- c(2, 3, 2, 4, 5)

# Model Regresi Berganda
model_berganda <- lm(harga ~ luas + kamar)
summary(model_berganda)
```

```
## 
## Call:
## lm(formula = harga ~ luas + kamar)
## 
## Residuals:
##       1       2       3       4       5 
## -22.901  -6.107  16.031  32.824 -19.847 
## 
## Coefficients:
##             Estimate Std. Error t value Pr(>|t|)
## (Intercept)  156.489    104.150   1.503    0.272
## luas           3.053      1.724   1.771    0.219
## kamar         30.534     50.865   0.600    0.609
## 
## Residual standard error: 33.84 on 2 degrees of freedom
## Multiple R-squared:  0.9771,	Adjusted R-squared:  0.9542 
## F-statistic: 42.67 on 2 and 2 DF,  p-value: 0.0229
```

::: rmdexercise
## Soal Evaluasi 15 {.unnumbered}

1.  Apa itu multikolinearitas dalam regresi berganda? [STP-12.1]{.capaian}
2.  Bagaimana cara menginterpretasikan Adjusted $R^2$? [STP-12.2]{.capaian}

:::

<!--chapter:end:14-regresi-berganda.Rmd-->

# Analisis Statistik Multivariat Interdependensi

## Konsep Dasar

Analisis multivariat interdependensi tidak membedakan variabel menjadi dependen dan independen. Tujuannya adalah untuk mencari struktur dasar dari sekumpulan variabel.
Contoh: **Analisis Faktor** dan **Principal Component Analysis (PCA)**. Biasanya digunakan untuk mereduksi dimensi data (menyederhanakan banyak variabel menjadi beberapa faktor utama).

## Studi Kasus dengan R

Mereduksi 5 indikator kepuasan menjadi faktor-faktor utama.


``` r
# Simulasi Data
set.seed(123)
data_survei <- matrix(rnorm(100*5), ncol=5)
colnames(data_survei) <- c("Q1", "Q2", "Q3", "Q4", "Q5")

# Principal Component Analysis
pca_result <- prcomp(data_survei, scale. = TRUE)
summary(pca_result)
```

```
## Importance of components:
##                           PC1    PC2    PC3    PC4    PC5
## Standard deviation     1.1077 1.0610 1.0191 0.9468 0.8440
## Proportion of Variance 0.2454 0.2251 0.2077 0.1793 0.1425
## Cumulative Proportion  0.2454 0.4705 0.6783 0.8575 1.0000
```

``` r
# Melihat beban faktor (loadings)
pca_result$rotation
```

```
##            PC1        PC2        PC3        PC4       PC5
## Q1  0.67277300  0.3292034 -0.1275847 -0.1588174 0.6304766
## Q2  0.19353433 -0.6901072  0.1205644  0.6023990 0.3299640
## Q3 -0.28920162 -0.4912642 -0.5283287 -0.5405369 0.3220413
## Q4  0.01926618 -0.2337862  0.8146660 -0.5122828 0.1373262
## Q5 -0.65261949  0.3455152  0.1624021  0.2393297 0.6091420
```

::: rmdexercise
## Soal Evaluasi 16 {.unnumbered}

1.  Apa tujuan utama dari Analisis Faktor? [STP-13.1]{.capaian}
2.  Jelaskan perbedaan mendasar antara Analisis Regresi dan Analisis Faktor! [STP-13.2]{.capaian}

:::

<!--chapter:end:15-multivariat-interdependensi.Rmd-->

