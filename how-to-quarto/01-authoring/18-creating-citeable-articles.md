---
title: "Creating Citeable Articles"
source: "https://quarto.org/docs/authoring/create-citeable-articles.html"
author:
published:
created: 2026-06-09
description:
tags:
  - "clippings"
---
You can make it easier for others to cite your work by providing additional metadata with the YAML front-matter of your article. Citations can be provided for both articles published to the web or for articles published in journals (with or without a DOI).

## Web Articles

To provide a citation for an article published to the web, include author and date metadata as well as a citation url. For example:

```yaml
---
title: "Summarizing Output for Reproducible Documents"
description: | 
  A summary of the best practices for summarizing output of reproducible scientific documents.
date: 5/4/2018

  - name: Norah Jones 
    url: https://example.com/norahjones
    affiliation: Spacely Sprockets
    affiliation-url: https://example.com/spacelysprockets
citation:
  url: https://example.com/summarizing-output
bibliography: biblio.bib
---
```

Name particles can be further defined in the `name` key following the [Citation Style Language (CSL) specification for naming particles](https://docs.citationstyles.org/en/stable/specification.html#name-particles). If you omit the citation url, Quarto will attempt to generate a citation url by using the `site-url` and the current page’s location. If you’d like to allow Quarto to generate the citation url, you can omit the citation url and simply enable citation output on the page. For example:

```yaml
---
title: "Summarizing Output for Reproducible Documents"
description: | 
  A summary of the best practices for summarizing output of reproducible scientific documents.
date: 5/4/2018

  - name: Norah Jones 
    url: https://example.com/norahjones
    affiliation: Spacely Sprockets
    affiliation-url: https://example.com/spacelysprokets
citation: true
bibliography: biblio.bib
---
```

When this metadata is available, a citation appendix is automatically added to the article. The citation appendix will present both a copy-able `bibtex` representation of the document and a formatted representation of the citation (based upon the document’s CSL file, if specified). For example:

By default both the `bibtex` and formatted representations are displayed. You can use the `appendix-cite-as` option to control this behavior:

| `appendix-cite-as: false` | Do not include any citations in the appendix. |
| --- | --- |
| `appendix-cite-as: bibtex` | Show only the BibTeX version of the citation. |
| `appendix-cite-as: display` | Show only the display version of the citation. |

## Journal Articles

If your article is published within a Journal, you can add the following the additional fields to generate the appropriate citation entry:

```yaml
---
title: "Summarizing Output for Reproducible Documents"
description: | 
  A summary of the best practices for summarizing output of reproducible scientific documents.
date: 5/4/2018

  - name: Norah Jones 
    url: https://example.com/norahjones
    affiliation: Spacely Sprockets
    affiliation-url: https://example.com/spacelysprokets
citation:
  type: article-journal
  container-title: "Journal of Data Science Software"
  doi: "10.23915/reprodocs.00010"
  url: https://example.com/summarizing-output
bibliography: biblio.bib
---
```

This is how the citation is presented in the appendix:

![Appearance of a journal citation in document appendix with both BibTex and plain text citations given for attribution.](https://quarto.org/docs/authoring/images/appendix-citation-journal.png)

## Other Types of Documents

The BibTeX and formatted attribution displayed in the document will be generated based upon the complete citation information that is present in the `citation` key, which is based upon the [Citation Style Language (CSL) specification for items](https://docs.citationstyles.org/en/stable/specification.html). You can learn more about the available options in the [Citation Metadata Reference](https://quarto.org/docs/reference/metadata/citation.html).

## Google Scholar

Quarto documents can include metadata compatible with the format indexed by [Google Scholar](https://scholar.google.com/). This makes it easy for indexing engines (Google Scholar or otherwise) to extract not only a citation for your article but also information on other sources which you cited. To enable this use the `google-scholar` option:

```yaml
title: "Summarizing Output for Reproducible Documents"
description: | 
  A summary of the best practices for summarizing output of reproducible scientific documents.
date: 5/4/2018

  - name: Norah Jones 
    url: https://example.com/norahjones
    affiliation: Spacely Sprockets
    affiliation-url: https://example.com/spacelysprokets
citation:
  type: article-journal
  container-title: "Journal of Data Science Software"
  doi: "10.23915/reprodocs.00010"
  url: https://example.com/summarizing-output
bibliography: biblio.bib 
google-scholar: true
```

For example, here is the Google Scholar metadata automatically included for a document created with the above metadata:

```html
<meta name="citation_title" content="Summarizing Output for Reproducible Documents">
<meta name="citation_author" content="Norah Jones">
<meta name="citation_online_date" content="2018-05-04">
<meta name="citation_fulltext_html_url" content="https://example.com/summarizing-output">
<meta name="citation_publication_date" content="2018-05-04">
<meta name="citation_journal_title" content="Journal of Data Science Software">
<meta name="citation_reference" content="citation_title=Donald knuth;,citation_fulltext_html_url=http://dx.doi.org/10.7551/mitpress/
5485.003.0041;,citation_publication_date=1989;,citation_journal_title
=undefined;">
```

In the addition to the citation metadata from this document described above, Quarto will automatically generate a `citatation_reference` entry for each of the entries included in the document’s bibliography.

## Citation Fields

Quarto’s approach to emitting scholarly metadata is to take the standard CSL fields and make them into the corresponding Google Scholar / Zotero / Highwire metadata tags as appropriate. The following fields, when specified under the `citation` key of the document metadata, will generate scholarly meta tags in the rendered HTML document as described. These fields comprise the required Google Scholar fields as well as additional, optional fields that may also be included.

<table><colgroup><col> <col> <col></colgroup><tbody><tr><td rowspan="2"><h2>Document Yaml</h2><p><code>title</code><br><sub>Document <code>title</code> will be used if not provided.</sub></p></td><td rowspan="2"><h2>Metadata Tag</h2><p><code>citation_title</code></p></td><td></td></tr><tr><td></td></tr><tr><td><code>author</code><br><sub>One or more authors <sup><a href="#fn:1">1</a></sup>. Document <code>author</code> will be used if not provided as a citation subkey.</sub></td><td><code>citation_author</code></td><td></td></tr><tr><td><code>editor</code><br><sub>One or more editors <sup><a href="#fn:2">2</a></sup>.</sub></td><td><code>citation_editor</code></td><td></td></tr><tr><td><code>abstract</code><br><sub>Document <code>abstract</code> will be used if not provided.</sub></td><td><code>citation_abstract</code></td><td></td></tr><tr><td><code>keyword</code> <sup><a href="#fn:3">3</a></sup><br><sub>Document <code>keywords</code> will be used if not provided.</sub></td><td><code>citation_keywords</code></td><td></td></tr><tr><td><code>issued</code><br><sub>Document <code>date</code> will be used if not provided.</sub></td><td><p><code>citation_publication_date</code></p><p><sub>In addition, the issued date will be used to populate the following fields:</sub><br><br><code>citation_cover_date</code><br><code>citation_year</code></p></td><td></td></tr><tr><td><code>available-date</code><br><sub>Document <code>date</code> will be used if not provided.</sub></td><td><code>citation_online_date</code></td><td></td></tr><tr><td colspan="3"><code>url</code> | <code>citation_fulltext_html_url</code> | <sub><code>url</code> will be synthesized for current document if a <a href="https://quarto.org/docs/websites/website-tools.html#preview-images"><code>site-url</code></a> has been specified.</sub> |</td></tr><tr><td><code>pdf-url</code></td><td><code>citation_pdf_url</code></td><td></td></tr><tr><td><code>language</code><br><sub>Document <code>lang</code> will be used if not provided.</sub></td><td><code>citation_language</code></td><td></td></tr><tr><td><code>type</code><br><sub>A valid CSL type. See <a href="https://docs.citationstyles.org/en/stable/specification.html#appendix-iii-types">https://docs.citationstyles.org/en/stable/specification.html#appendix-iii-types</a></sub>.</td><td><code><none></code></td><td></td></tr><tr><td><code>doi</code><br><sub>Document <code>doi</code> will be used if not provided.</sub></td><td><code>citation_doi</code></td><td></td></tr><tr><td><code>isbn</code></td><td><code>citation_isbn</code></td><td></td></tr><tr><td><code>issn</code></td><td><code>citation_issn</code></td><td></td></tr><tr><td><code>eissn</code></td><td><code>citation_eissn</code></td><td></td></tr><tr><td><code>pmid</code></td><td><code>citation_pmid</code></td><td></td></tr><tr><td><code>issue</code></td><td><code>citation_issue</code></td><td></td></tr><tr><td><code>volume</code></td><td><code>citation_volume</code></td><td></td></tr><tr><td><code>page</code><br><sub>Will be split on <code>-</code> to create appropriate page metadata.</sub></td><td><p><code>citation_firstpage</code></p><p><code>citation_lastpage</code></p></td><td></td></tr><tr><td><code>page-first</code></td><td><code>citation_firstpage</code></td><td></td></tr><tr><td><code>page-last</code></td><td><code>citation_lastpage</code></td><td></td></tr><tr><td><code>abstract-url</code></td><td><code>citation_abstract_html_url</code></td><td></td></tr><tr><td><code>container-title</code></td><td><p><code>citation_journal_title</code></p><p><small>For specific types, other meta tags will be produced:</small></p><ul><small><li><p>type: paper-conference<br><code>citation_conference_title</code></p></li><li><p>type: book<br><code>citation_book_title</code></p></li></small><li><p><small>type: chapter<br><code>citation_inbook_title</code></small></p></li></ul></td><td></td></tr><tr><td><code>number</code></td><td><p><code>citation_technical_report_number</code></p><p><sub><code>citation_technical_report_number</code> will be created if the type is report.</sub></p></td><td></td></tr><tr><td><code>publisher</code></td><td><p><code>citation_publisher</code></p><p><small>For specific types, other meta tags will be produced:</small></p><small><ul><li><p>type: paper-conference<br><code>citation_conference</code></p></li><li><p>type: thesis<br><code>citation_dissertation_institution</code></p></li><li><p>type:report<br><code>citation_technical_report_institution</code></p></li></ul></small></td><td></td></tr><tr><td><code>container-title-short</code></td><td><code>citation_journal_abbrev</code></td><td></td></tr><tr><td><code>collection-title</code></td><td><code>citation_series_title</code></td><td></td></tr></tbody></table>

For example, citation data for a published conference paper defined as such in the document front matter:

```yaml
title: A Published Conference Paper

  - name: Norah Jones
    affiliation: School of Hard Knocks
    orcid: 0000-0001-8715-9476
citation:
  type: paper-conference
  container-title: "Proceedings of the annual conference of the Society for Research"
  publisher: "Society for Research"
  issued: 2020/09/23
  volume: 2
  doi: "10.23915/reprodocs.00010"
  url: https://example.com/summarizing-output
  page-first: 46
  page-last: 53
  editor:
  - Don Draper
  - Nick Fury
google-scholar: true
```

provides HTML metadata like:

```html
<meta name="citation_title" content="A Published Conference Paper">
<meta name="citation_author" content="Norah Jones">
<meta name="citation_editor" content="Nick Cage">
<meta name="citation_editor" content="Don Draper">
<meta name="citation_publication_date" content="2020-09-23">
<meta name="citation_cover_date" content="2020-09-23">
<meta name="citation_year" content="2020">
<meta name="citation_fulltext_html_url" content="https://example.com/summarizing-output">
<meta name="citation_doi" content="10.23915/reprodocs.00010">
<meta name="citation_volume" content="2">
<meta name="citation_language" content="en">
<meta name="citation_conference_title" content="Proceedings of the annual conference of the Society for Research">
<meta name="citation_conference" content="Society for Research">
```

[^1]: Specify one or more authors using one of the following:

```yaml
author: Norah Jones
```

or multiple values like:

```yaml
author:
-   Norah Jones
-   Nick Fury
```

The list of authors provded under the citation key will be used instead of the document authors when generating the html metadata.

[^2]: Specify one or more editors using one of the following:

```yaml
editors: Norah Jones
```

or multiple values like:

```yaml
editors:
-   Norah Jones
-   Nick Fury
```

[^3]: Note that the `keyword` citation field is a comma separated string of keywords (consistent with CSL).