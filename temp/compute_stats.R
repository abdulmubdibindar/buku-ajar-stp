df1 <- read.csv("datasets/DataUtama_mhsITERA.csv", sep = ";")
df2 <- read.csv("datasets/DataUtama_mhsUNILA.csv", sep = ";")
df3 <- read.csv("datasets/DataUtama_mhsUBL.csv", sep = ";")
df4 <- read.csv("datasets/DataUtama_mhsUINRIL.csv", sep = ";")

cat(
  "\nITERA jarak: N=", sum(
    !is.na(df1$jarak.km)
  ),
  ", Mean=", mean(df1$jarak.km, na.rm = T),
  ", SD=", sd(df1$jarak.km, na.rm = T), "\n"
)
cat(
  "\nUNILA jarak: N=", sum(
    !is.na(df2$jarak.km)
  ),
  ", Mean=", mean(df2$jarak.km, na.rm = T),
  ", SD=", sd(df2$jarak.km, na.rm = T), "\n"
)
cat(
  "\nUBL jarak: N=", sum(
    !is.na(df3$jarak.km)
  ),
  ", Mean=", mean(df3$jarak.km, na.rm = T),
  ", SD=", sd(df3$jarak.km, na.rm = T), "\n"
)
cat(
  "\nUINRIL jarak: N=", sum(
    !is.na(df4$jarak.km)
  ),
  ", Mean=", mean(df4$jarak.km, na.rm = T),
  ", SD=", sd(df4$jarak.km, na.rm = T), "\n"
)
