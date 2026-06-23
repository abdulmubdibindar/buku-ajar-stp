---
title: "Citations"
source: "https://quarto.org/docs/authoring/citations.html"
author:
published:
created: 2026-06-09
description:
tags:
  - "clippings"
---
## Overview

Quarto will use Pandoc to automatically generate citations and a bibliography in a number of styles. To use this capability, you will need:

- A quarto document formatted with citations (see [Citation Markdown](https://quarto.org/docs/authoring/citations.html#sec-citations)).
- A bibliographic data source, for example a BibLaTeX (`.bib`) or BibTeX (`.bibtex`) file.
- Optionally, a `CSL` file which specifies the formatting to use when generating the citations and bibliography (when not using `natbib` or `biblatex` to generate the bibliography).

Note

When using `format: typst`, by default citation processing is handled by Typst, not Pandoc. See the [Typst](https://quarto.org/docs/authoring/citations.html#typst) section below for more details.

## Bibliography Files

Quarto supports bibliography files in a wide variety of formats including BibLaTeX and CSL. Add a bibliography to your document using the `bibliography` YAML metadata field. For example:

```yaml
---
title: "My Document"
bibliography: references.bib
---
```

Tip

You can provide more than one bibliography file if you would like by setting the `bibliography` field’s value to a YAML array.

See the [Pandoc Citations](https://pandoc.org/MANUAL.html#citations) documentation for additional information on bibliography formats.

## Citation Syntax

Quarto uses the standard Pandoc markdown representation for citations (e.g. `[@citation]`) — citations go inside square brackets and are separated by semicolons. Each citation must have a key, composed of ‘@’ + the citation identifier from the database, and may optionally have a prefix, a locator, and a suffix. The citation key must begin with a letter, digit, or `_`, and may contain alphanumerics, `_`, and internal punctuation characters (`:.#$%&-+?<>~/`). Here are some examples:

| ``` Blah Blah [see @knuth1984, pp. 33-35; also @wickham2015, chap. 1] ``` | Blah Blah (see [Knuth 1984, 33–35](https://quarto.org/docs/authoring/citations.html#ref-knuth1984); also [Wickham 2015, chap. 1](https://quarto.org/docs/authoring/citations.html#ref-wickham2015)) | Blah Blah see \[1\], pp. 33-35; also \[1\], chap. 1 |
| --- | --- | --- |
| ``` Blah Blah [@knuth1984, pp. 33-35, 38-39 and passim] ``` | Blah Blah ([Knuth 1984, 33–35, 38–39](https://quarto.org/docs/authoring/citations.html#ref-knuth1984) and passim) | Blah Blah \[1\], pp. 33-35, 38-39 and passim |
| ``` Blah Blah [@wickham2015; @knuth1984]. ``` | Blah Blah ([Wickham 2015](https://quarto.org/docs/authoring/citations.html#ref-wickham2015); [Knuth 1984](https://quarto.org/docs/authoring/citations.html#ref-knuth1984)). | Blah Blah \[1, 2\]. |
| ``` Wickham says blah [-@wickham2015] ``` | Wickham says blah ([^2]) | Wickham says blah \[1\] |

You can also write in-text citations, as follows:

| ``` @knuth1984 says blah. ``` | Knuth ([^1]) says blah. | \[1\] says blah. |
| --- | --- | --- |
| ``` @knuth1984 [p. 33] says blah. ``` | Knuth ([1984, 33](https://quarto.org/docs/authoring/citations.html#ref-knuth1984)) says blah. | \[1\] \[p. 33\] says blah. |

See the [Pandoc Citations](https://pandoc.org/MANUAL.html#citations) documentation for additional information on citation syntax.

## Citation Style

Quarto uses Pandoc to format citations and bibliographies. By default, Pandoc will use the [Chicago Manual of Style](https://chicagomanualofstyle.org/) author-date format, but you can specify a custom formatting using CSL ([Citation Style Language](https://citationstyles.org/)). To provide a custom citation stylesheet, provide a path to a CSL file using the `csl` metadata field in your document, for example:

```yaml
---
title: "My Document"
bibliography: references.bib
csl: nature.csl
---
```

You can find CSL files or learn more about using styles at the [CSL Project](https://github.com/citation-style-language/styles). You can browse the list of more than 8,500 Creative Commons CSL definitions in the CSL Project’s [central repository](https://github.com/citation-style-language/styles) or Zotero’s [style repository](https://www.zotero.org/styles).

`CSL` styling is only available when the `cite-method` is `citeproc` (which it is by default). If you are using another `cite-method`, you can control the formatting of the references using the mechanism provided by that method.

## Bibliography Generation

By default, Pandoc will automatically generate a list of works cited and place it in the document if the style calls for it. It will be placed in a div with the id `refs` if one exists:

```markdown
### References

::: {#refs}
:::
```

If no such div is found, the works cited list will be placed at the end of the document.

Tip

You can suppress generation of a bibliography by including `suppress-bibliography: true` option in your document metadata

Here’s an example of a generated bibliography:

## Including Uncited Items

If you want to include items in the bibliography without actually citing them in the body text, you can define a dummy `nocite` metadata field and put the citations there:

```markdown
---
nocite: |
  @item1, @item2
---

@item3
```

In this example, the document will contain a citation for `item3` only, but the bibliography will contain entries for `item1`, `item2`, and `item3`.

It is possible to create a bibliography with all the citations, whether or not they appear in the document, by using a wildcard:

```markdown
---
nocite: |
  @*
---
```

## LaTeX: using BibLaTeX or natbib

When creating PDFs, you can choose to use either the default Pandoc [citation handling](https://pandoc.org/MANUAL.html#citations) based on citeproc, or alternatively use [natbib](https://ctan.org/pkg/natbib) or [BibLaTeX](https://ctan.org/pkg/biblatex). This can be controlled using the `cite-method` option. For example:

```yaml
format:
  pdf: 
    cite-method: biblatex
```

The default is to use `citeproc` (Pandoc’s built in citation processor).

See the main article on using [Citations](https://quarto.org/docs/authoring/citations.html) with Quarto for additional details on citation syntax, available bibliography formats, etc.

### Options

When using natbib or biblatex you can specify the following additional options to affect how bibliographies are rendered:

| biblatexoptions | List of options for biblatex |
| --- | --- |
| natbiboptions | List of options for natbib |
| biblio-title | Title for bibliography |
| biblio-style | Style for bibliography |

## Typst

Typst comes with its [own citation processing system for bibliographies](https://typst.app/docs/reference/model/bibliography/) and using `format: typst` defaults to it.

Use the `csl` option to specify a bibliography style for Typst’s citation processing. The value can be a path to a CSL file or one of [Typst’s built-in styles](https://typst.app/docs/reference/model/bibliography/#parameters-style):

```
document.qmd
```

```yaml
---
bibliography: refs.bib
csl: my-style.csl
---
```

```
document.qmd
```

```yaml
---
bibliography: refs.bib
csl: apa
---
```

The `bibliographystyle` option is also supported and accepts the same values as `csl`.

If you prefer to use Pandoc’s citation processing instead of Typst’s, set `citeproc: true` explicitly:

```
document.qmd
```

```yaml
---
citeproc: true
bibliography: refs.bib
csl: https://www.zotero.org/styles/apa-with-abstract
---
```

See [Citation Style](https://quarto.org/docs/authoring/citations.html#sec-citations-style) for more on specifying citation styles with Pandoc’s system.

[^1]: Knuth, Donald E. 1984. “Literate Programming.” *The Computer Journal* 27 (2): 97–111.

[^2]: Wickham, Hadley. 2015. *R Packages*. 1st ed. O’Reilly Media, Inc.