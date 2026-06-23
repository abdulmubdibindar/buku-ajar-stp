---
title: "VS Code"
source: "https://quarto.org/docs/tools/vscode/index.html"
author:
published:
created: 2026-06-09
description:
tags:
  - "clippings"
---
## Overview

Quarto can render Jupyter notebooks represented as plain text (`.qmd`) or as a normal notebook file (`.ipynb`). The [Quarto VS Code Extension](https://marketplace.visualstudio.com/items?itemName=quarto.quarto) includes many tools that enhance working these documents, including:

- Integrated render and preview for Quarto documents.
- Syntax highlighting for markdown and embedded languages
- Completion and diagnostics for YAML options
- Completion for embedded languages (e.g. Python, R, Julia, etc.)
- Commands and key-bindings for running cells and selected lines.
- Live preview for LaTeX math as well as Mermaid and Graphviz diagrams

The Quarto extension integrates directly with the Jupyter, R, and Julia extensions. For example, here the Quarto extension runs a Python cell and shows contextual help for Python functions:

You can install the Quarto extension from the [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=quarto.quarto) or the [Open VSX Registry](https://open-vsx.org/extension/quarto/quarto).

## VS Code Editors

Depending on your preference and the task at hand, you can author documents for rendering by Quarto using three different editors within VS Code:

1. The source code editor for editing `.qmd` documents as text.
2. The [Visual Editor](https://quarto.org/docs/tools/vscode/visual-editor.html) for WYSIWYG editing of `.qmd` documents.
3. The [Notebook Editor](https://quarto.org/docs/tools/vscode/notebook.html) for editing `.ipynb` notebooks.

We’ll cover the source code editor below, however you might also want to consult the documentation for the [Visual Editor](https://quarto.org/docs/tools/vscode/visual-editor.html) or [Notebook Editor](https://quarto.org/docs/tools/vscode/notebook.html) after you’ve become familiar with the basics.

## Render and Preview

The Quarto VS Code extension includes commands and keyboard shortcuts for rendering Quarto documents (both standalone and within websites or books). After rendering, `quarto preview` is used behind the scenes to provide a preview pane within VS Code alongside your document:

![Two windows arranged side by side. The window on the left is a qmd file opened in VS Code. The contents of this document are the same as the first part of the Getting Started: Welcome section of this website. The contents of this document are rendered by Quarto in the window on the right.](https://quarto.org/docs/tools/images/vscode-render-dark.png)

To render and preview, execute the **Quarto: Preview** command. You can alternatively use the Ctrl+Shift+K keyboard shortcut, or the **Preview** button (![Preview icon](https://quarto.org/docs/tools/images/vscode-preview-icon.svg)) at the top right of the editor:

![The top of the VS Code editor. The right side of the editor tab area includes a Preview button.](https://quarto.org/docs/tools/images/vscode-preview-button.png)

Note that on the Mac you should use `Cmd` rather than `Ctrl` as the prefix for all Quarto keyboard shortcuts.

### Other Formats

The **Quarto: Preview** command renders the default format of the currently active document. If you want to preview a different format, use the **Quarto: Preview Format** command:

![The top of the VS Code editor. The editor title menu is expanded and the Preview Format command is available on the menu.](https://quarto.org/docs/tools/images/vscode-preview-format-menu.png)

When you execute **Preview Format**, you’ll see a quick pick list of formats to choose from (any formats declared in the document as well as some standard formats like PDF and MS Word):

![The top of the VS Code editor. The command pallette shows a quick pick list of available formats to preview.](https://quarto.org/docs/tools/images/vscode-preview-format.png)

After previewing a different format, the **Quarto: Preview** command and Ctrl+Shift+K keyboard shortcut will be automatically rebound to the newly selected format for the duration of the current preview. To switch back to previewing the original format, use **Quarto: Preview Format** command again.

Embedded preview is currently supported for HTML and PDF based formats (including `revealjs` and `beamer` slideshows). However, for Word and other formats you need to use an appropriate external program to preview the output.

### Render Command

The **Quarto: Preview** command is what you will most commonly use while authoring documents. If you have a single format (e.g. HTML or PDF) then previewing also renders your document so it’s ready for distribution once you are happy with the output. However, if you have multiple formats will need to explicitly render them (as preview only renders a single format at a time). You can do this with the **Quarto: Render Document** command:

![The top of the VS Code editor. The command palette shows a quick pick list of available formats to render.](https://quarto.org/docs/tools/images/vscode-render-command.png)

If you have multiple declared formats you can render all of them. You can also selectively render any of the declared formats or other standard formats like PDF and MS Word.

## Render on Save

By default Quarto does not automatically render `.qmd` or `.ipynb` files when you save them. This is because rendering might be very time consuming (e.g. it could include long running computations) and it’s good to have the option to save periodically without doing a full render.

However, you can configure the Quarto extension to automatically render whenever you save. You can do this either within VS Code settings or within the YAML options for your project or document. To configure the VS Code setting, search for `quarto.render` in settings and you’ll find the **Render on Save** option:

![The VS Code Quarto render settings. The Render on Save option is checked.](https://quarto.org/docs/tools/images/vscode-render-on-save.png)

You might also want to control this behavior on a per-document or per-project basis. If you include the `editor: render-on-save` option in your document or project YAML it will supersede whatever your VS Code setting is. For example:

## External Preview

If you prefer to use an external browser for preview (or have no preview triggered at all by rendering) you can use the **Preview Type** option to specify an alternate behavior:

![VS Code settings interface with 'quarto preview type' entered into the search bar. User settings reveals Quarto > Render: Preview Type, with a dropdown to select location for document preview after render. The default, internal, is selected, which previews using a side-by-side panel in VS Code. The other two options in the dropdown are external and none.](https://quarto.org/docs/tools/images/vscode-preview-settings.png)

## Code Cells

There are a variety of tools that make it easier to edit and execute code cells. Editing tools include syntax highlighting, code folding, code completion, and signature tips:

![A Quarto document in VS Code with a python code cell. There is a code completion helper active in the python cell.](https://quarto.org/docs/tools/images/vscode-code-cell.png)

For Python, R, and Julia cells, commands are available to execute the current cell, previous cells, or the currently selected line(s). Cell output is shown side by side in the Jupyter interactive console: R and Python cells are executed in the appropriate Console, and output is shown in the pane:

![VS Code with two panes open, source code on the right, and the interactive output of that code shown in a second pane on the left.](https://quarto.org/docs/tools/images/vscode-execute-cell.png)

Here are all of the commands and keyboard shortcuts available for executing cells:

| Run Current Cell | ⇧⌃ Enter |
| --- | --- |
| Run Selected Line(s) | ⌃ Enter |
| Run Next Cell | ⌥⌃ N |
| Run Previous Cell | ⌥⌃ P |
| Run All Cells | ⌥⌃ R |
| Run Cells Above | ⇧⌥⌃ P |
| Run Cells Below | ⇧⌥⌃ N |

You can quickly insert a new code cell using the Ctrl+Shift+I keyboard shortcut.

Enhanced features for embedded languages (e.g. completion, code execution) can be enabled by installing the most recent version(s) of these extensions:

- [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [Jupyter Extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
- [R Extension](https://marketplace.visualstudio.com/items?itemName=REditorSupport.r)
- [Julia Extension](https://marketplace.visualstudio.com/items?itemName=julialang.language-julia)

### Execution Directory

Embedded language extensions handle the working directory for execution in distinct ways:

1. The Python Extension runs code within the directory of the source file from which code is executed. You can customize this behavior using the `jupyter.notebookFileRoot` option.
2. The R Extension runs code within the working directory of the R session running in the **R Interactive** terminal. You can change this directory manually using `setwd()`.
3. The Julia Extension runs code within the working directory of the Julia session running in the **Julia REPL** terminal. You can change this directory manually using `cd()`.

## Contextual Assistance

Execute the **Quarto: Show Assist Panel** command to show a panel in the sidebar that shows contextual assistance depending on the current cursor location:

1. Help/documentation is shown when editing code
2. A realtime preview of equations is shown when editing LaTeX math
3. Thumbnail previews are shown when your cursor is located on a markdown image.

For example, below help on the matplotlib `plot()` function is shown automatically when the cursor is located on the function:

![Screenshot of VS Code editor with three vertical sections. The leftmost includes the file explorer, and quarto help. The second pane is the source code for a quarto file with python code. The third is interactive with Python running and output of the code cells shown.](https://quarto.org/docs/computations/images/python-vscode.png)

## Live Preview

While editing LaTeX math or Mermaid and Graphviz diagrams, click the **Preview** button above the code (or use the Ctrl+Shift+L keyboard shortcut) to open a live preview which will update automatically as you edit.

Here we see a preview of the currently edited LaTeX equation displayed in the Quarto assist panel:

![Quarto document open in VS Code with a LaTeX equation shown in the 'Quarto Equation' section of the panel to the left of the document.](https://quarto.org/docs/tools/images/vscode-equation.png)

Here we see a Graphviz diagram preview automatically updated as we edit:

## YAML Intelligence

YAML code completion is available for project files, YAML front matter, and executable cell options:

![Quarto document with YAML being edited. Next to the cursor code completion helper is open showing YAML options beginning with the letters preceding the cursor ('co').](https://quarto.org/docs/tools/images/vscode-yaml-completion.png)

If you have incorrect YAML it will also be highlighted when documents are saved:

![Quarto document YAML metadata with an incorrect option underlined in red.](https://quarto.org/docs/tools/images/vscode-yaml-diagnostics.png)

## Code Snippets

Code snippets are templates that make it easier to enter repeating code patterns (e.g. code blocks, callouts, divs, etc.). Execute the **Insert Snippet** command within a Quarto document to insert a markdown snippet:

![Quarto document with dropdown 'Select a snippet' dropdown, the first item (bold - insert bold text) is selected.](https://quarto.org/docs/tools/images/vscode-snippets.png)

### IntelliSense

VS Code uses IntelliSense to suggest snippets or possible values for a specific function while typing. This is turned off by default for snippets, but not for values. To enable snippet suggestions in IntelliSense while typing or when selecting a text snippet and pressing `ctrl+space`, the setting `editor.snippetSuggestions` needs to be set to a value other than `none` (for example to `inline`).

- Press `F1` and search for `Preferences: Open Settings (UI)` or `File` > `Preferences` > `Settings`
- Search for following term `@lang:quarto editor.snippetSuggestions`. `Editor: Snippet Suggestions` should show up.
- Change value to a not- `none` value.

## Learning More

Besides the traditional source editor described above, you can also use one of the following other editors depending on your preferences and task at hand:

1. The [Visual Editor](https://quarto.org/docs/tools/vscode/visual-editor.html) for WYSIWYG editing of `.qmd` documents.
2. The [Notebook Editor](https://quarto.org/docs/tools/vscode/notebook.html) for editing `.ipynb` notebooks.