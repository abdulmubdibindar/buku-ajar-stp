# Panduan Lengkap: Penomoran dan Referensi Rumus LaTeX di R Markdown/Bookdown

## Daftar Isi

1. [Pengenalan](#pengenalan)
2. [Environment Rumus Bernomor](#environment-rumus-bernomor)
3. [Memberikan Label pada Rumus](#memberikan-label-pada-rumus)
4. [Me-refer Rumus di Badan Dokumen](#me-refer-rumus-di-badan-dokumen)
5. [Contoh Lengkap Berbagai Kasus](#contoh-lengkap-berbagai-kasus)
6. [Tips dan Best Practices](#tips-dan-best-practices)
7. [Troubleshooting](#troubleshooting)
8. [Referensi Tambahan](#referensi-tambahan)

---

## Pengenalan

Dalam penulisan dokumen ilmiah, rumus matematis sering kali perlu diberi nomor untuk memudahkan referensi dalam teks. R Markdown/Bookdown mendukung penomoran otomatis rumus LaTeX dengan menggunakan sintaks khusus.

### Perbedaan Rumus Display vs Inline

- **Inline math**: Rumus dalam teks menggunakan `$...$` (tidak bernomor)
  - Contoh: `$E = mc^2$` menghasilkan $E = mc^2$
- **Display math tanpa nomor**: Rumus tersendiri menggunakan `$$...$$` (tidak bernomor)

  ```latex
  $$
  y = mx + c
  $$
  ```

- **Display math dengan nomor**: Menggunakan environment khusus seperti `equation`, `align`, dll.

---

## Environment Rumus Bernomor

### 1. Environment `equation`

Untuk **rumus tunggal yang bernomor**.

**Sintaks:**

```latex
\begin{equation}
rumus_matematika
(\#eq:label-unik)
\end{equation}
```

**Contoh:**

```latex
\begin{equation}
E = mc^2
(\#eq:einstein)
\end{equation}
```

**Kapan digunakan:**

- Rumus tunggal yang penting dan perlu dirujuk
- Definisi matematika dasar
- Persamaan utama dalam analisis

---

### 2. Environment `align`

Untuk **beberapa rumus yang sejajar** (biasanya pada tanda sama dengan).

**Sintaks:**

```latex
\begin{align}
rumus_1 (\#eq:label-1)\\
rumus_2 (\#eq:label-2)\\
rumus_3 (\#eq:label-3)
\end{align}
```

**Contoh:**

```latex
\begin{align}
\bar{x} &= \frac{\sum x_i}{n} (\#eq:mean)\\
s^2 &= \frac{\sum (x_i - \bar{x})^2}{n-1} (\#eq:variance)\\
s &= \sqrt{s^2} (\#eq:stdev)
\end{align}
```

**Catatan penting:**

- Gunakan `&` untuk menandai titik penjajaran (alignment point)
- Gunakan `\\` untuk pindah baris
- Setiap baris mendapat nomor tersendiri

**Kapan digunakan:**

- Serangkaian rumus yang berhubungan
- Derivasi matematis langkah demi langkah
- Definisi beberapa statistik deskriptif

---

### 3. Environment `align` dengan `\nonumber`

Untuk **menyembunyikan nomor pada baris tertentu**.

**Sintaks:**

```latex
\begin{align}
rumus_1 \nonumber\\
rumus_2 (\#eq:label-penting)\\
rumus_3 \nonumber
\end{align}
```

**Contoh:**

```latex
\begin{align}
\text{Diketahui: } y &= 2x + 3 \nonumber\\
\text{Maka: } 2y &= 4x + 6 (\#eq:hasil-kali-dua)\\
\text{Atau: } y &= 2x + 3 \nonumber
\end{align}
```

**Kapan digunakan:**

- Hanya beberapa baris yang perlu diberi nomor
- Langkah antara yang tidak perlu dirujuk
- Penjelasan atau keterangan dalam deretan rumus

---

### 4. Environment `split` di dalam `equation`

Untuk **rumus panjang yang dipecah beberapa baris** dengan **satu nomor saja**.

**Sintaks:**

```latex
\begin{equation}
\begin{split}
baris_1\\
baris_2\\
baris_3
\end{split}
(\#eq:label-unik)
\end{equation}
```

**Contoh:**

```latex
\begin{equation}
\begin{split}
\text{Total} &= variabel_1 + variabel_2 + variabel_3 \\
             &+ variabel_4 + variabel_5 + variabel_6 \\
             &+ variabel_7 + variabel_8
\end{split}
(\#eq:total-panjang)
\end{equation}
```

**Kapan digunakan:**

- Rumus yang terlalu panjang untuk satu baris
- Rumus yang merupakan satu kesatuan konsep
- Ekspansi aljabar yang panjang

---

### 5. Environment `gather`

Untuk **beberapa rumus terpusat tanpa penjajaran**.

**Sintaks:**

```latex
\begin{gather}
rumus_1 (\#eq:label-1)\\
rumus_2 (\#eq:label-2)
\end{gather}
```

**Contoh:**

```latex
\begin{gather}
a^2 + b^2 = c^2 (\#eq:pythagoras)\\
E = mc^2 (\#eq:einstein-2)\\
F = ma (\#eq:newton)
\end{gather}
```

**Kapan digunakan:**

- Kumpulan rumus yang tidak perlu disejajarkan
- Rumus-rumus dengan panjang berbeda
- Daftar persamaan penting

---

### 6. Environment `multline`

Untuk **satu rumus panjang** yang dipecah beberapa baris (baris pertama rata kiri, terakhir rata kanan, tengah di tengah).

**Sintaks:**

```latex
\begin{multline}
baris_pertama \\
baris_tengah \\
baris_terakhir
(\#eq:label-unik)
\end{multline}
```

**Contoh:**

```latex
\begin{multline}
\sum_{i=1}^{n} (x_i - \bar{x})^2 = \\
(x_1 - \bar{x})^2 + (x_2 - \bar{x})^2 + \cdots + (x_n - \bar{x})^2
(\#eq:ekspansi-jumlah-kuadrat)
\end{multline}
```

**Kapan digunakan:**

- Rumus sangat panjang yang merupakan satu kesatuan
- Ekspansi yang perlu ditampilkan secara penuh

---

### 7. Environment `aligned` di dalam `equation`

Alternatif dari `split`, memberikan kontrol lebih pada penjajaran.

**Sintaks:**

```latex
\begin{equation}
\begin{aligned}
baris_1\\
baris_2
\end{aligned}
(\#eq:label-unik)
\end{equation}
```

**Contoh:**

```latex
\begin{equation}
\begin{aligned}
y &= mx + c \\
  &= 2x + 3
\end{aligned}
(\#eq:substitusi)
\end{equation}
```

---

## Memberikan Label pada Rumus

### Format Label di Bookdown

**Aturan umum:**

```latex
(\#eq:nama-label)
```

**Komponen:**

- `(\#` - pembuka label khusus Bookdown
- `eq:` - prefix untuk equation (rumus)
- `nama-label` - identifier unik
- `)` - penutup label

### Konvensi Penamaan Label

#### 1. Gunakan Prefix `eq:`

**Benar:**

```latex
(\#eq:persamaan-linear)
(\#eq:mean)
(\#eq:variance)
```

**Salah:**

```latex
(\#persamaan-linear)  # Tidak ada prefix
(\#fig:mean)          # Prefix salah (fig untuk gambar)
```

#### 2. Gunakan Huruf Kecil

**Benar:**

```latex
(\#eq:teorema-pythagoras)
```

**Salah:**

```latex
(\#eq:Teorema-Pythagoras)  # Huruf kapital
(\#eq:MEAN)                 # Semua kapital
```

#### 3. Gunakan Tanda Hubung `-` sebagai Pemisah

**Benar:**

```latex
(\#eq:standar-deviasi-sampel)
(\#eq:rumus-kuartil-bawah)
```

**Salah:**

```latex
(\#eq:standar_deviasi_sampel)  # Underscore
(\#eq:rumusKuartilBawah)       # camelCase
(\#eq:rumus kuartil bawah)     # Spasi (akan error!)
```

#### 4. Buat Label Deskriptif

**Baik:**

```latex
(\#eq:mean-populasi)
(\#eq:variance-sampel)
(\#eq:teorema-limit-pusat)
```

**Kurang baik:**

```latex
(\#eq:rumus1)
(\#eq:eq2)
(\#eq:x)
```

#### 5. Gunakan Konteks Bab (Opsional)

Untuk proyek besar, tambahkan konteks bab:

```latex
(\#eq:bab2-mean)
(\#eq:bab3-regresi-linear)
(\#eq:statistik-inferensial-t-test)
```

### Penempatan Label

#### Dalam `equation`:

```latex
\begin{equation}
rumus
(\#eq:label)      # Label di baris terakhir sebelum \end{equation}
\end{equation}
```

#### Dalam `align`:

```latex
\begin{align}
rumus_1 (\#eq:label-1)\\     # Label di akhir baris
rumus_2 (\#eq:label-2)       # Tanpa \\ di baris terakhir
\end{align}
```

#### Dalam `split` atau `aligned`:

```latex
\begin{equation}
\begin{split}
baris_1\\
baris_2
\end{split}
(\#eq:label)      # Label setelah \end{split}
\end{equation}
```

---

## Me-refer Rumus di Badan Dokumen

### Sintaks Dasar

**Format:**

```markdown
\@ref(eq:nama-label)
```

**Contoh penggunaan:**

```markdown
Seperti yang ditunjukkan pada Persamaan \@ref(eq:mean), rata-rata dihitung dengan...
```

**Hasil render:**

> Seperti yang ditunjukkan pada Persamaan 3.1, rata-rata dihitung dengan...

### Variasi Penggunaan dalam Kalimat

#### 1. Di Awal Kalimat

```markdown
Persamaan \@ref(eq:variance) menunjukkan rumus untuk variansi sampel.
```

#### 2. Di Tengah Kalimat

```markdown
Berdasarkan Persamaan \@ref(eq:mean), kita dapat menghitung rata-rata data.
```

#### 3. Di Akhir Kalimat

```markdown
Standar deviasi adalah akar kuadrat dari variansi (Persamaan \@ref(eq:stdev)).
```

#### 4. Merujuk Beberapa Persamaan

```markdown
Persamaan \@ref(eq:mean), \@ref(eq:variance), dan \@ref(eq:stdev) adalah statistik deskriptif dasar.
```

Atau dengan rentang:

```markdown
Persamaan \@ref(eq:mean) hingga \@ref(eq:stdev) menunjukkan statistik deskriptif dasar.
```

### Gaya Penulisan Referensi

#### Formal (untuk jurnal/tesis):

```markdown
Seperti yang ditunjukkan pada Persamaan \@ref(eq:mean), ...
Berdasarkan Persamaan \@ref(eq:variance), dapat disimpulkan bahwa...
Substitusi nilai ke Persamaan \@ref(eq:stdev) menghasilkan...
```

#### Informal (untuk catatan/slide):

```markdown
Lihat Persamaan \@ref(eq:mean) untuk detailnya.
Gunakan rumus di Persamaan \@ref(eq:variance).
```

#### Dalam Kurung:

```markdown
Rata-rata dihitung dengan menjumlahkan semua nilai lalu dibagi jumlah observasi (Persamaan \@ref(eq:mean)).
```

### Link Otomatis

Referensi `\@ref(eq:...)` akan otomatis menjadi:

- **Link klikabel** yang menuju ke rumus yang dirujuk
- **Nomor yang tepat** sesuai urutan dalam dokumen
- **Update otomatis** jika urutan rumus berubah

---

## Contoh Lengkap Berbagai Kasus

### Contoh 1: Statistik Deskriptif

**Kode R Markdown:**

```markdown
## Ukuran Pemusatan Data

### Mean (Rata-rata)

Mean atau rata-rata merupakan ukuran tendensi sentral yang paling umum digunakan.
Mean dihitung dengan menjumlahkan seluruh nilai observasi kemudian membaginya dengan
jumlah observasi.

\begin{equation}
\bar{x} = \frac{\sum\_{i=1}^{n} x_i}{n} = \frac{x_1 + x_2 + \cdots + x_n}{n}
(\#eq:mean-sampel)
\end{equation}

Di mana:

- $\bar{x}$ = mean sampel
- $x_i$ = nilai observasi ke-$i$
- $n$ = jumlah observasi dalam sampel

Untuk populasi, mean dilambangkan dengan $\mu$ dan dihitung menggunakan rumus yang
sama seperti Persamaan \@ref(eq:mean-sampel), namun dengan $N$ (ukuran populasi)
sebagai pembagi.

\begin{equation}
\mu = \frac{\sum\_{i=1}^{N} x_i}{N}
(\#eq:mean-populasi)
\end{equation}

### Variansi

Variansi mengukur seberapa jauh nilai-nilai data tersebar dari mean. Berdasarkan
Persamaan \@ref(eq:mean-sampel), kita dapat menghitung deviasi setiap nilai dari
mean, kemudian menghitung rata-rata kuadrat deviasi tersebut.

\begin{equation}
s^2 = \frac{\sum\_{i=1}^{n} (x_i - \bar{x})^2}{n-1}
(\#eq:variance-sampel)
\end{equation}

Di mana $s^2$ adalah variansi sampel, dan $n-1$ adalah derajat kebebasan.

### Standar Deviasi

Standar deviasi adalah akar kuadrat dari variansi (Persamaan \@ref(eq:variance-sampel)):

\begin{equation}
s = \sqrt{s^2} = \sqrt{\frac{\sum\_{i=1}^{n} (x_i - \bar{x})^2}{n-1}}
(\#eq:stdev-sampel)
\end{equation}

Hubungan antara Persamaan \@ref(eq:variance-sampel) dan Persamaan \@ref(eq:stdev-sampel)
menunjukkan bahwa standar deviasi adalah ukuran penyebaran yang lebih intuitif karena
memiliki satuan yang sama dengan data asli.
```

### Contoh 2: Rumus Panjang dengan Split

**Kode R Markdown:**

```markdown
## Ekspansi Jumlah Kuadrat

Dalam analisis regresi, kita sering perlu menghitung jumlah kuadrat. Ekspansi lengkapnya
dapat dituliskan sebagai:

\begin{equation}
\begin{split}
\sum\_{i=1}^{n} (x_i - \bar{x})^2 &= (x_1 - \bar{x})^2 + (x_2 - \bar{x})^2 + (x_3 - \bar{x})^2 \\
&+ (x_4 - \bar{x})^2 + \cdots + (x_n - \bar{x})^2
\end{split}
(\#eq:ekspansi-jumlah-kuadrat)
\end{equation}

Persamaan \@ref(eq:ekspansi-jumlah-kuadrat) menunjukkan bahwa jumlah kuadrat deviasi
adalah penjumlahan dari kuadrat selisih setiap nilai dengan mean.
```

### Contoh 3: Derivasi Matematis dengan Align

**Kode R Markdown:**

```markdown
## Derivasi Rumus Variansi

Kita dapat menurunkan rumus alternatif untuk variansi:

\begin{align}
s^2 &= \frac{\sum*{i=1}^{n} (x_i - \bar{x})^2}{n-1} (\#eq:variance-awal)\\
&= \frac{\sum*{i=1}^{n} (x*i^2 - 2x_i\bar{x} + \bar{x}^2)}{n-1} \nonumber\\
&= \frac{\sum*{i=1}^{n} x*i^2 - 2\bar{x}\sum*{i=1}^{n}x*i + n\bar{x}^2}{n-1} \nonumber\\
&= \frac{\sum*{i=1}^{n} x*i^2 - 2n\bar{x}^2 + n\bar{x}^2}{n-1} \nonumber\\
&= \frac{\sum*{i=1}^{n} x_i^2 - n\bar{x}^2}{n-1} (\#eq:variance-alternatif)
\end{align}

Dari derivasi di atas, Persamaan \@ref(eq:variance-awal) dapat disederhanakan menjadi
Persamaan \@ref(eq:variance-alternatif), yang sering lebih efisien untuk komputasi.
```

### Contoh 4: Sistem Persamaan

**Kode R Markdown:**

```markdown
## Regresi Linear Sederhana

Dalam regresi linear sederhana, kita mencari persamaan garis:

\begin{equation}
Y = \beta_0 + \beta_1 X + \epsilon
(\#eq:regresi-populasi)
\end{equation}

Di mana $\beta_0$ dan $\beta_1$ adalah parameter yang tidak diketahui. Untuk mengestimasi
parameter tersebut dari sampel, kita menggunakan metode Ordinary Least Squares (OLS) yang
menghasilkan:

\begin{align}
b*1 &= \frac{\sum*{i=1}^{n}(x*i - \bar{x})(y_i - \bar{y})}{\sum*{i=1}^{n}(x_i - \bar{x})^2} (\#eq:slope)\\
b_0 &= \bar{y} - b_1\bar{x} (\#eq:intercept)
\end{align}

Persamaan \@ref(eq:slope) menghitung kemiringan (slope) garis regresi, sedangkan
Persamaan \@ref(eq:intercept) menghitung titik potong (intercept). Dengan menggunakan
Persamaan \@ref(eq:regresi-populasi) beserta estimasi dari Persamaan \@ref(eq:slope)
dan \@ref(eq:intercept), kita dapat memprediksi nilai $Y$ untuk nilai $X$ tertentu.
```

### Contoh 5: Probabilitas

**Kode R Markdown:**

```markdown
## Distribusi Normal

Fungsi kepadatan probabilitas (probability density function) dari distribusi normal adalah:

\begin{equation}
f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}
(\#eq:pdf-normal)
\end{equation}

Di mana:

- $\mu$ = mean populasi
- $\sigma$ = standar deviasi populasi
- $\pi$ = konstanta pi (3.14159...)
- $e$ = bilangan Euler (2.71828...)

Untuk standarisasi, kita transformasikan variabel $X$ menjadi $Z$:

\begin{equation}
Z = \frac{X - \mu}{\sigma}
(\#eq:z-score)
\end{equation}

Dengan menggunakan Persamaan \@ref(eq:z-score), kita dapat mengubah distribusi normal
dengan mean $\mu$ dan standar deviasi $\sigma$ menjadi distribusi normal standar dengan
mean 0 dan standar deviasi 1. Substitusi Persamaan \@ref(eq:z-score) ke dalam
Persamaan \@ref(eq:pdf-normal) menghasilkan fungsi kepadatan probabilitas normal standar.
```

### Contoh 6: Menggunakan Gather

**Kode R Markdown:**

```markdown
## Sifat-sifat Expected Value

Expected value memiliki beberapa sifat penting:

\begin{gather}
E(c) = c (\#eq:ev-konstanta)\\
E(cX) = cE(X) (\#eq:ev-skalar)\\
E(X + Y) = E(X) + E(Y) (\#eq:ev-penjumlahan)\\
E(XY) = E(X)E(Y) \text{ jika } X \text{ dan } Y \text{ independen} (\#eq:ev-perkalian)
\end{gather}

Di mana $c$ adalah konstanta, dan $X$ serta $Y$ adalah variabel acak. Persamaan
\@ref(eq:ev-konstanta) hingga \@ref(eq:ev-perkalian) adalah sifat-sifat fundamental
yang sering digunakan dalam derivasi statistik.
```

---

## Tips dan Best Practices

### 1. Konsistensi Penamaan

**Buat sistem penamaan yang konsisten:**

```latex
# Statistik deskriptif
(\#eq:mean-sampel)
(\#eq:mean-populasi)
(\#eq:median)
(\#eq:modus)

# Ukuran penyebaran
(\#eq:variance-sampel)
(\#eq:variance-populasi)
(\#eq:stdev-sampel)
(\#eq:stdev-populasi)

# Regresi
(\#eq:regresi-linear-sederhana)
(\#eq:regresi-slope)
(\#eq:regresi-intercept)
```

### 2. Dokumentasi Label

**Buat daftar label di awal dokumen atau di file terpisah:**

```markdown
<!-- Daftar Label Persamaan:
- eq:mean-sampel: Mean sampel (Bab 3)
- eq:variance-sampel: Variansi sampel (Bab 3)
- eq:stdev-sampel: Standar deviasi sampel (Bab 3)
- eq:regresi-linear: Model regresi linear (Bab 5)
-->
```

### 3. Penjelasan Simbologi

**Selalu jelaskan simbol setelah rumus:**

```markdown
\begin{equation}
\bar{x} = \frac{\sum\_{i=1}^{n} x_i}{n}
(\#eq:mean)
\end{equation}

Di mana:

- $\bar{x}$ = mean sampel
- $x_i$ = nilai observasi ke-$i$
- $n$ = jumlah observasi
```

### 4. Konteks Sebelum Rumus

**Berikan konteks sebelum menampilkan rumus:**

```markdown
Mean atau rata-rata merupakan ukuran tendensi sentral yang dihitung dengan:

\begin{equation}
\bar{x} = \frac{\sum\_{i=1}^{n} x_i}{n}
(\#eq:mean)
\end{equation}
```

### 5. Referensi yang Natural

**Integrasikan referensi secara natural dalam kalimat:**

**Baik:**

```markdown
Berdasarkan Persamaan \@ref(eq:mean), kita dapat menghitung rata-rata.
```

**Kurang baik:**

```markdown
Lihat eq:mean untuk mean.
```

### 6. Hindari Spasi dalam Label

**Benar:**

```latex
(\#eq:variansi-sampel)
(\#eq:standar-deviasi)
```

**Salah (akan error):**

```latex
(\#eq:variansi sampel)     # Spasi akan menyebabkan error!
(\#eq: standar-deviasi)     # Spasi setelah : juga error!
```

### 7. Gunakan Environment yang Tepat

| Situasi                                        | Environment yang Disarankan |
| ---------------------------------------------- | --------------------------- |
| Satu rumus penting                             | `equation`                  |
| Beberapa rumus sejajar                         | `align`                     |
| Rumus panjang (satu nomor)                     | `equation` + `split`        |
| Beberapa rumus tidak sejajar                   | `gather`                    |
| Derivasi dengan hanya beberapa langkah penting | `align` + `\nonumber`       |

### 8. Format Penulisan yang Rapi

**Beri indent untuk readability:**

```latex
\begin{equation}
  \begin{split}
    hasil &= variabel_1 + variabel_2 \\
          &+ variabel_3 + variabel_4
  \end{split}
  (\#eq:hasil)
\end{equation}
```

### 9. Komentar untuk Rumus Kompleks

**Tambahkan komentar untuk rumus yang rumit:**

```latex
<!-- Rumus berikut adalah derivasi dari teorema Bayes -->
\begin{equation}
P(A|B) = \frac{P(B|A)P(A)}{P(B)}
(\#eq:bayes)
\end{equation}
```

### 10. Cross-reference yang Informatif

**Tambahkan konteks saat me-refer:**

**Informatif:**

```markdown
Sesuai dengan definisi mean pada Persamaan \@ref(eq:mean), ...
```

**Kurang informatif:**

```markdown
Sesuai Persamaan \@ref(eq:mean), ...
```

---

## Troubleshooting

### Masalah 1: Nomor Persamaan Tidak Muncul

**Penyebab:**

- Menggunakan `$$...$$` alih-alih environment `equation`
- Lupa menutup environment dengan `\end{equation}`, `\end{align}`, dll.

**Solusi:**

```latex
<!-- SALAH: Tidak akan ada nomor -->
$$
y = mx + c
$$

<!-- BENAR: Akan ada nomor -->
\begin{equation}
y = mx + c
(\#eq:linear)
\end{equation}
```

### Masalah 2: Referensi Tidak Berfungsi (Muncul "??")

**Penyebab:**

- Label salah eja
- Lupa prefix `eq:`
- Dokumen perlu di-render ulang

**Solusi:**

1. Pastikan label sama persis:

   ```latex
   # Di rumus:
   (\#eq:mean-sampel)

   # Di teks:
   \@ref(eq:mean-sampel)  # Harus persis sama!
   ```

2. Re-render dokumen (kadang perlu 2x):
   ```r
   bookdown::render_book("index.Rmd")
   ```

### Masalah 3: Error "Duplicate label"

**Penyebab:**

- Dua rumus menggunakan label yang sama

**Solusi:**

- Cari dan ganti salah satu label dengan yang unik:
  ```bash
  # Di terminal/command line, cari label duplikat:
  grep -r "eq:mean" *.Rmd
  ```

### Masalah 4: Environment Tidak Ditutup

**Gejala:**

- Error saat rendering
- Rumus berantakan

**Penyebab:**

```latex
\begin{equation}
y = mx + c
(\#eq:linear)
# Lupa \end{equation}!
```

**Solusi:**

- Selalu pastikan setiap `\begin{...}` punya pasangan `\end{...}`

### Masalah 5: Alignment Tidak Berfungsi di `align`

**Penyebab:**

- Lupa tanda `&` untuk alignment point

**Solusi:**

```latex
<!-- SALAH: Tidak sejajar -->
\begin{align}
x = 1 (\#eq:x)\\
y = 2 (\#eq:y)
\end{align}

<!-- BENAR: Sejajar di tanda = -->
\begin{align}
x &= 1 (\#eq:x)\\
y &= 2 (\#eq:y)
\end{align}
```

### Masalah 6: Label Tidak Dikenali karena Spasi

**Gejala:**

- Error parsing
- Referensi tidak berfungsi

**Penyebab:**

```latex
(\#eq:mean sampel)    # SALAH: Ada spasi!
(\#eq: mean-sampel)   # SALAH: Spasi setelah :
```

**Solusi:**

```latex
(\#eq:mean-sampel)    # BENAR
```

### Masalah 7: Rumus Terpotong di PDF

**Penyebab:**

- Rumus terlalu panjang untuk satu baris

**Solusi:**

- Gunakan `split` atau `multline`:
  ```latex
  \begin{equation}
  \begin{split}
  hasil &= bagian_awal \\
        &+ bagian_akhir
  \end{split}
  (\#eq:hasil)
  \end{equation}
  ```

### Masalah 8: Simbol Khusus Tidak Muncul

**Penyebab:**

- Package LaTeX tidak ter-load

**Solusi:**

- Tambahkan di YAML header `index.Rmd`:
  ```yaml
  output:
    bookdown::gitbook:
      includes:
        in_header: preamble.tex
  ```
- Di `preamble.tex`:
  ```latex
  \usepackage{amsmath}
  \usepackage{amssymb}
  ```

### Masalah 9: Penomoran Restart di Setiap Bab

**Gejala:**

- Nomor persamaan kembali ke 1 di setiap bab baru

**Penyebab:**

- Ini sebenarnya behavior normal untuk bookdown (penomoran per bab: 1.1, 1.2, 2.1, 2.2, dst.)

**Solusi (jika ingin continuous):**

- Tambahkan di YAML:
  ```yaml
  output:
    bookdown::gitbook:
      number_sections: yes
  ```

### Masalah 10: Referensi Muncul Sebagai Link Rusak

**Penyebab:**

- Salah format sintaks

**Solusi:**

```markdown
<!-- SALAH -->

@ref(eq:mean) # Lupa backslash
\ref(eq:mean) # Bukan untuk bookdown
[eq:mean] # Bukan sintaks referensi

<!-- BENAR -->

\@ref(eq:mean) # Ini yang benar!
```

---

## Referensi Tambahan

### Resource Online

1. **Bookdown Official Documentation:**
   - https://bookdown.org/yihui/bookdown/markdown-extensions-by-bookdown.html#equations
   - Dokumentasi resmi tentang penomoran persamaan di Bookdown

2. **R Markdown Cookbook:**
   - https://bookdown.org/yihui/rmarkdown-cookbook/
   - Bab tentang mathematical expressions

3. **LaTeX Mathematics:**
   - https://en.wikibooks.org/wiki/LaTeX/Mathematics
   - Referensi lengkap tentang matematika di LaTeX

4. **AMS Math Package Documentation:**
   - http://mirrors.ctan.org/macros/latex/required/amsmath/amsldoc.pdf
   - Dokumentasi package amsmath (align, gather, dll.)

### Cheat Sheet Quick Reference

**Environment untuk rumus bernomor:**

```latex
equation    # Satu rumus, satu nomor
align       # Beberapa rumus sejajar, masing-masing bernomor
gather      # Beberapa rumus tengah, masing-masing bernomor
split       # Rumus panjang dalam equation, satu nomor
multline    # Rumus panjang, satu nomor, alignment khusus
```

**Format label:**

```latex
(\#eq:nama-label)    # Di dalam environment
```

**Format referensi:**

```markdown
\@ref(eq:nama-label) # Di body teks
```

**Menyembunyikan nomor:**

```latex
\nonumber    # Di akhir baris dalam align/gather
```

### Contoh Template Minimal

**File: `example.Rmd`**

```markdown
---
title: "Contoh Penomoran Rumus"
output: bookdown::gitbook
---

# Pendahuluan

Dokumen ini mendemonstrasikan penomoran rumus.

# Statistik Dasar

Mean dihitung dengan:

\begin{equation}
\bar{x} = \frac{\sum x_i}{n}
(\#eq:mean)
\end{equation}

Berdasarkan Persamaan \@ref(eq:mean), kita dapat menghitung rata-rata.
```

### Saran Workflow

1. **Tulis rumus dulu tanpa label** untuk memastikan syntax LaTeX benar
2. **Tambahkan label** setelah yakin rumus sudah benar
3. **Render dokumen** untuk melihat penomoran
4. **Tambahkan referensi** di teks
5. **Render ulang** untuk memastikan referensi berfungsi

---

## Penutup

Panduan ini mencakup semua aspek penting dalam penomoran dan referensi rumus LaTeX di R Markdown/Bookdown. Dengan mengikuti konvensi dan best practices yang dijelaskan, Anda dapat:

- ✅ Membuat rumus bernomor dengan berbagai environment
- ✅ Memberikan label yang konsisten dan deskriptif
- ✅ Me-refer rumus dengan link klikabel otomatis
- ✅ Menghindari error umum
- ✅ Menghasilkan dokumen yang profesional dan mudah dinavigasi

Selamat menulis dokumen ilmiah! 📊✨
