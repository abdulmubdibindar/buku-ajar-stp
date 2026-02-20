# Menentukan Ukuran Sampel

Penentuan ukuran sampel dalam penelitian kuantitatif bergantung pada beberapa parameter statistik, yaitu tingkat kepercayaan (_level of confidence_), batas toleransi kesalahan (_margin of error_), dan proporsi atau variabilitas dari populasi yang diteliti [1]. Pendekatan probabilitas menuntut ukuran sampel yang cukup agar inferensi statistik dapat dilakukan secara valid dan representatif terhadap populasi target [2].

## Formula Dasar Penentuan Ukuran Sampel

Untuk menghitung ukuran sampel minimum yang presisi, persamaan yang digunakan didasarkan pada tingkat kepercayaan, rentang kesalahan, dan estimasi proporsi populasi [3]. Rumus perhitungan ukuran sampel ($n$) dinyatakan sebagai berikut:

$$n = p\% \times q\% \times \left( \frac{z}{e\%} \right)^2$$

**Keterangan:**

- $n$ = ukuran sampel minimum yang dibutuhkan.
- $p\%$ = persentase subjek yang termasuk dalam kategori spesifik yang diteliti.
- $q\%$ = persentase subjek yang tidak termasuk dalam kategori spesifik ($100\% - p\%$).
- $z$ = nilai _z-score_ yang berkorespondensi dengan tingkat kepercayaan yang diinginkan (misalnya, $z = 1,96$ untuk tingkat kepercayaan 95%) [3].
- $e\%$ = tingkat kesalahan atau _margin of error_ yang disyaratkan [3].

Apabila proporsi populasi ($p\%$) tidak diketahui sebelum penelitian—misalnya karena tidak ada data _pilot study_—disarankan untuk menggunakan asumsi bahwa 50% sampel memiliki atribut tersebut ($p = 50\%$, $q = 50\%$) [1]. Asumsi $P_u = 0{,}5$ ini merupakan skenario terburuk yang memberikan hasil perkalian maksimum ($0{,}5 \times 0{,}5 = 0{,}25$), sehingga menghasilkan estimasi ukuran sampel yang paling besar (konservatif) [4].

## Penyesuaian Ukuran Sampel untuk Populasi Terhingga

Apabila populasi penarikan sampel relatif kecil (secara umum kurang dari 10.000 kasus), ukuran sampel minimum awal ($n$) yang dihitung dari formula dasar akan melebih-lebihkan jumlah yang sebenarnya dibutuhkan. Dalam situasi populasi terhingga (_finite population_), ukuran sampel dapat diperkecil tanpa mengurangi tingkat akurasi dengan menggunakan rumus penyesuaian berikut [5]:

$$n' = \frac{n}{1 + \left( \dfrac{n}{N} \right)}$$

**Keterangan:**

- $n'$ = ukuran sampel minimum yang telah disesuaikan (_adjusted minimum sample size_).
- $n$ = ukuran sampel minimum yang dihitung dari persamaan formula dasar [5].
- $N$ = ukuran total populasi [5].

Konsep penyesuaian ini merupakan aplikasi dari _finite population correction_ (FPC). Sebagai catatan, _formula Slovin_ yang umum dikenal dengan persamaan $n = N / (1 + N \cdot e^2)$ adalah bentuk penyederhanaan matematis dari koreksi ini yang mematok tingkat kepercayaan 95% dan varians maksimal populasi; namun formulasi tersebut tidak dibahas di dalam literatur saintifik yang dirujuk, dan penggunaannya perlu disertai kehati-hatian terkait asumsi yang melandarinya.

## Penentuan Ukuran Sampel Berdasarkan _Statistical Power_ dan Teknik Multivariat

Selain menggunakan estimasi proporsi, ukuran sampel sangat ditentukan oleh metode analisis data yang digunakan, jumlah variabel, serta kekuatan uji statistik (_statistical power_) yang diharapkan.

### _Power Analysis_

Ukuran sampel berhubungan erat dengan peluang menolak hipotesis nol secara tepat. Secara umum, ukuran sampel harus cukup besar untuk mengamankan nilai _statistical power_ minimal 0,80 (80%) pada tingkat signifikansi $\alpha$ (umumnya 0,05 atau 0,01) berdasarkan _effect size_ yang diantisipasi [6], [7]. Semakin kecil _effect size_ yang dihipotesiskan, semakin besar ukuran sampel yang dibutuhkan untuk mendeteksinya secara reliabel [7].

### Regresi Multipel

Aturan praktis (_rule of thumb_) untuk regresi multipel merekomendasikan rasio minimal 5 observasi untuk setiap variabel independen (5:1). Namun, untuk memastikan hasil yang dapat digeneralisasikan secara optimal, rasio yang diharapkan adalah 15:1 hingga 20:1 [8], [9]. Ukuran sampel juga direkomendasikan berjumlah minimum 50 observasi, dan idealnya 100 atau lebih [9].

### Regresi Logistik

Karena regresi logistik menggunakan pendekatan _Maximum Likelihood Estimation_ (MLE), kebutuhan ukuran sampelnya lebih besar dibandingkan regresi linier standar. Jumlah sampel pada setiap kategori variabel dependen harus sekurang-kurangnya 10 observasi per parameter yang diestimasi [10], [11].

### Analisis Faktor

Untuk mengekstraksi faktor secara stabil, sampel sebaiknya tidak kurang dari 50 observasi, dengan jumlah yang lebih disukai berkisar minimal 100 observasi [12]. Rasio minimum yang disyaratkan adalah 5 observasi per variabel, meskipun rasio 10:1 lebih direkomendasikan guna menghindari _overfitting_ yang spesifik pada sampel tertentu [12], [13].

---

## Referensi

[1] M. N. K. Saunders, P. Lewis, dan A. Thornhill, _Research Methods for Business Students_, 9th ed. Harlow: Pearson Education Limited, 2023.

[2] R. Ewing dan K. Park (Eds.), _Basic Quantitative Research Methods for Urban Planners_. New York, NY: Routledge, 2020.

[3] D. de Vaus, _Surveys in Social Research_, 6th ed. Abingdon: Routledge, 2014.

[4] G. Henry, _Practical Sampling_. Newbury Park, CA: Sage, 1990.

[5] A. Fink, _How to Sample in Surveys_, 2nd ed. Thousand Oaks: Sage, 2002.

[6] J. F. Healey dan C. Donoghue, _Statistics: A Tool for Social Research and Data Analysis_, 11th ed. Cengage Learning, 2020.

[7] J. Cohen, _Statistical Power Analysis for the Behavioral Sciences_, 2nd ed. Hillsdale, NJ: Lawrence Erlbaum Associates, 1988.

[8] J. F. Hair, W. C. Black, B. J. Babin, dan R. E. Anderson, _Multivariate Data Analysis_, 7th ed. Upper Saddle River, NJ: Pearson Prentice Hall, 2010.

[9] G. Kalton, _Introduction to Survey Sampling_, Sage University Paper series on Quantitative Applications in the Social Sciences. Beverly Hills: Sage, 1983.

[10] J. F. Hair, W. C. Black, B. J. Babin, dan R. E. Anderson, _Multivariate Data Analysis_, 7th ed. Upper Saddle River, NJ: Pearson Prentice Hall, 2010.

[11] R. Ewing dan K. Park (Eds.), _Basic Quantitative Research Methods for Urban Planners_. New York, NY: Routledge, 2020.

[12] J. F. Hair, W. C. Black, B. J. Babin, dan R. E. Anderson, _Multivariate Data Analysis_, 7th ed. Upper Saddle River, NJ: Pearson Prentice Hall, 2010.

[13] D. de Vaus, _Surveys in Social Research_, 6th ed. Abingdon: Routledge, 2014.
