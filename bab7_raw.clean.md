Bab 6
Analisis Statistik Inferensial: Uji
Hipotesis Satu Populasi

6.1 Capaian Pembelajaran
Setelah mempelajari bab ini, Anda diharapkan:

    1. Mampu memaknai hasil dari pengujian hipotesis satu
         populasi pada suatu kasus STP-6.1

Agar lebih mudah memahami konsep dasar, Anda dapat
mempelajari studi kasus terlebih dahulu dan menyimak
pembahasan sesuai dengan konsep dasarnya.

6.2 Konsep Dasar
Analisis statistik dengan uji hipotesis digunakan untuk
memperkirakan nilai dari parameter populasi melalui pengujian
hipotesis dengan menggunakan informasi yang diperoleh dari
sampel [2]. Hipotesis sendiri dapat dipahami sebagai dugaan
awal mengenai suatu kondisi, nilai, atau keadaan
parameter. Dugaan ini dapat berasal dari teori, penelitian
sebelumnya, atau klaim tertentu yang ingin diuji. Dalam hal ini,
nilai sampel (statistik) berperan sebagai bukti (evidence)
untuk menguji hipotesis terhadap parameter yang telah
dirumuskan [1, 2].

                                                                               131
Melalui pengujian hipotesis, kita sebagai peneliti akan dapat
menarik kesimpulan (inferensi) mengenai kondisi sebenarnya
pada populasi. Secara sederhana, konsep dasar analisis ini dapat
dianalogikan dengan pertanyaan: "jika rata-rata nilai sampel
adalah X, apakah nilai rata-rata populasinya juga X?" (Gambar
6-1). Kita tidak tahu nilai populasi sebenarnya dan
hanya mengandalkan nilai sampel untuk menguji
hipotesis.

    Gambar 6-1 Ilustrasi Alur Hubungan Karakteristik Populasi, Statistik
                                         Sampel, dan Inferensi

Sebagai contoh yang lebih nyata, khususnya dalam konteks
perencanaan, sering muncul pertanyaan: "Apakah benar
bahwa rata-rata penghasilan penduduk Kota Z berada
di atas UMR?". Pertanyaan ini sebetulnya bukan pertanyaan
yang sulit. Untuk menjawabnya, kita hanya perlu
mengumpulkan data penghasilan seluruh penduduk lalu
kemudian menghitung rata-ratanya. Hanya saja, persoalannya
menjadi rumit saat jumlah populasi penduduk perkotaan yang
datanya akan kita kumpulkan sangat besar (tahukah kamu,
jumlah penduduk untuk kota kecil saja mencapai 10.000 jiwa),
sehingga untuk menjawab pertanyaan tersebut, dilakukan
pengambilan sampel dan prosedur dari analisis inferensial ini.

Selanjutnya, dari sampel sebanyak 350 orang, diketahui
bahwa rata-rata penghasilan mereka berada di atas
UMR. Namun, hal ini belum dapat langsung digunakan untuk

132
menjawab pertanyaan karena data yang kita peroleh hanya dari
350 orang saja. Hal ini kemudian menimbulkan pertanyaan baru:
"Apakah kondisi yang sama (rata-rata di atas UMR)
juga berlaku pada populasi penduduk secara
keseluruhan?" atau "Apakah bukti dari data sampel ini
cukup kuat untuk menolak `dugaan' kita bahwa rata-
rata penghasilan penduduk berada di atas UMR?"

Dalam pengujian hipotesis, kita tidak akan menghitung berapa
nilai rata-rata penghasilan seluruh penduduk (parameternya),
melainkan hanya mengetahui apakah dugaan yang kita miliki
salah (ditolak) atau benar (gagal ditolak).

Lalu bagaimana cara kerja analisis ini, mengapa kita bisa
menggunakan statistik sampel untuk menyimpulkan karakteristik
populasi? Pada dasarnya, proses yang dilakukan adalah
menguji apakah perbedaan atau hubungan yang diamati
dalam sampel cukup kuat untuk disimpulkan berlaku
juga pada populasi.

Maksudnya, sampel hanyalah sebagian kecil dari populasi. Apa
yang kita temukan pada sampel (misalnya rata-rata, perbedaan,
atau hubungan antar-variabel) belum tentu berlaku juga di
populasi. Melalui uji hipotesis, kita memeriksa apakah temuan
dari sampel hanya terjadi karena kebetulan dalam
pengambilan sampel (kesalahan sampling), atau benar-benar
mencerminkan kondisi populasi [1, 2]. Jika hasil dari sampel
terbukti cukup kuat secara statistik, maka kita dapat
menggeneralisasikan kesimpulan tersebut ke populasi.

Adapun kondisi kebetulan ini dapat dijelaskan melalui
pertanyaan berikut: "Apabila pengambilan sampel diulang

                                                                               133
terhadap 350 orang yang berbeda, apakah rata-rata sampelnya
akan tetap berada di atas UMR?" Jika hasilnya konsisten, berarti
temuan tersebut tidak terjadi karena kebetulan. Hal ini menjadi
indikasi bahwa data sampel cukup kuat untuk mencerminkan
populasi. Namun, jika hasilnya berbeda, maka ada kemungkinan
bahwa perbedaan tersebut muncul akibat kebetulan atau faktor
kesalahan dalam pengambilan sampel.
Coba perhatikan Gambar 6-2. Pada dasarnya nilai populasi
sangat beragam, dan rata-rata populasi hanya menunjukkan
kecenderungan umum dari nilai-nilai tersebut. Namun, dalam
praktiknya kita mungkin menemukan data responden yang
nilainya sangat jauh berbeda dari rata-rata (pencilan/outlier).
Nilai pencilan ini dapat mengganggu representasi data dan
membuat sampel terlihat tidak mewakili kondisi populasi secara
keseluruhan.

        Gambar 6-2 Hubungan Statistik Sampel dan Parameter Populasi

Selanjutnya, mari kita lihat contoh kasus yang lain. Sebagai
bentuk evaluasi terhadap implementasi perencanaan dan

134
pembangunan kota, diperlukan evaluasi program berdasarkan
sudut pandang maysarakat sebagai penerima layanan.

Misalnya, pemerintah ingin mengevaluasi keberhasilan program
pemerintah Makan Bergizi Gratis (MBG) di Kota Bandar
Lampung. Untuk itu, pemerintah melakukan survei untuk
menjaring skor kepuasan masyarakat penerima manfaat
program dengan angka 0­100. Dalam hal ini, dapat ditetapkan
sebuah indikator bahwa program dianggap berhasil apabila
skor kepuasan masyarakat penerima layanan mencapai
angka 80 atau lebih.

Dengan demikian, apabila hasil survei menunjukkan skor
kepuasan masyarakat berada di atas angka tersebut, maka
program dapat dinilai berhasil sesuai indikator yang telah
ditetapkan. Dalam contoh ini, skor kepuasan masyarakat
sebesar 80 atau lebih adalah dugaan yang ingin kita
telusuri sebagai bentuk hipotesis yang akan diuji.

Selanjutnya, dilakukan survei kepada 200 orang responden
secara acak. Dari responden ini, diketahui bahwa skor kepuasan
responden berada di angka 85. Lalu, pertanyaannya: "apakah
secara keseluruhan, yaitu pada seluruh anggota populasi di Kota
Bandar Lampung, skor kepuasan terhadap program MBG benar-
benar mencapai lebih dari 80 sehingga program MBG dapat
dikatakan berhasil?".

Selanjutnya, analisis dilakukan untuk membuktikan apakah nilai
statistik, yaitu skor kepuasan sebesar 85 dari 200 responden,
benar-benar dapat mencerminkan kondisi populasi atau
hanya muncul karena kebetulan dalam proses pengambilan
sampel. Dengan kata lain, data sampel yang menunjukkan skor

                                                                               135
kepuasan 85 dijadikan dasar untuk menguji apakah hipotesis
dapat ditolak atau tidak.

Catatan 6-1

Hasil dari pengujian hipotesis hanya memiliki dua kemungkinan,
yaitu menolak atau gagal menolak hipotesis (hipotesis
kosong, H). Menolak hipotesis berarti menyetujui bahwa
kondisi yang terjadi justru merupakan `kebalikan' atau `antitesis'
dari dugaan awal. Sebaliknya, gagal menolak hipotesis berarti
kita tidak menemukan cukup bukti untuk menolak hipotesis,
sehingga secara tidak langsung kita "menerima" bahwa hipotesis
tersebut masih mungkin benar.

Istilah yang digunakan adalah gagal menolak, bukan menerima,
karena dalam pendekatan statistik kita tidak pernah
membuktikan bahwa hipotesis (H) benar. Fokus pengujian
statistik adalah mencari kemungkinan untuk menolak hipotesis,
bukan membuktikan kebenarannya. Dengan cara pandang ini,
proses pengolahan data menjadi lebih mudah dipahami: kita
mencari bukti untuk menolak dugaan awal, bukan membuktikan
bahwa dugaan itu pasti benar.

6.2.1 Perbedaan Estimasi Parameter dengan Uji
           Hipotesis

Estimasi parameter dan uji hipotesis memiliki tujuan yang
berbeda. Estimasi parameter menghasilkan suatu rentang nilai
yang mungkin bagi parameter populasi. Pertanyaan yang
dijawab biasanya berbentuk: "Berapa kira-kira nilai rata-rata
populasi X?"

136
Sementara itu, uji hipotesis berfokus pada penerimaan atau
penolakan dugaan kita tentang parameter populasi. Pertanyaan
yang diajukan lebih ke arah: "Jika saya menduga bahwa rata-
rata populasi X adalah Y, apakah dugaan tersebut dapat
diterima?"

Jadi, melalui pengujian hipotesis kita tidak akan bicara `berapa
nilainya...?' tetapi untuk membuktikan dugaan dalam bentuk
hipotesis `apakah benar jika?...'

6.2.2 Hipotesis Kosong dan Hipotesis Alternatif
Dalam pengujian hipotesis, terdapat dua jenis hipotesis, yaitu
hipotesis kosong (H) dan hipotesis alternatif (H atau Ha)
yang masing-masing akan dijelaskan dengan rinci sebagai
berikut.

6.2.2.1 Hipotesis kosong
Hipotesis kosong muncul dari prinsip ilmiah bahwa "pengetahuan
harus dapat dibuktikan oleh data". Artinya, peneliti tidak dapat
langsung menyatakan adanya perbedaan atau hubungan tanpa
adanya bukti yang kuat. Oleh karena itu, hipotesis kosong
digunakan sebagai titik awal yang logis dengan
menganggap bahwa tidak ada perbedaan atau tidak ada
hubungan antara kondisi yang diamati dan dugaan yang
dimiliki [2].

Dengan kata lain, hipotesis kosong menggambarkan kondisi
netral atau standar yang dapat dijadikan dasar pembuktian.
Dari sinilah kemudian pengujian dilakukan untuk melihat
apakah ada cukup bukti untuk menolak H dan `menerima
hipotesis alternatif ' ataupun tidak.

                                                                               137
Melanjutkan contoh MBG, misalkan kita memiliki dugaan:
"apakah benar bahwa program MBG berhasil dengan memberikan
kepuasan kepada masyarakat?". Dalam hal ini, ada dua
kemungkinan kondisi yang terjadi: 1) program tidak
memberikan dampak apa-apa sehingga masyarakat tidak
memberikan rata-rata nilai kepuasan di atas 80; atau 2) program
berhasil sehingga masyarakat puas dan memberikan rata-rata
skor kepuasan di atas 80.

Kemungkinan pertama, yaitu "program tidak memberikan
dampak apa-apa sehingga masyarakat tidak memberikan rata-
rata nilai kepuasan di atas 80", menggambarkan kondisi netral
atau tidak ada perbedaan. Oleh karena itu, pernyataan ini
dijadikan sebagai hipotesis kosong (H) dan dituliskan dengan
simbol persamaan (=). Secara matematis, hipotesis kosong
untuk rata-rata skor kepuasan ini dapat dinyatakan sebagai
berikut (perhatikan penulisan notasi parameter populasi
di subbab 5.2.1, rata-rata populasi dinotasikan dengan
):

                                   H:  = 

Notasi  menunjukkan nilai dugaan (hipotesis) yang kita miliki.
Dalam kasus ini, karena kita menetapkan nilai minimal
masyarakat "puas" adalah pada rata-rata skor = 80, dugaan
terhadap rata-rata skor kepuasan populasi adalah 80, sehingga
 = 80. Berdasarkan kondisi tersebut, penulisan hipotesis dapat
dirumuskan kembali sebagai berikut:

                                 H :  = 80

Hipotesis nol menyatakan bahwa nilai parameter populasi tidak
berbeda (sama) dengan nilai yang diduga. Secara sederhana, hal

138
ini dapat dimaknai sebagai: "nilai rata-rata sampel X yang
dijadikan bukti tidak cukup kuat untuk menolak H". Dengan
demikian, kondisi yang diasumsikan dalam hipotesis nol
dianggap masih berlaku, atau dengan kata lain, hipotesis nol
gagal ditolak.

6.2.2.2 Hipotesis alternatif
Sementara itu, hipotesis alternatif (H) adalah dugaan awal
mengenai kondisi yang berbeda (antitesis) dari keadaan
netral atau standar yang diasumsikan dalam hipotesis kosong
[2]. Dengan kata lain, hipotesis alternatif menyatakan adanya
perbedaan atau hubungan yang ingin dibuktikan peneliti.

Hipotesis alternatif ini dapat berbentuk tidak berarah,
misalnya hanya menyatakan "ada perbedaan" tanpa
menyebutkan ke arah mana perbedaannya, atau berarah, yaitu
menyatakan secara spesifik bahwa suatu kondisi "lebih besar",
"lebih kecil", atau "lebih tinggi" dibandingkan standar yang
ada.

Secara rinci ragam bentuk hipotesis alternatif ini adalah sebagai
berikut [12]:

    1. Kasus "tidak sama dengan"  digunakan ketika dugaan
         hanya menyatakan"ada perbedaan", tanpa
         menyebutkan lebih besar atau lebih kecil.

    2. Kasus "lebih dari"  digunakan ketika dugaan
         menyatakan bahwa parameter populasi lebih besar
         daripada nilai dugaan.

    3. Kasus "kurang dari"  digunakan ketika dugaan
         menyatakan bahwa parameter populasi lebih kecil
         daripada nilai dugaan.

                                                                               139
Adapun bentuk matematis dari hipotesis alternatif yang
mungkin dipilih ditampilkan pada Tabel 6.1 berikut.

     Tabel 6.1 Alternatif Bentuk Hipotesis Alternatif

No   Bentuk    Persamaan  Interpretasi

     kasus     matematis

I Tidak sama H1:    Rata-rata parameter tidak sama

     dengan               dengan nilai dugaan ()

II Lebih dari  H1:  >  Rata-rata parameter lebih besar

                          nilai dugaan ()

III Kurang dari H1:  <  Rata-rata parameter tidak sama

                          dengan nilai dugaan ()

Melanjutkan contoh pada bagian sebelumnya, hipotesis
alternatif akan mencerminkan kemungkinan kondisi ke-2, yaitu
"program memberikan dampak sehingga nilainya bukan
80/berbeda dari 80". Ini adalah contoh kasus untuk bentuk tidak
berarah karena menggunakan pertidaksamaan (ada kata
"berbeda").

Walaupun bentuk ini bisa digunakan, hasilnya tidak lebih
informatif dibandingkan kita menentukan arahnya (lebih
besar/lebih kecil). Jika kita menggunakan kata lebih-dari atau
kurang-dari dalam perumusan hipotesis alternatif kita, maka
hipotesis alternatif kita memiliki arah, dan kita akan
menggunakan < atau > dalam bentuk persamaan matematisnya.

Memilih tanda atau arah pertidaksamaan dalam perumusan
hipotesis alternatif berarah sangat penting karena ini
menentukan posisi wilayah kritis pada kurva distribusi
statistik sampel, yang menjadi dasar dalam pengujian hipotesis.

140
Posisi ini disebut "tail" (ekor) yang merupakan istilah untuk
posisi wilayah kritis sebagaimana yang dijelaskan lebih rinci
pada subbab 6.2.3.

Catatan 6-2

Hipotesis kosong, atau sering juga disebut sebagai hipotesis nol
(H), biasanya disimbolkan dengan tanda sama dengan (=),
karena menggambarkan kondisi standar atau tidak ada
perbedaan.

Sebaliknya, hipotesis alternatif, atau sering juga disebut sebagai
hipotesis penelitian (H) menunjukkan kondisi yang berlawanan
dengan hipotesis kosong. Bentuknya bisa tidak berarah, ditandai
dengan simbol tidak sama dengan (), atau berarah, ditandai
dengan simbol lebih dari (>) atau kurang dari (<) sesuai arah
dugaan yang ingin diuji.

6.2.3 Titik Kritis dan p-value
Pengujian hipotesis dilakukan dengan menggunakan dua
pendekatan utama, yaitu titik kritis dan nilai p (p-value), yang
keduanya didasarkan pada konsep distribusi statistik
sebagaimana dijelaskan pada subbab 4.2.8.

6.2.3.1 Titik kritis dan wilayah kritis
Secara lebih rinci, titik kritis adalah nilai pada distribusi
sampling (distribusi statisik sampel) yang menandai batas awal
dari suatu area yang disebut wilayah kritis (critical region) atau
wilayah penolakan. Wilayah kritis ini mencakup hasil sampel
yang dianggap "tidak mungkin" terjadi apabila hipotesis kosong
benar [2]. Praktisnya, titik kritis menjadi pemisah kedua area

                                                                               141
untuk menentukan apakah H ditolak atau gagal ditolak
(Gambar 6-3).

Penentuan titik kritis didasarkan pada tingkat signifikansi
(alpha, ), yang dalam ilmu sosial umumnya ditetapkan sebesar
5% atau 0,05. Nilai titik kritis ini diperoleh dari tabel distribusi,
yaitu Tabel Z untuk ukuran sampel besar (dan Tabel t untuk
ukuran sampel kecil). Dalam hal ini, dapat kita disepakati
bahwa ukuran sampel besar adalah jumlah sampel lebih dari
100, sedangkan sampel dengan jumlah 100 atau kurang
digolongkan sebagai sampel kecil [6, 1] (baca Teorema Limit
Sentral, subbab 4.2.5).

Distribusi wilayah kritis ditentukan oleh bentuk hipotesis
alternatif yang telah dirumuskan. Masing-masing bentuk
hipotesis alternatif (tidak sama dengan, kurang dari, dan lebih
dari) akan mempengaruhi letak wilayah kritis pada kurva
distribusi sampling.

1) Kasus tidak sama dengan (two tailed)
Kasus tidak sama dengan adalah bentuk hipotesis tanpa arah,
sehingga wilayah kritis akan terbagi dua secara sama rata di
ekor (tail) kurva. Apabila kita menetapkan =5%, maka masing-
masing ekor akan menampung /2 = 2,5%. Dalam hal ini, titik
kritis dihitung berdasarkan nilai /2.

2) Kasus lebih dari (right tailed)
Selanjutnya untuk bentuk lebih dari, wilayah kritis hanya
berada di ekor kanan kurva. Dengan  = 5%, titik kritis
ditentukan langsung berdasarkan nilai  tersebut.

142
3) Kasus kurang dari (left tailed)
Wilayah kritis akan berada di ekor sebelah kiri. Sama halnya
dengan bentuk lebih dari, nilai titik kritis ditentukan langsung
berdasarkan nilai  yang digunakan. Pengujian pada hipotesis
ini memiliki bentuk kurva right tailed.

        Gambar 6-3 Ilustrasi Titik Kritis pada Kurva Distribusi Normal

Setelah wilayah kritis dan titik kritis ditetapkan, nilai statistik
uji (Z-score ataupun t-score) dihitung dari data sampel, lalu
dibandingkan dengan titik kritis tersebut. Jika Z-score jatuh
ke dalam area penerimaan H, maka dapat disimpulkan
bahwa hipotesis kosong tidak ditolak (H dianggap
benar untuk kasus yang diuji).
6.2.3.2 Nilai Statistik Uji dan Nilai p (p-value)
Setelah wilayah kritis dan titik kritis ditetapkan, nilai statistik
uji (Z-score ataupun t-score) dihitung dari data sampel, lalu

                                                                               143
dibandingkan dengan titik kritis tersebut. Jika nilai statistik
uji jatuh di dalam wilayah kritis, maka dapat
disimpulkan bahwa hipotesis kosong ditolak (H1 gagal
ditolak untuk kasus yang diuji). Sebaliknya, jika nilai
tersebut jatuh di luar wilayah kritis, maka hipotesis
kosong gagal ditolak (H1 ditolak untuk kasus yang diuji).
Penjelasan tersebut diilustrasikan oleh Gambar 6-4 (a) dan (b)
secara berturut-turut.

                        wilayah kritis ( atau /2)
                        p-value

                                                                          Statistik Uji

(a)                 titik kritis

     Statistik Uji

                                                 (b)
                                                                      titik kritis

Gambar 6-4. Ilustrasi Penetapan Hipotesis yang Ditolak (untuk Satu Ekor)

Sementara itu, nilai p (p-value) adalah probabilitas untuk
memperoleh hasil sampel seperti yang kita amati, atau bahkan
hasil yang lebih ekstrem, dengan asumsi bahwa hipotesis
kosong (H) benar. Dengan kata lain, nilai p menunjukkan
seberapa besar kemungkinan hasil yang kita peroleh dari sampel

144
muncul hanya karena kebetulan, apabila pada populasi
sebenarnya tidak ada perbedaan atau hubungan apa pun.

Saat ini, perangkat lunak statistik modern (Excel, R, SPSS, dsb)
secara otomatis menghitung nilai p dari data yang dianalisis.
Nilai p tersebut kemudian dibandingkan dengan tingkat
signifikansi () yang sudah ditentukan. Jika nilai p lebih
besar dari , maka dapat disimpulkan bahwa H gagal
ditolak (tidak ada cukup bukti untuk menolak hipotesis
kosong).

Catatan 6-3

Kaidah pengujian hipotesis terkait titik kritis dan nilai p adalah
sebagai berikut:

Jika Z-score jatuh ke dalam area penolakan H, nilai p < ,
maka H ditolak  kondisi yang berlaku adalah H1

Jika Z-score jatuh ke dalam area penerimaan H, nilai p > 
maka dapat disimpulkan bahwa H gagal ditolak  kondisi
yang berlaku adalah H

6.2.4 Langkah-langkah Pengujian Hipotesis
Berikut adalah rangkuman langkah-langkah pengujian hipotesis.
Proses ini memungkinkan peneliti menarik kesimpulan (inferensi)
tentang populasi yang lebih besar berdasarkan data dari sampel
yang lebih kecil.

Agar lebih mudah dipahami, langkah-langkah pengujian
hipotesis ini akan dibahas melalui studi kasus sederhana evaluasi
keberhasilan program Makan Bergizi Gratis (MBG) yang telah

                                                                               145
diuraikan sebelumnya (lihat kembali subbab 6.2 Konsep
Dasar).

Pada kasus ini, evaluasi dilakukan dengan menyurvei skor rating
kepuasan penerima layanan MBG yang berkisar antara 0­100.
Pertanyaan yang ingin dijawab dari survei ini adalah: "apakah
benar bahwa skor kepuasan masyarakat penerima
layanan mencapai skor 80?"

Berdasarkan hasil survei terhadap sampel berukuran 200 orang,
diperoleh informasi bahwa rata-rata skor tingkat kepuasannya
adalah 95 dengan standar deviasi 2,3. Dan dengan tingkat
kepercayaan 95%, akan dilakukan pengujian hipotesis sebagai
dasar untuk menentukan apakah program MBG dapat
dikatakan berhasil sesuai indikator yang ditetapkan.

6.2.4.1 Membuat asumsi
Untuk dapat menyelesaikan kasus melalui pengujian hipotesis,
kita sebagai peneliti harus memastikan bahwa: proses
pengambilan sampel telah dilakukan secara acak dan
memenuhi persyaratan statistik. Persyaratan statistik
tersebut adalah distribusi sampling-nya (distribusi statistik
sampelnya) mengikuti distribusi normal. Berikut adalah
penjelasannya:

a. responden dipilih secara acak (random) sesuai kaidah
     pengambilan sampel probabilistik  proses sampling
     terhadap 200 responden dilakukan menggunakan teknik
     sampling acak (random sampling)

b. Distribusi statistik sampel mengikuti distribusi normal 
     dapat dipenuhi oleh jumlah sampel yang besar [6] (lihat
     subbab 4.2.4)

146
Perlu diperhatikan bahwa kita akan menguji hipotesis untuk
rata-rata. Oleh karena itu variabel kita harus bisa dipastikan
bertingkat pengukuran minimal metrik. Variabel yang akan
diuji di sini adalah skor kepuasan yang merupakan variabel
interval, maka uji hipotesis dapat dilanjutkan.

6.2.4.2 Merumuskan hipotesis (H dan H1)
Langkah selanjutnya adalah menerjemahkan masalah penelitian
ke dalam pernyataan yang dapat diuji, yaitu hipotesis. Hipotesis
ini biasanya dapat dikenali dari tujuan penelitian, pertanyaan
yang diajukan, atau target yang ingin dicapai dalam kasus yang
sedang dianalisis.

Dalam kasus penilaian keberhasilan program Makan Bergizi
Gratis (MBG), ditetapkan indikator bahwa program dinyatakan
berhasil apabila skor kepuasan masyarakat mencapai
skor 80.

Oleh karena hipotesis kosong mengandung makna bahwa tidak
ada dampak/tidak ada perbedaan antara pemberian
program atau tidak, artinya nilai 80 kita tetapkan sebagai
rata-rata skor di mana masyarakat tidak merasakan kepuasan
terhadap program tersebut. Ini dapat dijadikan dasar awal
pengujian, yaitu hipotesis kosong (H).

Selanjutnya, sebagai antitesis dari H, hipotesis alternatif (H)
harus mengikuti bentuk-bentuk yang ada di Adapun bentuk
matematis dari hipotesis alternatif yang mungkin dipilih
ditampilkan pada Tabel 6.1 berikut.

Tabel 6.1, yakni bentuk two-tailed test (kasus 1), atau right-
tailed test (kasus 2) dan kasus ke-3 (left-tailed test). Bentuk two-
tailed test (kasus 1) atau right-tailed test (kasus 2) kurang tepat

                                                                               147
untuk digunakan dalam kasus ini, karena ketidaksamaan dengan
skor 80 (misalnya 90, 91, atau 100) justru masih termasuk ke
dalam kondisi H yang kita uji.

Berdasarkan hipotesis kosong, hipotesis alternatif kita adalah
"program ini berhasil sehingga memberikan rata-rata skor
kepuasan >80." Oleh karena itu, bentuk persamaan hipotesis
dari kasus yang kita miliki adalah sebagai berikut:

                   H:  =  = 80 atau H:  = 80

                   H1:  >  = 80 atau H1:  > 80

Pada hipotesis yang telah dirumuskan, H0 menunjukkan kondisir
rata-rata skor kepuasan masyarakat mencapai angka 80. Kondisi
ini akan mengindikasikan adanya keberhasilan Program MBG.
Sementara itu, H1 menunjukkan kondisi rata-rata skor kepuasan
masyarakat tidak mencapai angka 80. Kondisi ini
mengindikasikan adanya ketidakberhasilan program MBG.

Sementara itu, H1 menunjukkan keadaan sebaliknya. Statistik
skor kepuasan yang <80 benar-benar mewakili kondisi
keseluruhan (parameternya). Artinya, hipotesis bahwa
masyarakat cukup puas dengan program MBG gagal diterima.

6.2.4.3 Memilih distribusi sampling dan menentukan wilayah
             serta titik kritis

Distribusi sampling dipilih dengan mempertimbangkan jumlah
atau ukuran sampel yang digunakan. Sementara itu, wilayah
kritis ditetapkan berdasarkan bentuk hipotesis yang telah
dikembangkan (lihat subbab 6.2.3).

148
1. Ukuran sampel adalah 200 responden, sehingga dapat
    dikategorikan sebagai sampel besar. Oleh karena itu,
    distribusi sampling yang digunakan adalah Distribusi Z.

2. Hipotesis alternatif yang digunakan berbentuk lebih dari
    (right-tailed test), sehingga wilayah kritis berada di ekor
    sebelah kanan kurva distribusi.

3. Dengan tingkat kepercayaan 95% ( = 5%), nilai Z yang
    menjadi batas wilayah kritis adalah +1,65. Adapun
    gambaran dari distribusi sampling dan wilayah kritis ini
    dapat dilihat pada Gambar 6-5. (Zkritis = +1,65)

6.2.4.4 Menghitung statistik uji
Perhitungan statistik uji, dalam hal ini adalah Z-score, dapat
dihitung dengan rumus sebagai berikut.

  =    - 0
       

        Gambar 6-5 Distribusi Sampling dan Wilayah Kritis Kasus MBG

Perhitungan SE sendiri, sebagaimana yang sudah kita pelajari
pada 4.2.6, dijabarkan menjadi rumus berikut:

                                                                               149
       =    - 0
             

            

Untuk menghitung statitstik uji, akan lebih mudah jika kita
dapat merangkum terlebih dahulu semua informasi penting yang
diberikan.

Pada kasus yang sedang diuji, beberapa informasi penting yang
dapat dirangkum adalah sebagai berikut:

     · x (rata-rata sampel) = 95
     ·  (nilai dugaan, atau rata-rata populasi H) = 80
     · s (standar deviasi sampel) = 2,3
     · n (ukuran sampel) = 200

Maka perhitungan statistik uji Z-score dari kasus adalah sebagai
berikut:

                                                 95 - 80
                                            = 2,3

                                                  200
                                                   15
                                             = 0,1626
                                             = 92,25

Dengan begitu, dapat kita ketahui bahwa statistik uji (Z-score,
atau Zhitung) adalah +92,25.

6.2.4.5 Menarik kesimpulan

Langkah terakhir adalah membandingkan nilai statistik uji
dengan wilayah kritis untuk membuat keputusan. Proses ini
dapat dilakukan dengan mudah melalui ilustrasi distribusi
normal yang menunjukkan wilayah kritis.

Pada tahap ini, peneliti menetapkan keputusan akhir: apakah
nilai statistik uji jatuh pada wilayah penolakan H,

150
sehingga hipotesis kosong ditolak, atau justru berada di
luar wilayah tersebut, sehingga H gagal ditolak.
Pada kasus, nilai statistik uji dan titik kritis adalah:

                               Zhitung = +92,25
                                Zkritis = +1,65
sehingga keputusannya adalah nilai statistik uji jatuh jauh ke
dalam wilayah kritis. Bahkan, nilai ini berada jauh di sisi kanan
grafik. Oleh karena itu, hipotesis kosong dapat ditolak
(Gambar 6-6).
6.2.4.6 Memaknai hasil pengujian hipotesis
Dengan merumuskan hipotesis kosong (H) sebagai = 80, hasil
pengujian menunjukkan bahwa kita tidak menemukan
bukti statistik untuk menyimpulkan bahwa program
tidak memberikan dampak kepuasan sehingga tidak bisa
dikatakan tidak berhasil. Rata-rata skor kepuasan sampel
yang diperoleh, yaitu 95, berada jauh di atas ambang batas,
yakni 80. Hal ini membuat kemungkinan bahwa parameter skor
kepuasan berada di bawah angka 80 menjadi sangat kecil.

                                                                               151
  Gambar 6-6 Penarikan Kesimpulan Statistik Hitung dan Wilayah Kritis

Berdasarkan pengujian ini, kita tidak memiliki bukti untuk
menolak hipotesis kosong. Sebaliknya, hasil sampel justru sangat
mendukung hipotesis kosong bahwa program MBG berhasil,
sesuai dengan indikator rata-rata skor kepuasan masyarakat
yang ditetapkan ( 80).

6.3 Studi Kasus
Dengan menggunakan data pada subbab sebelumnya mengenai
jarak tempat tinggal mahasiswa ITERA menuju
kampus dari 333 responden, pihak kampus merespons
kebutuhan mobilitas mahasiswa dengan merencanakan
penyediaan layanan Bus Kampus. Namun, layanan ini hanya
akan efektif jika mayoritas mahasiswa tinggal pada jarak dekat
( 5 km) dari kampus dan apabila lebih dari 80% mahasiswa
berminat terhadap layanan tersebut. Sebagai informasi awal
bahwa pengambilan data yang dilakukan telah sesuai dengan
prinsip probabilitas dan data yang terkumpul memiliki
distribusi normal.

152
6.3.1 Pengujian hipotesis rata-rata populasi
Apabila rata-rata jarak tempat tinggal mahasiswa memang
berada pada 5 km atau kurang, maka penyediaan Bus Kampus
dapat dianggap tepat dan efektif. Berdasarkan data sampel
tersebut, diketahui bahwa rata-rata jarak tempat tinggal
mahasiswa dari kampus adalah sebesar 4,59 km dengan
simpangan baku yaitu 2,23 km. Selanjutnya dengan tingkat
kepercayaan 95%, kita akan melakukan pengujian terhadap
rata-rata populasi mahasiswa ITERA tersebut.

6.3.1.1 Membuat asumsi
Berdasarkan informasi awal yang dimiliki, kita dapat membuat
asumsi yang sesuai dengan syarat pengujian hipotesis sebagai
berikut:

a. Sampling telah memenuhi prinsip probabilitas
b. Distribusi sampling mengikuti distribusi normal (hal ini

     juga didukung oleh jumlah sampel besar (n=333) yang
     telah dikumpulkan

Selain itu, tingkat pengukuran variabel berada pada skala
interval-rasio (jarak tempat tinggal dari kampus), sehingga
dilakukan uji hipotesis rata-rata.

6.3.1.2 Merumuskan hipotesis (H dan H1)
Dalam kasus, terdapat dua pernyataan penting yang menjadi
dasar perumusan hipotesis, yaitu:

    1. "...merencanakan penyediaan layanan Bus Kampus..."
    2. "Apabila rata-rata jarak tempat tinggal

         mahasiswa memang berada pada 5 km atau
         kurang, maka penyediaan Bus Kampus dapat dianggap
         tepat dan efektif."

                                                                               153
Dua pernyataan tersebut menunjukkan tujuan kebijakan yang
ingin divalidasi, yaitu apakah benar rata-rata jarak tempat
tinggal mahasiswa ke kampus adalah 5 km atau kurang.

Dari sini muncul pertanyaan: "Apakah benar bahwa rata-rata
tempat tinggal mahasiswa adalah 5 km atau kurang?"

Pertanyaan ini mengindikasikan bentuk persamaan (),
sehingga dapat dijadikan dasar untuk merumuskan hipotesis
kosong (H).

Selanjutnya, sebagai antitesis dari H, maka hipotesis alternatif
(H) dirumuskan dalam bentuk right-tailed test. Artinya, jika H
menyatakan bahwa rata-rata jarak tempat tinggal mahasiswa
adalah  5 km, maka H menyatakan kebalikannya, yaitu > 5
km.

Oleh karena itu, kalimat hipotesis kosong dan alternatif dari
kasus yang kita miliki adalah sebagai berikut:

               H:  =  = 5 km atau H:  = 5 km

               H1:  >  = 5 km atau H1:  > 5 km

Pada hipotesis yang telah dirumuskan, H menunjukkan kondisi
bahwa rata-rata jarak tempat tinggal mahasiswa dari kampus
adalah 5 km atau dengan kata lain sama dengan 5 km.
Sementara itu, H menunjukkan kondisi bahwa rata-rata jarak
tempat tinggal mahasiswa dari kampus adalah lebih dari 5 km.
Jika kondisi ini terbukti, maka penyediaan Bus Kampus justru
memiliki potensi yang lemah dalam mendukung efektivitas
layanan transportasi mahasiswa.

154
6.3.1.3 Memilih distribusi sampling dan menentukan wilayah
             kritis

Berdasarkan informasi yang telah diberikan pada kasus, dapat
disimpulkan:

  1. Ukuran sampel adalah 333 responden, sehingga dapat
       dikategorikan sebagai sampel besar. Oleh karena itu,
       distribusi sampling yang digunakan adalah Distribusi Z.

  2. Hipotesis alternatif yang digunakan berbentuk lebih dari
       dari (right-tailed test), sehingga wilayah kritis berada di
       ekor sebelah kanan kurva distribusi.

  3. Dengan tingkat kepercayaan 95% ( = 5%), nilai Z yang
       menjadi batas wilayah kritis adalah +1,65. Adapun
       gambaran dari distribusi sampling dan wilayah kritis ini
       dapat dilihat pada Gambar 6-7. (Zkritis = +1,65)

6.3.1.4 Menghitung statistik uji
Berdasarkan kasus yang telah diuraikan, dapat rangkum:

    · x (rata-rata sampel) = 4,59 km
    ·  (nilai dugaan, atau rata-rata populasi H) = 5 km
    · s (standar deviasi sampel) = 2,25 km
    · n (ukuran sampel) = 333

                                                                               155
                 Gambar 6-7 Distribusi Sampling dan Wilayah Kritis.

maka perhitungan statistik uji Z-score dari kasus adalah sebagai
berikut:

                                       4,59 - 5
                                  = 2,33

                                         333
                                    = -3,36
Dengan demikian, nilai statistik uji yang diperoleh adalah: -3,36
6.3.1.5 Menarik kesimpulan
Pada kasus, nilai statistik uji dan titik kritis adalah:
                                Zhitung = -3,36
                                Zkritis = +1,65
sehingga keputusannya adalah nilai statistik uji tidak jatuh ke
dalam wilayah kritis sehingga hipotesis kosong gagal ditolak
(Gambar 6-8).

156
  Gambar 6-8 Penarikan Kesimpulan Statistik Hitung dan Wilayah Kritis

6.3.1.6 Memaknai Hasil Pengujian Hipotesis
Dengan merumuskan hipotesis kosong (H) sebagai = 5 km,
hasil pengujian menunjukkan bahwa kita tidak menemukan
bukti statistik kuat untuk untuk menyimpulkan bahwa
hipotesis ini gagal. Hasil sampel mendukung H, yaitu bahwa
rata-rata jarak mahasiswa ITERA ke kampus adalah 5 km atau
kurang.

Dengan demikian berdasarkan data yang diperoleh, penyediaan
Bus Kampus dapat dianggap tepat dan berpotensi
efektif. Kedepannya, kita dapat merekomendasikan kajian lebih
teknik untuk menindaklanjuti program Bus Kampus mencakup
rute, titik pemberhentian, dan waktu perjalanan. Program Bus
Kampus ini selain dapat memberikan kemudahan bagi
mahasiswa untuk melakukan pergerakan menuju kampus,
program ini juga dapat menekan potensi emisi yang ditimbulkan
dari penggunaan kendaraan bermotor dan mendukung
pencapaian transporasi berkelanjutan di lingkungan pendidikan
kampus Institut Teknologi Sumatera.

                                                                               157
6.3.2 Pengujian hipotesis proporsi populasi
Selanjutnya, terkait minat mahasiswa menggunakan Bus
Kampus. Pihak kampus menilai bahwa keberhasilan program
juga sangat bergantung pada minat mahasiswa sebagai calon
pengguna. Minat yang tinggi mencerminkan potensi efektivitas
program dan mendukung pencapaian tujuan yang lebih besar,
khususnya apabila lebih dari 80% mahasiswa berminat
terhadap layanan tersebut. Berdasarkan survei terhadap 333
responden, diketahui 70% mahasiswa berminat. Dengan
tingkat kepercayaan 99%, kitahipotesis proporsi terhadap
minat tersebut.

6.3.2.1 Membuat asumsi
Berdasarkan informasi awal yang dimiliki, kita dapat membuat
asumsi yang sesuai dengan syarat pengujian hipotesis sebagai
berikut:

a. Sampling telah memenuhi prinsip probabilitas
b. Distribusi sampling mengikuti distribusi normal (hal ini

     juga didukung oleh jumlah sampel besar (n=333) yang
     telah dikumpulkan

Selain itu, tingkat pengukuran variabel berada pada skala
nominal (jawaban berminat/tidak berminat), sehingga
dilakukan uji hipotesis proporsi.

6.3.2.2 Merumuskan hipotesis (H dan H1)
Dalam kasus, terdapat dua pernyataan penting yang menjadi
dasar perumusan hipotesis, yaitu:

1. "...merencanakan penyediaan layanan Bus Kampus..."
2. "Apabila lebih dari 80% mahasiswa berminat...."

158
Dua pernyataan tersebut menunjukkan tujuan kebijakan yang
ingin divalidasi, yaitu apakah benar terdapat lebih dari 80%
mahasiswa yang berminat.

Dari sini muncul pertanyaan: "Apakah benar bahwa terdapat
lebih dari 80% mahasiswa yang berminat?"

Pertanyaan ini mengindikasikan bentuk pertidaksamaan lebih
dari (>), sehingga tidak dapat dijadikan sebagai kondisi netral
H. Dugaan ini merujuk pada kondisi hipotesis alternatif (H)
pada bentuk kasus 3 (right-tailed).

Oleh karena itu, bentuk kondisi netral yang dapat dijadikan
hipotesis kosong adalah "apakah benar bahwa terdapat sebesar
80% atau 0,8 mahasiswa yang berminat". Dengan demikian, H
dapat dirumuskan sebagai proporsi mahasiswa yang berminat
adalah 80.

Oleh karena itu, bentuk persamaan hipotesis dari kasus yang
kita miliki adalah sebagai berikut:

                 H: P = P = 0,8 atau H: P = 0,8

                 H1: P > P = 0,8 atau H1: P > 0,8

Pada hipotesis yang telah dirumuskan, H menunjukkan kondisi
bahwa proporsi mahasiswa yang berminat dengan program Bus
Kampus adalah 0,8. Kondisi ini mendukung asumsi bahwa
program Bus Kampus akan kurang efektif karena rendahnya
minat.

Sementara itu, H menunjukkan kondisi bahwa proporsi
mahasiswa yang berminat dengan program Bus Kampus adalah
lebih dari 0,8. Kondisi ini mendukung asumsi bahwa minat

                                                                               159
mahasiswa tinggi dan dapat mendukung efektivitas program
Bus Kampus.
6.3.2.3 Memilih distribusi sampling dan menentukan wilayah

             kritis
Berdasarkan informasi yang telah diberikan pada kasus, dapat
disimpulkan:

  1. Ukuran sampel adalah 333 responden, sehingga dapat
       dikategorikan sebagai sampel besar. Oleh karena itu,
       distribusi sampling yang digunakan adalah Distribusi Z.

  2. Hipotesis alternatif yang digunakan berbentuk lebih dari
       dari (right-tailed test), sehingga wilayah kritis berada di
       ekor sebelah kanan kurva distribusi.

  3. Dengan tingkat kepercayaan 99% ( = 1%), nilai Z yang
       menjadi batas wilayah kritis adalah +2,23. Adapun
       gambaran dari distribusi sampling dan wilayah kritis ini
       dapat dilihat pada Gambar 6-9. (Zkritis = +2,23)

     Gambar 6-9 Distribusi Sampling dan Wilayah Kritis Kasus Proporsi

160
6.3.2.4 Menghitung statistik uji
Berdasarkan kasus yang telah diuraikan, dapat rangkum:

    ·  (proporsi sampel) = 0,7
    · P (nilai dugaan, atau proporsi populasi H) = 0,8
    · n (ukuran sampel) = 333
maka perhitungan statistik uji Z-score dari kasus adalah sebagai
berikut:

                             =  - 0
                                  (1- )
                                     0,70 - 0,80

                               =
                                  0,70(133-3 0,70)

                               = -3,98
Dengan demikian, nilai statistik uji yang diperoleh adalah: -3,98
6.3.2.5 Menarik kesimpulan
Pada kasus, nilai statistik uji dan titik kritis adalah:

                                Zhitung = -3,98
                                Zkritis = +2,33
sehingga keputusannya adalah nilai statistik uji tidak jatuh ke
dalam wilayah kritis sehingga hipotesis kosong gagal ditolak
(Gambar 6-10).

                                                                               161
  Gambar 6-10 Penarikan Kesimpulan Statistik Hitung dan Wilayah Kritis

6.3.2.6 Memaknai Hasil Pengujian Hipotesis
Dengan merumuskan hipotesis kosong (H) sebagai P=80, hasil
pengujian menunjukkan bahwa kita tidak menemukan bukti
statistik kuat untuk untuk menyimpulkan bahwa
hipotesis ini gagal. Artinya, data sampel mendukung H,
yaitu bahwa proporsi minat mahasiswa terhadap layanan Bus
Kampus tidak mencapai atau melebihi 80.

Berdasarkan kesimpulan tersebut, maka dapat disimpulkan
secara populasi, minat mahasiswa rendah. Hal ini mendukung
pernyataan bahwa, penyediaan Bus Kampus tidak dapat
dianggap tepat dan berpotensi efektif. Meskipun dari sisi
statistik calon pengguna, yaitu mahasiswa berada pada lokasi
yang efektif, ternyata minat mahasiswa rendah untuk
menggunakan program Bus Kampus. Pihak kampus ITERA
perlu mengkaji ulang rencana program ini, atau dapat
melakukan modifikasi terhadap rencana yang ada. Faktor-faktor

162
yang mempengaurhi minat mahasiswa ini juga dapat dikaji lebih
lanjtu kedepannya jika respon pihak kampus terhadap distribusi
dan sebaran mahasiswa ini ingin diteruskan.
6.4 Soal Evaluasi
Untuk kasus-kasus berikut, tentukanlah (a) hipotesis kosong dan
hipotesis alternatifnya, (b) keputusan dalam memilih hipotesis
yang diterima, dan (c) makna dari hasil pemilihan hipotesis
tersebut. Gunakan galat sebesar 5% untuk semua soal. STP-6.1

    1. Berdasarkan survei kepada 173 orang dosen ITERA pada
         tahun 2023, rata-rata usianya pada saat itu adalah 29
         tahun dengan simpangan bakunya adalah 2,9 tahun. Jika
         ingin diketahui apakah rata-rata usia dosen ITERA pada
         tahun 2023 tersebut adalah sebenarnya sama saja
         dengan 30 tahun, ujilah pernyataan tersebut.

    2. Hasil survei kepada 427 orang mahasiswa menunjukkan
         bahwa 0,56-nya adalah pengguna sepeda motor pribadi.
         Bagaimana hasil pengujian hipotesis yang menyatakan
         bahwa sebenarnya pengguna sepeda motor pada
         mahasiswa itu lebih dari setengahnya.

                                                                               163
