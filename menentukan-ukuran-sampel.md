# Menentukan Ukuran Sampel

Penentuan ukuran sampel dalam penelitian kuantitatif bergantung pada dua faktor analitik utama: (1) derajat akurasi yang diisyaratkan untuk sampel tersebut, dan (2) sejauh mana terdapat variasi atau heterogenitas dalam populasi terkait karakteristik utama yang sedang diteliti [1]. Pendekatan probabilitas menuntut ukuran sampel yang cukup agar inferensi statistik dapat dilakukan secara valid dan representatif terhadap populasi target [2].

## Pendekatan de Vaus: Ukuran Sampel Berbasis _Sampling Error_

### Prinsip Dasar

Berlawanan dengan intuisi awam, ukuran populasi asal dari mana sampel ditarik sebagian besar **tidak relevan** terhadap akurasi sampel [1]. Akurasi sebuah sampel ditentukan oleh **ukuran absolut** dari sampel itu sendiri, bukan proporsinya terhadap populasi [1]. Pengecualian terjadi hanya ketika ukuran sampel merepresentasikan proporsi yang substansial dari populasi (misalnya 10% atau lebih); pada kondisi ini diperlukan formula penyesuaian yang disebut _finite population correction_ [1].

De Vaus oleh karenanya tidak menyusun tabel ukuran sampel berdasarkan besaran populasi, melainkan berdasarkan **tingkat kesalahan (_margin of error_) dan heterogenitas populasi** [1].

Dasar matematis yang digunakan adalah _standard error_ binomial:

$$
S_B = \sqrt{\frac{P \times Q}{N}}
$$

**Keterangan:**

- $S_B$ = estimasi _standard error_
- $P$ = persentase observasi pada kategori yang menjadi fokus
- $Q$ = persentase observasi di luar kategori fokus ($100\% - P$)
- $N$ = jumlah kasus dalam sampel

Pada tingkat kepercayaan 95%, nilai parameter populasi yang sesungguhnya secara probabilistik akan jatuh dalam rentang $\pm 2$ unit _standard error_ dari persentase sampel [1].

### Tabel 1: Ukuran Sampel Minimum pada Varians 50/50

Apabila variasi populasi pada variabel yang diteliti tidak diketahui, asumsi yang paling konservatif adalah menetapkan kondisi heterogenitas ekstrem, yakni pemisahan respons 50/50 [1]. Kondisi ini menghasilkan _standard error_ terbesar dan dengan demikian kebutuhan sampel yang paling besar. Tabel berikut merangkum ukuran sampel minimum pada variasi tingkat _sampling error_ dalam kondisi tersebut, untuk _simple random sampling_ pada tingkat kepercayaan 95%:

| _Sampling error_ | Ukuran Sampel Min. | _Sampling error_ | Ukuran Sampel Min. |
| :--------------: | :----------------: | :--------------: | :----------------: |
|       1,0%       |       10.000       |       5,5%       |        330         |
|       1,5%       |       4.500        |       6,0%       |        277         |
|       2,0%       |       2.500        |       6,5%       |        237         |
|       2,5%       |       1.600        |       7,0%       |        204         |
|       3,0%       |       1.100        |       7,5%       |        178         |
|       3,5%       |        816         |       8,0%       |        156         |
|       4,0%       |        625         |       8,5%       |        138         |
|       4,5%       |        494         |       9,0%       |        123         |
|       5,0%       |        400         |       9,5%       |        110         |
|                  |                    |      10,0%       |        100         |

Hukum yang berlaku secara statistik adalah bahwa untuk mengurangi _sampling error_ menjadi setengahnya (misalnya dari 5,0% menjadi 2,5%), ukuran sampel harus dilipatgandakan sebanyak **empat kali lipat** (dari 400 menjadi 1.600) [1]. Di luar titik tertentu, biaya penambahan unit sampel menjadi tidak proporsional dibandingkan kelebihan presisi yang didapatkan.

### Tabel 2: Ukuran Sampel Berdasarkan Tingkat Homogenitas Populasi

Tabel di atas mengasumsikan distribusi populasi terbelah tepat di tengah (50/50). Untuk populasi di mana proporsi yang besar dari elemennya diharapkan memberikan satu respons yang dominan (lebih homogen), sampel yang lebih kecil cukup tanpa kehilangan presisi [1]. Tabel berikut memetakan kebutuhan ukuran sampel pada variasi ekspektasi respons (_split_) dan berbagai toleransi _sampling error_ pada tingkat kepercayaan 95%:

| Toleransi*Sampling Error* | _Split_ 5/95 | _Split_ 10/90 | _Split_ 20/80 | _Split_ 30/70 | _Split_ 40/60 | _Split_ 50/50 |
| :-----------------------: | :----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: |
|            1%             |    1.900     |     3.600     |     6.400     |     8.400     |     9.600     |    10.000     |
|            2%             |     479      |      900      |     1.600     |     2.100     |     2.400     |     2.500     |
|            3%             |     211      |      400      |      711      |      933      |     1.066     |     1.100     |
|            4%             |     119      |      225      |      400      |      525      |      600      |      625      |
|            5%             |      76      |      144      |      226      |      336      |      370      |      400      |
|            6%             |      —       |      100      |      178      |      233      |      267      |      277      |
|            7%             |      —       |      73       |      131      |      171      |      192      |      204      |
|            8%             |      —       |       —       |      100      |      131      |      150      |      156      |
|            9%             |      —       |       —       |      79       |      104      |      117      |      123      |
|            10%            |      —       |       —       |       —       |      84       |      96       |      100      |

Tanda (—) menunjukkan bahwa ukuran sampel pada kondisi tersebut lazimnya terlalu kecil untuk memungkinkan analisis data secara memadai [1].

Dalam instrumen penelitian multi-tujuan, tiap variabel dapat memiliki ekspektasi _split_ yang berbeda-beda. Keputusan analitis yang tepat dalam kondisi ini adalah mengambil ukuran sampel berdasarkan asumsi variabilitas terbesar (50/50) untuk memitigasi kekurangan data pada variabel kunci [1].

### Catatan: _Sampling Error_ pada Subkelompok

_Sampling error_ berlaku secara eksklusif berdasarkan jumlah unit di dalam sebuah subkelompok, bukan ukuran total sampel. Apabila analisis akan memecah sampel ke dalam subkelompok (misalnya berdasarkan gender atau kategori demografi), presisi estimasi akan menurun tajam saat ukuran subkelompok terlalu sempit. Implikasinya, kebutuhan ukuran sampel total harus dihitung dengan mempertimbangkan ukuran subkelompok yang terkecil [1].

---

## Pendekatan _Power Analysis_

### Konsep Dasar: Empat Parameter yang Saling Terkait

_Power analysis_ adalah metode statistik yang digunakan untuk mengestimasi ukuran sampel minimum yang diperlukan agar suatu pengujian hipotesis dapat dilakukan secara andal [3]. Metode ini menghubungkan empat parameter yang saling berkaitan secara matematis:

**1. _Type I Error_ ($\alpha$)**
Probabilitas menolak hipotesis nol ($H_0$) padahal $H_0$ tersebut sebenarnya benar [4]. Peneliti secara keliru menyimpulkan adanya efek atau perbedaan padahal di populasi hal tersebut tidak ada. Batas toleransi maksimal ditetapkan melalui _alpha level_ ($\alpha$), yang paling umum adalah 0,05 atau 0,01 [4].

**2. _Type II Error_ ($\beta$)**
Probabilitas gagal menolak hipotesis nol padahal $H_0$ tersebut sebenarnya salah [4]. Peneliti gagal mendeteksi efek atau perbedaan yang sesungguhnya ada di populasi.

**3. _Statistical Power_ ($1 - \beta$)**
Probabilitas menolak hipotesis nol secara benar ketika $H_0$ seharusnya ditolak [4]. Ini adalah probabilitas bahwa signifikansi statistik akan berhasil dideteksi jika efeknya memang nyata di populasi. Batas _power_ yang direkomendasikan sebagai standar dalam penelitian adalah **0,80 (80%)** [3].

**4. _Effect Size_**
Estimasi seberapa besar derajat fenomena yang diteliti (misalnya, seberapa kuat korelasi atau seberapa besar selisih rata-rata) di dalam populasi [4]. _Effect size_ memiliki hubungan terbalik dengan kebutuhan ukuran sampel: semakin besar _effect size_ yang diantisipasi, semakin kecil sampel yang dibutuhkan untuk mendeteksinya secara andal [4].

### Prosedur Penentuan Ukuran Sampel

Untuk menentukan ukuran sampel melalui _power analysis_, tiga parameter berikut harus ditetapkan terlebih dahulu [3], [4]:

**Langkah 1 — Mengestimasi _Effect Size_**
Nilai ini biasanya didasarkan pada tinjauan literatur dari penelitian terdahulu atau ditetapkan pada tingkat minimum yang masih bermakna secara substantif [4]. Jika _effect size_ yang diekspektasikan kecil, ukuran sampel yang diperlukan akan lebih besar.

**Langkah 2 — Menetapkan _Alpha Level_ ($\alpha$)**
Penggunaan $\alpha = 0{,}01$ (lebih ketat) akan membutuhkan ukuran sampel yang lebih besar dibandingkan $\alpha = 0{,}05$ untuk mencapai tingkat _power_ yang sama [4].

**Langkah 3 — Menetapkan Target _Power Level_ ($1 - \beta$)**
Target ideal yang umum digunakan adalah 0,80, yang berarti membatasi kemungkinan _Type II error_ ($\beta$) sebesar maksimal 20% [3].

Setelah ketiga parameter ini ditetapkan, perhitungan matematis — yang saat ini sering diotomatisasi dengan perangkat lunak seperti G\*Power, PASS, atau paket `pwr` di R — akan memecahkan persamaan untuk menemukan satu parameter yang tersisa, yaitu jumlah sampel ($N$) yang diperlukan [3].

### Hubungan Antar-Parameter

Hubungan antar-keempat parameter ini bersifat _trade-off_. Tabel berikut merangkum arah perubahan kebutuhan ukuran sampel ketika salah satu parameter diperketat:

| Perubahan parameter                          | Efek terhadap kebutuhan ukuran sampel |
| -------------------------------------------- | ------------------------------------- |
| $\alpha$ diperkecil (misal 0,05 → 0,01)      | Sampel**bertambah**                   |
| Target*power* ditingkatkan (misal 80% → 90%) | Sampel**bertambah**                   |
| _Effect size_ yang diantisipasi lebih kecil  | Sampel**bertambah**                   |
| _Effect size_ yang diantisipasi lebih besar  | Sampel**berkurang**                   |

---

## Referensi

[1] D. de Vaus, _Surveys in Social Research_, 6th ed. Abingdon: Routledge, 2014.

[2] R. Ewing dan K. Park (Eds.), _Basic Quantitative Research Methods for Urban Planners_. New York, NY: Routledge, 2020.

[3] J. F. Hair, W. C. Black, B. J. Babin, dan R. E. Anderson, _Multivariate Data Analysis_, 7th ed. Upper Saddle River, NJ: Pearson Prentice Hall, 2010.

[4] J. F. Healey dan C. Donoghue, _Statistics: A Tool for Social Research and Data Analysis_, 11th ed. Cengage Learning, 2020.

[5] J. Cohen, _Statistical Power Analysis for the Behavioral Sciences_, 2nd ed. Hillsdale, NJ: Lawrence Erlbaum Associates, 1988.

[6] M. N. K. Saunders, P. Lewis, dan A. Thornhill, _Research Methods for Business Students_, 9th ed. Harlow: Pearson Education Limited, 2023.
