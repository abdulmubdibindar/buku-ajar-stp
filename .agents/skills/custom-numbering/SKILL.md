---
name: custom-numbering
description: Guides the agent on how to use, configure, and implement custom automatic numbering systems in Quarto book projects (for HTML and PDF/LaTeX output). Use this skill when tasked with configuring Quarto cross-references, writing Lua filters for sequence counting, or setting up pre-render scripts for counter resets.
---

# Custom Numbering in Quarto Books

This skill provides generic guidelines for configuring, applying, and extending custom automatic numbering systems in Quarto book projects.

---

## 1. Chapter-Based Numbering (Quarto Custom Floats)

Use this approach when blocks need to be numbered relative to the current chapter (e.g., "Figure 1.1", "Case 3.2"), support captions, and allow standard cross-referencing (`@key-id`).

### Configuration (`_quarto.yml`)
Register the custom float type under `crossref.custom`:
```yaml
crossref:
  chapters: true
  custom:
    - kind: float
      key: customkey
      reference-prefix: "Custom Label"
      caption-prefix: "Custom Label"
```

### Usage in Markdown
Wrap the block in a fenced div containing a unique ID prefixed with the custom key and the class, followed by a heading for the title/caption:
```markdown
::: {#customkey-unique-identifier}
### Title of the Block

Content of the block...
:::
```

*Note: Quarto will automatically prefix the title with "Custom Label [Chapter].[Index]: " during render. Do not hardcode the numbering.*

---

## 2. Global-Sequential Numbering (Lua Filters & Pre-Render)

Use this approach when blocks must be numbered sequentially across the entire book regardless of chapters (e.g., "Exercise 1", "Exercise 2", ..., "Exercise 50") and do not require complex native Quarto float properties.

### Step 1: Pre-Render Script (Counter Reset)
Configure a pre-render script to delete the temporary counter file before compilation begins. This ensures numbering resets to a clean slate.

**In `reset_counter.R` or `reset_counter.py`**:
```R
# R example
if (file.exists("custom_counter.txt")) {
  file.remove("custom_counter.txt")
}
```

Register the pre-render script in `_quarto.yml`:
```yaml
project:
  pre-render: reset_counter.R
```

### Step 2: Pandoc Lua Filter
Write a Pandoc Lua filter to dynamically read, increment, and update the counter, prepending the label to the target div container.

**Example `custom-filter.lua`**:
```lua
local counter_file = "custom_counter.txt"

function Div(el)
  if el.classes:includes("custom-numbered-class") then
    local count = 0
    local f = io.open(counter_file, "r")
    if f then
      local content = f:read("*all")
      count = tonumber(content) or 0
      f:close()
    end
    
    count = count + 1
    
    f = io.open(counter_file, "w")
    if f then
      f:write(tostring(count))
      f:close()
    end
    
    local prefix = pandoc.Para({
      pandoc.Strong({pandoc.Str("Custom Label " .. count .. ": ")})
    })
    table.insert(el.content, 1, prefix)
    return el
  end
end
```

Register the filter in `_quarto.yml`:
```yaml
filters:
  - custom-filter.lua
```

### Step 3: Usage in Markdown
Apply the class inside a fenced div block without any manual headings:
```markdown
::: {.custom-numbered-class}
Content of the block...
:::
```

---

## 3. Formatting and Layout Best Practices

To ensure blocks render correctly in HTML, PDF, and other target formats:

1. **Avoid HTML Render Errors**: Always leave exactly **one blank line** before and after the fenced div lines (`:::`) in the markdown.
2. **HTML Styling (CSS)**: Define custom classes in the project stylesheet (e.g., `style.css`) to style borders, background colors, and margins:
   ```css
   .custom-numbered-class {
       padding: 1em;
       margin: 1em 0;
       border-left: 6px solid #9c27b0;
       background-color: #f3e5f5;
   }
   ```
3. **PDF/LaTeX Styling (Preamble)**: Define matching environment boxes using LaTeX packages like `tcolorbox` in the preamble header (e.g., `preamble.tex`):
   ```latex
   \usepackage{tcolorbox}
   \newtcolorbox{custom-numbered-class}{
     colback=gray!10,
     colframe=black,
     boxrule=0.5pt,
     leftrule=6pt
   }
   ```
