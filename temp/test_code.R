library(ggplot2)
library(patchwork)

alpha <- 0.10
z_kritis_dua <- qnorm(1 - alpha / 2)
z_kritis_satu <- qnorm(1 - alpha)     

warna_tolak   <- '#e74c3c'
warna_terima  <- '#2ecc71'
warna_kurva   <- '#2c3e50'

x_seq <- seq(-4, 4, length.out = 500)
df    <- data.frame(x = x_seq, y = dnorm(x_seq))

# --- Plot 1: Uji Dua Ekor ---
p1 <- ggplot(df, aes(x, y)) +
  geom_area(data = subset(df, x <= -z_kritis_dua),
            aes(y = y), fill = warna_tolak, alpha = 0.85) +
  geom_area(data = subset(df, x >= z_kritis_dua),
            aes(y = y), fill = warna_tolak, alpha = 0.85) +
  geom_area(data = subset(df, x >= -z_kritis_dua & x <= z_kritis_dua),
            aes(y = y), fill = warna_terima, alpha = 0.35) +
  geom_line(color = warna_kurva, linewidth = 0.9) +
  geom_vline(xintercept = c(-z_kritis_dua, z_kritis_dua),
             linetype = 'dashed', color = warna_tolak, linewidth = 0.7) +
  annotate('text', x = -2.8, y = 0.07,
           label = 'Tolak', parse = FALSE,
           size = 3.2, color = 'white', fontface = 'bold') +
  annotate('text', x = -2.8, y = 0.03,
           label = 'H0', parse = FALSE,
           size = 3.2, color = 'white', fontface = 'bold') +
  annotate('text', x =  2.8, y = 0.07,
           label = 'Tolak', parse = FALSE,
           size = 3.2, color = 'white', fontface = 'bold') +
  annotate('text', x =  2.8, y = 0.03,
           label = 'H0', parse = FALSE,
           size = 3.2, color = 'white', fontface = 'bold') +
  annotate('text', x = 0, y = 0.16,
           label = 'Gagal Tolak H0', parse = FALSE,
           size = 3.2, color = '#1a6b3a', fontface = 'bold') +
  annotate('text', x = -3.5, y = 0.38,
           label = paste0('alpha/2 == ', alpha/2), parse = TRUE,
           size = 3, color = warna_tolak) +
  annotate('text', x =  3.5, y = 0.38,
           label = paste0('alpha/2 == ', alpha/2), parse = TRUE,
           size = 3, color = warna_tolak) +
  scale_x_continuous(breaks = NULL) +
  scale_y_continuous(expand = expansion(mult = c(0.08, 0.05))) +
  labs(title = 'Uji Dua Ekor (Two-Tailed)',
       subtitle = 'H1: μ1 ≠ μ2',
       x = NULL, y = NULL) +
  theme_minimal(base_size = 11) +
  theme(
    plot.title    = element_text(face = 'bold', hjust = 0.5, size = 11),
    plot.subtitle = element_text(hjust = 0.5, size = 10, color = '#555555'),
    axis.text.y   = element_blank(),
    panel.grid    = element_blank(),
    axis.line.x   = element_line(color = warna_kurva, linewidth = 0.5)
  )

# --- Plot 2: Uji Satu Ekor Kanan ---
p2 <- ggplot(df, aes(x, y)) +
  geom_area(data = subset(df, x >= z_kritis_satu),
            aes(y = y), fill = warna_tolak, alpha = 0.85) +
  geom_area(data = subset(df, x < z_kritis_satu),
            aes(y = y), fill = warna_terima, alpha = 0.35) +
  geom_line(color = warna_kurva, linewidth = 0.9) +
  geom_vline(xintercept = z_kritis_satu,
             linetype = 'dashed', color = warna_tolak, linewidth = 0.7) +
  annotate('text', x = 3, y = 0.07,
           label = 'Tolak', parse = FALSE,
           size = 3.2, color = 'white', fontface = 'bold') +
  annotate('text', x = 3, y = 0.03,
           label = 'H0', parse = FALSE,
           size = 3.2, color = 'white', fontface = 'bold') +
  annotate('text', x = -0.5, y = 0.16,
           label = 'Gagal Tolak H0', parse = FALSE,
           size = 3.2, color = '#1a6b3a', fontface = 'bold') +
  annotate('text', x = 3.3, y = 0.38,
           label = paste0('alpha == ', alpha), parse = TRUE,
           size = 3, color = warna_tolak) +
  scale_x_continuous(breaks = NULL) +
  scale_y_continuous(expand = expansion(mult = c(0.08, 0.05))) +
  labs(title = 'Uji Satu Ekor Kanan (Right One-Tailed)',
       subtitle = 'H1: μ1 > μ2',
       x = NULL, y = NULL) +
  theme_minimal(base_size = 11) +
  theme(
    plot.title    = element_text(face = 'bold', hjust = 0.5, size = 11),
    plot.subtitle = element_text(hjust = 0.5, size = 10, color = '#555555'),
    axis.text.y   = element_blank(),
    panel.grid    = element_blank(),
    axis.line.x   = element_line(color = warna_kurva, linewidth = 0.5)
  )

print(p1 + p2)
