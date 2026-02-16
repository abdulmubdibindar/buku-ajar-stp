
import os

file_path = "c:\\Users\\LENOVO\\buku-ajar-stp\\05-pengantar-inferensial.Rmd"

new_content = """::: rmdkasus
### Studi Kasus: Simulasi dengan Populasi Kecil {.unnumbered}

Untuk mempermudah pemahaman, bayangkan kita memiliki **populasi  kecil** yang terdiri dari **16 orang** saja. Setiap orang memiliki atribut **Kelompok** (A/B/C/D) dan tinggal di **Blok** tertentu (1/2/3/4).

Berikut adalah data lengkap ke-16 orang tersebut:

```{r 05-inferensia-setup-toy-populasi, echo=FALSE, message=FALSE, warning=FALSE}
library(dplyr)
library(knitr)

# Buat Populasi Toy N=16
populasi_kecil <- data.frame(
  ID = 1:16,
  Jarak = c(2.5, 1.0, 5.2, 3.8,  # Blok 1
            0.5, 1.2, 4.0, 6.1,  # Blok 2
            10.5, 11.2, 9.8, 8.5, # Blok 3
            15.0, 14.2, 16.5, 13.8), # Blok 4
  Kelompok = rep(c("A", "B", "C", "D"), 4), # Distribute Strata evenly
  Blok = rep(c("Blok 1", "Blok 2", "Blok 3", "Blok 4"), each = 4) # Clusters
)

# Tampilkan dalam format compact (2 kolom berdampingan)
# Split menjadi 2 bagian (1-8 dan 9-16)
df_split_1 <- populasi_kecil[1:8, ]
df_split_2 <- populasi_kecil[9:16, ]

# Rename columns for display to avoid confusion
colnames(df_split_1) <- c("ID", "Jarak", "Kelompok", "Blok")
colnames(df_split_2) <- c("ID", "Jarak", "Kelompok", "Blok")

# Bind side by side properly (cbind)
# Note: kable doesn't support multiple headers easily, so we just cbind
tabel_gabungan <- cbind(df_split_1, df_split_2)

kable(tabel_gabungan, caption = "Daftar Lengkap Populasi (N=16)")
```

Mari kita terapkan keempat teknik sampling untuk memilih sampel dari 16 orang ini.

**1. Simple Random Sampling (SRS)**

Kita ingin mengambil sampel sebanyak **n=4** secara acak murni.

```{r 05-inferensia-toy-srs, echo=FALSE}
set.seed(101) # Seed for reproducibility
sampel_srs <- populasi_kecil |> sample_n(4)
kable(sampel_srs, caption = "Hasil SRS (n=4)")
```
*Hasilnya adalah 4 orang yang terpilih secara acak tanpa pola tertentu.*

**2. Systematic Random Sampling**

Kita ingin mengambil sampel dengan interval **k=4**.
Kita urutkan berdasarkan ID, lalu ambil setiap kelipatan 4 (4, 8, 12, 16).

```{r 05-inferensia-toy-systematic, echo=FALSE}
# Ambil setiap kelipatan 4
urutan_sys <- seq(4, 16, by = 4)
sampel_sys <- populasi_kecil |> slice(urutan_sys)
kable(sampel_sys, caption = "Hasil Systematic Sampling (Interval k=4)")
```
*Perhatikan pola ID yang terpilih selalu berjarak 4 angka.*

**3. Stratified Random Sampling**

Kita ingin memastikan setiap **Kelompok** (A, B, C, D) terwakili.
Kita bagi populasi menjadi 4 strata (Kelompok), lalu ambil **1 orang acak** dari setiap strata.

```{r 05-inferensia-toy-stratified, echo=FALSE}
set.seed(102)
sampel_strat <- populasi_kecil |> 
  group_by(Kelompok) |> 
  sample_n(1) |> 
  ungroup() |>
  arrange(Kelompok) # Urutkan supaya terlihat perwakilannya

kable(sampel_strat, caption = "Hasil Stratified Sampling (1 wakil per Kelompok)")
```
*Hasilnya menjamin ada masing-masing satu perwakilan dari Kelompok A, B, C, dan D.*

**4. Cluster Sampling**

Kita ingin menghemat tenaga dengan hanya mendatangi satu lokasi saja.
Kita pilih secara acak **1 Blok** (Cluster), lalu ambil **semua orang** di blok tersebut.

```{r 05-inferensia-toy-cluster, echo=FALSE}
set.seed(103)
# Pilih 1 blok secara acak
blok_terpilih <- sample(unique(populasi_kecil$Blok), 1)

sampel_cluster <- populasi_kecil |> 
  filter(Blok == blok_terpilih)

kable(sampel_cluster, caption = paste("Hasil Cluster Sampling (Terpilih:", blok_terpilih, ")"))
```
*Kita hanya perlu mendatangi satu lokasi (Blok), tapi mendapatkan 4 responden sekaligus.*
:::
"""

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Indices are 0-based. 
# Line 48 in file (1-based) is index 47.
# Line 157 in file (1-based) is index 156.
start_idx = 47
end_idx = 157 # Slice is exclusive at end, so 157 stops at 156.

# Check context
print(f"Replacing from line {start_idx+1}: {lines[start_idx].strip()}")
print(f"To line {end_idx}: {lines[end_idx-1].strip()}")

# Keep header
header = lines[:start_idx]
# Keep footer
footer = lines[end_idx:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(header)
    f.write(new_content + "\n\n")
    f.writelines(footer)

print("Replacement done.")
