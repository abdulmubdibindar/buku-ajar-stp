---
name: write-equation
description: Guide for writing formatted and numbered mathematical equations in R Markdown/Bookdown documents. Use this skill when you need to write, edit, or format mathematical equations or when referencing existing equations in the text.
---

# Write Equation Skill

When writing mathematical equations in this project, you MUST follow these guidelines which are specific to the R Markdown / Bookdown environment setup.

## 1. Environments for Numbered Equations

Always use the appropriate LaTeX environment for the type of equation:

- **Single Equation**: Use `equation`
  ```latex
  \begin{equation}
  y = mx + c
  (\#eq:linear-model)
  \end{equation}
  ```
- **Multiple Aligned Equations**: Use `align` (use `&` for alignment point, `\\` for newline). Each line gets a number.
  ```latex
  \begin{align}
  x &= 1 (\#eq:x-value)\\
  y &= 2 (\#eq:y-value)
  \end{align}
  ```
- **Long Equation (Wrapped)**: Use `split` or `aligned` inside `equation`. Gets only ONE number.
  ```latex
  \begin{equation}
  \begin{split}
  hasil &= bagian_awal \\
        &+ bagian_akhir
  \end{split}
  (\#eq:hasil-panjang)
  \end{equation}
  ```
- **Multiple Unaligned Equations**: Use `gather`. Each line gets a number.
- **Suppressing Equation Number**: Use `\nonumber` before `\\` if a specific line shouldn't be numbered.

## 2. Labeling Equations

- **Syntax**: `(\#eq:nama-label-unik)`
- **Placement**: Place the label at the end of the equation line, right before `\end{equation}` or before the newline `\\` in `align`/`gather`.
- **Naming Rules**:
  - MUST use the `eq:` prefix.
  - MUST be entirely lowercased.
  - MUST use dashes (`-`) to separate words. NEVER use spaces, underscores, or camelCase.
  - MUST be descriptive (e.g., `(\#eq:teorema-pythagoras)` rather than `(\#eq:rumus1)`).

## 3. Referencing Equations in Text

- **Syntax**: `\@ref(eq:nama-label-unik)`
- **Usage Context**:
  - Integrate naturally into sentences: "Berdasarkan Persamaan \@ref(eq:mean-sampel), kita dapat..."
  - Capitalize the word "Persamaan" when referring to it in text.

## 4. Best Practices

- Always write variables and symbols explanations right after the equation:
  ```markdown
  \begin{equation}
  \bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}
  (\#eq:mean-sampel)
  \end{equation}
  
  Di mana:
  
  - $\bar{x}$ = mean sampel
  - $x_i$ = nilai observasi ke-$i$
  - $n$ = jumlah observasi
  ```
- Never use `$$...$$` if the equation needs to be numbered or referenced. Use `$$...$$` ONLY for display math that won't ever be referenced.
