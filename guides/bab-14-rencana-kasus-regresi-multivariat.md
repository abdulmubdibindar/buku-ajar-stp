# Rencana Kasus Regresi Linear Berganda (Bab 14)

## Konteks

Studi kasus Bab 14 merupakan **kelanjutan langsung** dari kasus yang sudah dibangun di Bab 13
(regresi linear sederhana), yaitu hubungan antara jarak ke taman kota dan Indeks Kualitas Udara
(IKU). Pengembangan ini dilakukan dengan menambahkan variabel-variabel independen baru agar
model menjadi lebih realistis dan dapat mengilustrasikan konsep regresi linear berganda,
termasuk penggunaan **variabel dummy** untuk variabel kategoris.

---

## Variabel

### Variabel Dependen

| Simbol | Nama | Satuan |
|--------|------|--------|
| $Y$ | Indeks Kualitas Udara (IKU) | poin (0–100) |

### Variabel Independen

| Simbol | Nama | Tipe | Satuan | Arah Pengaruh thd IKU |
|--------|------|------|--------|----------------------|
| $X_1$ | Jarak ke taman kota terdekat | Kontinu | km | Negatif — semakin jauh, IKU makin rendah |
| $X_2$ | Jarak ke kawasan industri terdekat | Kontinu | km | Positif — semakin jauh, IKU makin tinggi |
| $X_3$ | Proporsi tutupan vegetasi dalam radius 500 m | Kontinu | % | Positif — vegetasi menyerap polutan |
| $X_4$ | Zona fungsi lahan | Kategoris (3 level) | — | Tergantung dummy (lihat bawah) |

> **Catatan $X_3$**: Diasumsikan diukur dalam radius 500 m dari setiap titik pengambilan data IKU,
> menggunakan data citra satelit atau peta tutupan lahan.

---

## Variabel Dummy untuk $X_4$ (Zona Fungsi Lahan)

Tiga kategori zona fungsi lahan:

- **Perumahan** → **kategori referensi** ($d_1 = 0$, $d_2 = 0$)
- **Komersial** → $d_1 = 1$, $d_2 = 0$
- **Industri** → $d_1 = 0$, $d_2 = 1$

Dengan proporsi sampel: Perumahan 50%, Komersial 30%, Industri 20%.

### Interpretasi Koefisien Dummy

| Zona | Interpretasi |
|------|-------------|
| Komersial ($\beta_4$) | Selisih rata-rata IKU antara zona komersial dan perumahan, ceteris paribus — diharapkan negatif kecil |
| Industri ($\beta_5$) | Selisih rata-rata IKU antara zona industri dan perumahan, ceteris paribus — diharapkan negatif lebih besar |

---

## Persamaan Model Penuh

$$\hat{Y} = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \beta_3 X_3 + \beta_4 d_1 + \beta_5 d_2$$

---

## Generator Dataset R

```r
set.seed(42)
n <- 30

# Variabel kontinu
jarak_taman    <- round(runif(n, 0.5, 10), 1)  # km
jarak_industri <- round(runif(n, 0.5, 8), 1)   # km
vegetasi       <- round(runif(n, 5, 60), 1)     # %

# Variabel kategoris
zona <- sample(
  c("Perumahan", "Komersial", "Industri"),
  n, replace = TRUE,
  prob = c(0.5, 0.3, 0.2)
)

# Variabel dummy
d_komersial <- as.integer(zona == "Komersial")
d_industri  <- as.integer(zona == "Industri")

# Generate IKU (true coefficients)
iku <- round(
  75
  - 4.5 * jarak_taman
  + 3.0 * jarak_industri
  + 0.4 * vegetasi
  - 5   * d_komersial
  - 12  * d_industri
  + rnorm(n, 0, 4),
  0
)
iku[iku < 0] <- 0
iku[iku > 100] <- 100

df_berganda <- data.frame(
  No             = 1:n,
  jarak_taman    = jarak_taman,
  jarak_industri = jarak_industri,
  vegetasi       = vegetasi,
  zona           = zona,
  iku            = iku
)
```

### Parameter Pembangkit (True Coefficients)

| Parameter | Nilai |
|-----------|-------|
| $\beta_0$ (intersep) | 75 |
| $\beta_1$ (jarak taman) | −4,5 |
| $\beta_2$ (jarak industri) | +3,0 |
| $\beta_3$ (vegetasi) | +0,4 |
| $\beta_4$ (dummy Komersial) | −5 |
| $\beta_5$ (dummy Industri) | −12 |
| $\sigma$ (galat) | 4 |

---

## Narasi Konteks Kasus

> Studi lanjutan dari survei di Bab 13 kini mengukur **30 lokasi yang sama** di sebuah kota.
> Selain jarak ke taman kota, survei juga mencatat jarak ke kawasan industri terdekat, proporsi
> tutupan vegetasi dalam radius 500 m dari titik pengukuran, serta zona fungsi lahan di mana
> lokasi tersebut berada (perumahan, komersial, atau industri).

---

## Catatan Multikolinearitas

Perlu diperiksa korelasi antara:

- $X_1$ (jarak taman) dan $X_3$ (vegetasi): potensi korelasi negatif sedang karena taman
  berkontribusi pada tutupan vegetasi — **pantau, tapi biasanya masih aman**.
- $X_1$ dan $X_2$: diharapkan lemah karena keduanya mengukur jarak dari objek berbeda.
- $X_4$ (zona) dan $X_2$ (jarak industri): zona industri cenderung dekat kawasan industri —
  **perlu diverifikasi setelah data dibangkitkan**.
