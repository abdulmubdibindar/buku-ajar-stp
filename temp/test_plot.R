library(ggplot2)

z <- seq(-3.5, 3.5, length.out = 1000)
density <- dnorm(z)
df <- data.frame(z = z, density = density)
z_cutoff <- 1.25
df_b_right <- subset(df, z >= 0 & z <= z_cutoff)
df_c_right <- subset(df, z > z_cutoff)
df_b_left <- subset(df, z >= -z_cutoff & z < 0)
df_c_left <- subset(df, z < -z_cutoff)

p <- ggplot(df, aes(x = z, y = density)) +
  geom_line(size = 1) +
  geom_area(data = df_b_right, fill = "#56B4E9", alpha = 0.6) +
  geom_area(data = df_c_right, fill = "#E69F00", alpha = 0.6) +
  geom_area(data = df_b_left, fill = "#56B4E9", alpha = 0.6) +
  geom_area(data = df_c_left, fill = "#E69F00", alpha = 0.6) +
  geom_vline(xintercept = 0, linetype = "dashed", size = 0.8) +
  geom_vline(xintercept = z_cutoff, linetype = "dashed", size = 0.6, color="black") +
  geom_vline(xintercept = -z_cutoff, linetype = "dashed", size = 0.6, color="black") +
  annotate("text", x = z_cutoff/2, y = 0.15, label = "Area b", size = 5, fontface = "bold") +
  annotate("text", x = z_cutoff + 0.6, y = 0.05, label = "Area c", size = 5, fontface = "bold") +
  annotate("text", x = -z_cutoff/2, y = 0.15, label = "Area b", size = 5, fontface = "bold") +
  annotate("text", x = -z_cutoff - 0.6, y = 0.05, label = "Area c", size = 5, fontface = "bold") +
  scale_x_continuous(breaks = c(-z_cutoff, 0, z_cutoff), labels = c("-Z", "0", "+Z")) +
  theme_classic() +
  labs(x = "Z-score", y = "") +
  theme(axis.text.y = element_blank(), 
        axis.ticks.y = element_blank(),
        axis.line.y = element_blank(),
        axis.text.x = element_text(size = 12, face="bold"))

ggsave("test_plot.png", plot = p, width = 6, height = 4)
