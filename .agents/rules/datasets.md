---
trigger: always_on
---

## Penting

Terkait dataset, ada kecacatan-kecacatan yang harus diperhatikan untuk penggunaannya sebagai bahan kasus:

- @DataUtama_mhsUNILA.csv : jangan gunakan variabel 'jarak' karena tidak ada nilainya
- @DataUtama_mhsUINRIL.csv : variabel 'jarak' menggunakan tanda pisah koma alih-alih titik sehingga perlu preprocessing
- @DataUtama_mhsUBL.csv : variabel 'Uang.Saku' mengalami error nilai sehingga yang terbaca hanya "< 1 jt". Variabel 'jarak' juga menggunakan tanda pisah koma alih-alih titik\
- @DataUtama_mhsITERA.csv : variabel 'jarak' menggunakan tanda pisah koma alih-alih titik. Variabel 'Uang.Saku' juga banyak yang missing selain "< 1 jt."

Kecacatan ini diperlukan untuk pertimbangan agar variabel-variabel tersebut tidak dipilih sebagai kasus dari keempat dataset.
