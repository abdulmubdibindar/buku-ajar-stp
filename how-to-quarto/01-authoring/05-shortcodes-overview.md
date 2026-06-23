---
title: "Shortcodes"
source: "https://quarto.org/docs/authoring/shortcodes.html"
author:
published:
created: 2026-06-09
description:
tags:
  - "clippings"
---
## Overview

Shortcodes are special markdown directives that generate various types of content. Quarto shortcodes are similar in form and function to [Hugo shortcodes](https://gohugo.io/content-management/shortcodes/) and [WordPress shortcodes](https://codex.wordpress.org/Shortcode).

For example, the following shortcode prints the `title` from document metadata:

```markdown
{{< meta title >}}
```

## Built-in Shortcodes

Quarto supports several shortcodes natively:

| [version](https://quarto.org/docs/authoring/version.html) | Print Quarto CLI version |
| --- | --- |
| [var](https://quarto.org/docs/authoring/variables.html#var) | Print value from `_variables.yml` file |
| [meta](https://quarto.org/docs/authoring/variables.html#meta) | Print value from document metadata |
| [env](https://quarto.org/docs/authoring/variables.html#url) | Print system environment variable |
| [pagebreak](https://quarto.org/docs/authoring/markdown-basics.html#page-breaks) | Insert a native page-break |
| [kbd](https://quarto.org/docs/authoring/markdown-basics.html#keyboard-shortcuts) | Describe keyboard shortcuts |
| [video](https://quarto.org/docs/authoring/videos.html) | Embed a video in a document |
| [include](https://quarto.org/docs/authoring/includes.html) | Include contents of another qmd |
| [embed](https://quarto.org/docs/authoring/notebook-embed.html) | Embed cells from a Jupyter Notebook |
| [placeholder](https://quarto.org/docs/authoring/placeholder.html) | Add placeholder images to your document |
| [lipsum](https://quarto.org/docs/authoring/lipsum.html) | Add placeholder text to your document |
| [contents](https://quarto.org/docs/authoring/contents.html) | Rearrange content in your document |

If you want to dive in to creating your own shortcode, check out the article on [Creating Shortcodes](https://quarto.org/docs/extensions/shortcodes.html).