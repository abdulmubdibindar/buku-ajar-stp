df1 <- read.csv('datasets/DataUtama_mhsITERA.csv', sep=';')
df2 <- read.csv('datasets/DataUtama_mhsUNILA.csv', sep=';')
df3 <- read.csv('datasets/DataUtama_mhsUBL.csv', sep=';')
df4 <- read.csv('datasets/DataUtama_mhsUINRIL.csv', sep=';')

sink('stats_output.txt')

cat('=== ITERA columns ===\n')
cat(paste(names(df1), collapse='\n'), '\n\n')

cat('=== UNILA columns ===\n')
cat(paste(names(df2), collapse='\n'), '\n\n')

cat('=== UBL columns ===\n')
cat(paste(names(df3), collapse='\n'), '\n\n')

cat('=== UINRIL columns ===\n')
cat(paste(names(df4), collapse='\n'), '\n\n')

cat('=== ITERA jarak.km stats ===\n')
cat('N=', sum(!is.na(df1$jarak.km)), '\n')
cat('Mean=', round(mean(df1$jarak.km, na.rm=TRUE), 3), '\n')
cat('SD=', round(sd(df1$jarak.km, na.rm=TRUE), 3), '\n\n')

cat('=== UNILA jarak.km stats ===\n')
cat('N=', sum(!is.na(df2$jarak.km)), '\n')
cat('Mean=', round(mean(df2$jarak.km, na.rm=TRUE), 3), '\n')
cat('SD=', round(sd(df2$jarak.km, na.rm=TRUE), 3), '\n\n')

cat('=== UBL jarak.km stats ===\n')
cat('N=', sum(!is.na(df3$jarak.km)), '\n')
cat('Mean=', round(mean(df3$jarak.km, na.rm=TRUE), 3), '\n')
cat('SD=', round(sd(df3$jarak.km, na.rm=TRUE), 3), '\n\n')

cat('=== UINRIL jarak.km stats ===\n')
cat('N=', sum(!is.na(df4$jarak.km)), '\n')
cat('Mean=', round(mean(df4$jarak.km, na.rm=TRUE), 3), '\n')
cat('SD=', round(sd(df4$jarak.km, na.rm=TRUE), 3), '\n\n')

# Also check waktu.tempuh if available
cat('=== ITERA waktu.tempuh check ===\n')
wt_cols <- grep('waktu|tempuh|menit', names(df1), value=TRUE, ignore.case=TRUE)
cat(paste(wt_cols, collapse='\n'), '\n\n')

cat('=== UNILA waktu.tempuh check ===\n')
wt_cols2 <- grep('waktu|tempuh|menit', names(df2), value=TRUE, ignore.case=TRUE)
cat(paste(wt_cols2, collapse='\n'), '\n\n')

sink()
cat('Done\n')
