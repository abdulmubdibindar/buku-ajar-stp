---
title: "Cross-Reference Div Syntax"
source: "https://quarto.org/docs/authoring/cross-references-divs.html"
author:
published:
created: 2026-06-09
description:
tags:
  - "clippings"
---
## Overview

Cross-referenceable [figures](https://quarto.org/docs/authoring/cross-references-divs.html#figures), [tables](https://quarto.org/docs/authoring/cross-references-divs.html#tables) and [code listings](https://quarto.org/docs/authoring/cross-references-divs.html#listings) are known as *float* cross-references. Floats can appear in the rendered document at locations other than where they are defined, i.e. they float, and usually have captions.

Along with compact syntax for the most common uses of cross-references, Quarto also provides a more general div syntax for declaring floats that can be cross-referenced. To declare a cross-referenceable float, place the content inside a fenced div with the reference identifier as an attribute. The last paragraph inside the fenced div will be treated as the caption.

Warning

Quarto currently only supports this alternative syntax for **floats**, as described above. Some cross-referenceable elements like theorems, proofs, etc naturally use this div syntax, but note that Quarto does not support the use of the div syntax for block-level equations.

As a minimal example, consider the following QMD snippet:

```markdown
::: {#fig-example}

CONTENT

Caption

:::
```

This produces the following (admittedly silly) figure:

CONTENT

Figure 1: Caption

Now, this figure can be cross-referenced with `@fig-example`, see [Figure 1](https://quarto.org/docs/authoring/cross-references-divs.html#fig-example).

To be recognized as a cross-reference the identifier must begin with one of the built-in float reference types (Figures (`fig-`), Tables (`tbl-`) and Listings (`lst-`)), or be defined as a [custom float cross-reference](https://quarto.org/docs/authoring/cross-references-custom.html) type.

You can then refer to the element as usual with the `@` syntax, e.g.

```markdown
@fig-example shows...
```

The content can be any Quarto markdown. For example, [Figure 2](https://quarto.org/docs/authoring/cross-references-divs.html#fig-table) is a markdown table treated like a figure:

```markdown
::: {#fig-table}

| A | B |
|---|---|
| C | D |

A table treated like a figure 

:::
```

| C | D |
| --- | --- |

Figure 2: A table treated like a figure

[Table 1](https://quarto.org/docs/authoring/cross-references-divs.html#tbl-table) is an image treated like a table:

```markdown
::: {#tbl-table}

![](table.png)

An image treated like a table

:::
```

![](https://quarto.org/docs/authoring/images/crossref-div-table.png)

Table 1: An image treated like a table

[Figure 3](https://quarto.org/docs/authoring/cross-references-divs.html#fig-code) is a code cell treated like a figure:

```markdown
::: {#fig-code}

\`\`\`r
library(tidyverse)
starwars |> 
  ggplot(aes(height, mass)) + 
  geom_point()
\`\`\`

A code cell treated like a figure.

:::
```

```
library(tidyverse)
starwars |> 
  ggplot(aes(height, mass)) + 
  geom_point()
```

Figure 3: A code cell treated like a figure.

On this page, we illustrate common use cases for [Figures](https://quarto.org/docs/authoring/cross-references-divs.html#figures), [Tables](https://quarto.org/docs/authoring/cross-references-divs.html#tables) and [Code Listings](https://quarto.org/docs/authoring/cross-references-divs.html#listings) then some applications of the div syntax to:

## Figures

To create a cross-reference to a figure using div syntax, create a fenced div with an id starting with `fig-`, include the image followed by the caption inside the div:

```markdown
::: {#fig-elephant}

![](elephant.png)

An Elephant
:::
```

You can cross-reference a figure created by an executable code cell by including the code cell as the content:

```markdown
::: {#fig-line-plot}

\`\`\`{python}
import matplotlib.pyplot as plt
plt.plot([1,23,2,4])
plt.show()
\`\`\`

A line plot
:::
```

In the above example, you can reference the figure with `@fig-line-plot`, but not the code, which appears inline. If you would also like to be able to refer to the code, you can do so using code chunk options rather than the div syntax, see [Cross-References for Executable Code Blocks](https://quarto.org/docs/authoring/cross-references.html#code-listings) for details.

## Tables

To create a cross-reference to a table using div syntax, create a fenced div with an id starting with `tbl-`, include the table followed by the caption inside the div:

```markdown
::: {#tbl-letters}

| Col1 | Col2 | Col3 |
|------|------|------|
| A    | B    | C    |
| E    | F    | G    |
| A    | G    | G    |

My Caption

:::
```

If the table is produced by an executable code cell, put the cell inside the div as content, e.g:

```markdown
::: {#tbl-planets}

\`\`\`{python}
from IPython.display import Markdown
from tabulate import tabulate
table = [["Sun","696,000",1.989e30],
         ["Earth","6,371",5.972e24],
         ["Moon","1,737",7.34e22],
         ["Mars","3,390",6.39e23]]
Markdown(tabulate(
  table, 
  headers=["Astronomical object","R (km)", "mass (kg)"]
))
\`\`\`

Astronomical object

:::
```

In the above example, you can reference the table with `@tbl-planets`, but not the code, which appears inline. If you would also like to be able to refer to the code, you can do so using code chunk options rather than the div syntax, see [Cross-References for Executable Code Blocks](https://quarto.org/docs/authoring/cross-references.html#code-listings) for details.

## Listings

To create a cross-reference to a code listing using div syntax, create a fenced div with an id starting with `lst-`, include the code cell followed by the caption inside the div:

```markdown
::: {#lst-customers}

\`\`\`{.sql}
SELECT * FROM Customers
\`\`\`

Customers Query

:::
```

This also works for executable code cells that produce no output:

```markdown
::: {#lst-assign}

\`\`\`{r}
x <- 1
\`\`\`

Assignment in R

:::
```

However, if any output is produced, it is assumed the output should be the content of the cross-reference, and the code is lifted out and placed inline. For example, the code cell here produces output:

```markdown
::: {#lst-assign-output}

\`\`\`{r}
x <- 1
x
\`\`\`

Assignment in R

:::

@lst-assign-output
```

When rendered the above results in output being the contents of the listing, with the code appearing before the listing:

![Screenshot of a listing cross-reference. A code cell comes first, followed by Listing 1 which contains code output.](https://quarto.org/docs/authoring/images/crossrefs-listing-output.png)

If you need to reference both the code its output, use a combination of a display block and a code block with the code cell option `echo: false`:

```markdown
::: {#lst-assign-both}

\`\`\`r
x <- 1
x
\`\`\`

\`\`\`{r}
#| echo: false
x <- 1
x
\`\`\`

Assignment in R

:::
```

When the output is a figure or table, you can reference the code and the output individually by using code cell options, rather than the div syntax, as described in [Cross-References for Executable Code Blocks](https://quarto.org/docs/authoring/cross-references.html#code-listings).

## Diagrams

To create a cross-references to a diagram using div syntax, treat it like a figure. For example, [Figure 4](https://quarto.org/docs/authoring/cross-references-divs.html#fig-simple) is created using:

```markdown
::: {#fig-simple}

\`\`\`{dot}
graph {
  A -- B
}
\`\`\`

This is a simple graphviz graph
:::
```

<svg width="144" height="480" viewBox="0.00 0.00 62.00 116.00" xmlns="http://www.w3.org/2000/svg" xlink="http://www.w3.org/1999/xlink" style="; max-width: none; max-height: none"><g id="graph0" transform="scale(1 1) rotate(0) translate(4 112)"><polygon fill="white" stroke="transparent" points="-4,4 -4,-112 58,-112 58,4 -4,4"></polygon><g id="node1"><title>A</title> <ellipse fill="none" stroke="black" cx="27" cy="-90" rx="27" ry="18"></ellipse><text text-anchor="middle" x="27" y="-85.8" font-family="Times,serif" font-size="14.00">A</text> </g><g id="node2"><title>B</title> <ellipse fill="none" stroke="black" cx="27" cy="-18" rx="27" ry="18"></ellipse><text text-anchor="middle" x="27" y="-13.8" font-family="Times,serif" font-size="14.00">B</text> </g><g id="edge1"><title>A--B</title><path fill="none" stroke="black" d="M27,-71.7C27,-60.85 27,-46.92 27,-36.1"></path></g></g></svg>

Figure 4: This is a simple graphviz graph

If you would rather give diagrams a label and counter distinct from figures, consider defining [Custom Cross-Reference Types](https://quarto.org/docs/authoring/cross-references-custom.html).

## Videos

To add a cross-reference to a video, use the [cross-reference div syntax](https://quarto.org/docs/authoring/cross-references-divs.html) and treat it like a figure. For example,

```markdown
::: {#fig-cern}

{{< video https://www.youtube.com/embed/wo9vZccmqwc >}}

The video "CERN: The Journey of Discovery"

:::

In @fig-cern...
```

Which renders as:

![Screenshot that shows a YouTube video followed by the caption, 'Figure 1: The video CERN: The Journey of Discovery'. Below the caption is the text 'In Figure 1 ...'.](https://quarto.org/docs/authoring/images/crossrefs-video.png)

If you would rather give videos a label and counter distinct from figures, consider defining [Custom Cross-Reference Types](https://quarto.org/docs/authoring/cross-references-custom.html).

## Subreferences

Note

When your sub-content is either all figures or all tables there is abbreviated syntax, see the Cross References page for [Subfigures](https://quarto.org/docs/authoring/cross-references.html#subfigures) and [Subtables](https://quarto.org/docs/authoring/cross-references.html#subtables) for details.

Cross-reference divs can be nested to create elements with subreferences. For example, the outer div here defines the `fig-subrefs` reference along with the main caption, while the inner divs define `fig-first` and `fig-second` along with their respective captions:

```markdown
:::: {#fig-subrefs}

::: {#fig-first}

CONTENT 1

First caption
:::

::: {#fig-second}

CONTENT 2

Second caption
:::

Main caption
::::
```

This renders as:

CONTENT 1

(a) First caption

CONTENT 2

(b) Second caption

Figure 5: Main caption

Both the main element and the sub elements can be referenced directly in the text, e.g.

```markdown
@fig-subrefs, @fig-first, @fig-second
```

This renders as: [Figure 5](https://quarto.org/docs/authoring/cross-references-divs.html#fig-subrefs), [Figure 5 (a)](https://quarto.org/docs/authoring/cross-references-divs.html#fig-first), [Figure 5 (b)](https://quarto.org/docs/authoring/cross-references-divs.html#fig-second).

Combined with layout attributes, you can create complex layouts of mixed content where each element can be referenced. For example:

```markdown
:::: {#fig-complex layout="[[1, 1], [1]]"}

::: {#fig-elephant}

![](images/elephant.jpg)

An image file
:::

::: {#fig-scatterplot}

\`\`\`{r}
#| echo: false
plot(1:10)
\`\`\`

A computational figure
:::

::: {#fig-diagram}

\`\`\`{dot}
//| fig-height: 2
digraph {
  rankdir = "LR";
  Transform -> Visualize
}
\`\`\`

A diagram
:::

Example figure combining different types of content
::::
```

This renders as:

![A screenshot of a figure layout with two rows. The top row has two columns: on the left an image of an elephant silhouetted against a sunset with the caption (a) An image file; on the right a scatterplot with the caption (b) A computational figure. In the bottom row is a flow chart with a node Transform linked to the node Visualize with the caption (c) A diagram. Below the layout is the caption: Figure 1: Example figure combining different types of content.](https://quarto.org/docs/authoring/images/crossrefs-complex-layout.png)

## Computed Captions

If you want to include computed values in a caption, use the cross-reference div syntax, along with an [inline code expression](https://quarto.org/docs/computations/execution-options.html#inline-code). For example:

```markdown
::: {#fig-box}

\`\`\`{python}
#| echo: false
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 10]
p = plt.boxplot(x)
plt.show()
\`\`\`

This dataset has \`{python} len(x)\` observations.

:::
```

```markdown
::: {#fig-box}

\`\`\`{r}
#| echo: false

x <- c(1, 2, 3, 4, 5, 10)
boxplot(x)

\`\`\`

This dataset has \`{r} length(x)\` observations.

:::
```

## Conditional Content

The cross-reference div syntax combined with [conditional content](https://quarto.org/docs/authoring/conditional.html) allows the content of your reference to vary by format. For example, you might want an interactive JavaScript based plot when the format is HTML, but otherwise produce a static plot:

```markdown
::: {#fig-scatterplot}  
  
:::: {.content-visible when-format="html"}

\`\`\`{r}
# Code to produce JavaScript based plot
\`\`\`
::::

:::: {.content-visible unless-format="html"}

\`\`\`{r}
# Code to produce static plot
\`\`\`
::::

Scatterplot

:::

@fig-scatterplot
```