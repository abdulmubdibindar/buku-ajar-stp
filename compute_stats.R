df1 <- read.csv('datasets/DataUtama_mhsITERA.csv', sep=';')
df2 <- read.csv('datasets/DataUtama_mhsUNILA.csv', sep=';')

cat('\nITERA jarak: N=', sum(
  !is.na(df1$jarak.km)), 
  ', Mean=', mean(df1$jarak.km, na.rm=T), 
  ', SD=', sd(df1$jarak.km, na.rm=T), '\n')
cat('\nUNILA jarak: N=', sum(
  !is.na(df2$jarak.km)), 
  ', Mean=', mean(df2$jarak.km, na.rm=T), 
  ', SD=', sd(df2$jarak.km, na.rm=T), '\n')
