--[[
callout-buku.lua — callout khas buku ini.

Penulisan:

  ::: {#kasus-jarak-hunian .kasus title="Rata-rata Jarak per Jenis Hunian"}
  Isi...
  :::

Jenis bernomor (masuk TOC kanan di HTML):
  .capaian  -> "Capaian Pembelajaran Bab X"
  .kasus    -> "Studi Kasus X.n"
  .latihan  -> "Soal Latihan X.n"
Jenis tanpa nomor (tidak masuk TOC):
  .penting  -> "Penting"
  .catatan  -> "Catatan"

Rujukan @kasus-…, @latihan-…, @capaian-… dicetak sebagai label bertaut.
Label lintas bab diambil dari _callout-index.json (dibuat oleh
_scripts/indeks_callout.py saat pre-render); tanpa indeks, hanya rujukan di
dokumen yang sama yang bisa diselesaikan.

HTML: diubah menjadi callout Quarto (div .callout-*), ditambah heading
tersembunyi sebelum callout bernomor agar judulnya muncul di TOC.
Typst: dibungkus #kotak-buku (lihat _typst/kotak-buku.typ) yang boleh
terpotong antarhalaman.
]]

local JENIS = {
  capaian = { callout = "tip", numbered = true },
  kasus = { callout = "warning", numbered = true },
  latihan = { callout = "important", numbered = true },
  penting = { callout = "caution", numbered = false, label = "Penting" },
  catatan = { callout = "note", numbered = false, label = "Catatan" },
}

local function label_for(kind, bab, n)
  if kind == "capaian" then
    return "Capaian Pembelajaran Bab " .. bab
  elseif kind == "kasus" then
    return "Studi Kasus " .. bab .. "." .. n
  elseif kind == "latihan" then
    return "Soal Latihan " .. bab .. "." .. n
  end
  return JENIS[kind].label
end

local function is_html()
  return quarto.doc.is_format("html")
end

local function is_typst()
  return quarto.doc.is_format("typst")
end

-- Indeks lintas bab --------------------------------------------------------

local function project_dir()
  if quarto.project and quarto.project.directory then
    return quarto.project.directory
  end
  return "."
end

local function read_index()
  local f = io.open(pandoc.path.join({ project_dir(), "_callout-index.json" }), "r")
  if not f then
    return { chapters = {}, callouts = {} }
  end
  local ok, data = pcall(pandoc.json.decode, f:read("a"))
  f:close()
  if not ok or type(data) ~= "table" then
    return { chapters = {}, callouts = {} }
  end
  data.chapters = data.chapters or {}
  data.callouts = data.callouts or {}
  return data
end

local function current_file()
  local input = quarto.doc.input_file or ""
  return pandoc.path.make_relative(input, project_dir())
end

local function output_html(file)
  return (file:gsub("%.qmd$", ".html"))
end

-- Utilitas -----------------------------------------------------------------

local function kind_of(div)
  for _, c in ipairs(div.classes) do
    if JENIS[c] then
      return c
    end
  end
end

local function is_unnumbered(header)
  return header.classes:includes("unnumbered")
end

local function parse_inlines(text)
  local doc = pandoc.read(text, "markdown")
  if #doc.blocks == 0 then
    return pandoc.Inlines({})
  end
  return doc.blocks[1].content
end

local function typst_inlines(inlines)
  return pandoc.write(pandoc.Pandoc({ pandoc.Plain(inlines) }), "typst"):gsub("%s+$", "")
end

-- Penomoran ----------------------------------------------------------------

local state = {
  bab = 0,
  counters = {},
  labels = {}, -- id -> label untuk dokumen ini
}

local function next_number(kind)
  state.counters[kind] = (state.counters[kind] or 0) + 1
  return state.counters[kind]
end

local function render_callout(div, kind, toc_level)
  local spec = JENIS[kind]
  local n = spec.numbered and next_number(kind) or nil
  local label = label_for(kind, state.bab, n)

  -- Judul: atribut title, atau heading pertama di dalam div (sintaks lama).
  local content = div.content
  local title
  if div.attributes.title and div.attributes.title ~= "" then
    title = parse_inlines(div.attributes.title)
  elseif #content > 0 and content[1].t == "Header" then
    title = content[1].content
    content = pandoc.Blocks({ table.unpack(content, 2) })
  end

  local full = pandoc.Inlines({ pandoc.Str(label) })
  if title and #title > 0 and kind ~= "capaian" then
    full:insert(pandoc.Str(":"))
    full:insert(pandoc.Space())
    full:extend(title)
  end

  local id = div.identifier
  if id ~= "" and spec.numbered then
    state.labels[id] = label
  end

  if is_typst() then
    local out = pandoc.Blocks({
      pandoc.RawBlock("typst", '#kotak-buku(jenis: "' .. kind .. '", judul: [' .. typst_inlines(full) .. "])["),
    })
    out:extend(content)
    out:insert(pandoc.RawBlock("typst", "]" .. (id ~= "" and (" <" .. id .. ">") or "")))
    return out
  end

  local out = pandoc.Blocks({})
  if is_html() and spec.numbered and toc_level then
    -- Heading tersembunyi (lihat style.css) agar judul callout masuk TOC.
    local toc_id = "toc-buku-" .. (id ~= "" and id or (kind .. "-" .. state.bab .. "-" .. n))
    out:insert(pandoc.Header(toc_level, full:clone(), pandoc.Attr(toc_id, { "unnumbered" })))
  end
  -- Judul lewat atribut title, bukan heading: heading di dalam callout
  -- akan ikut masuk TOC. Id dipasang di pembungkus karena Quarto tidak
  -- mempertahankan id pada div callout.
  local callout = quarto.Callout({
    type = spec.callout,
    title = full,
    content = content,
    icon = false,
    attr = pandoc.Attr("", { "buku-" .. kind }),
  })
  out:insert(pandoc.Div({ callout }, pandoc.Attr(id, { "buku-callout" })))
  return out
end

-- Menelusuri blok sambil melacak bab dan level heading aktif.
-- toc = true hanya untuk blok tingkat atas (heading TOC tidak bisa di
-- dalam div lain).
local process_blocks

process_blocks = function(blocks, toc, merged)
  local out = pandoc.Blocks({})
  local level = 1
  for _, block in ipairs(blocks) do
    if block.t == "Header" then
      if block.level == 1 and merged and not is_unnumbered(block) then
        state.bab = state.bab + 1
        state.counters = {}
      end
      level = block.level
      out:insert(block)
    elseif block.t == "Div" then
      local kind = kind_of(block)
      if kind then
        block.content = process_blocks(block.content, false, merged)
        -- TOC HTML hanya sampai level 3 (toc-depth bawaan).
        out:extend(render_callout(block, kind, toc and math.min(level + 1, 3) or nil))
      else
        block.content = process_blocks(block.content, false, merged)
        out:insert(block)
      end
    else
      out:insert(block)
    end
  end
  return out
end

-- Rujukan ------------------------------------------------------------------

local function resolve_cites(doc, index)
  local here = current_file()
  return doc:walk({
    Cite = function(cite)
      if #cite.citations ~= 1 then
        return nil
      end
      local id = cite.citations[1].id
      if not (id:match("^kasus%-") or id:match("^latihan%-") or id:match("^capaian%-")) then
        return nil
      end
      local entry = index.callouts[id]
      local label = state.labels[id] or (entry and entry.label)
      if not label then
        quarto.log.warning("callout-buku: rujukan tidak dikenal @" .. id)
        return pandoc.Strong({ pandoc.Str("??" .. id) })
      end
      local target = "#" .. id
      if is_html() and entry and not state.labels[id] and entry.file ~= output_html(here) then
        target = entry.file .. "#" .. id
      end
      return pandoc.Link({ pandoc.Str(label) }, target)
    end,
  })
end

-- Entri --------------------------------------------------------------------

function Pandoc(doc)
  local index = read_index()

  -- Buku Typst digabung menjadi satu dokumen: bab dihitung dari H1.
  -- HTML dirender per bab: nomor bab diambil dari indeks/nama berkas.
  local numbered_h1 = 0
  for _, b in ipairs(doc.blocks) do
    if b.t == "Header" and b.level == 1 and not is_unnumbered(b) then
      numbered_h1 = numbered_h1 + 1
    end
  end
  local merged = numbered_h1 > 1

  if not merged then
    local file = current_file()
    local bab = index.chapters[file] or tonumber(pandoc.path.filename(file):match("^(%d+)%-")) or 0
    state.bab = math.tointeger(bab) or bab
  end

  doc.blocks = process_blocks(doc.blocks, true, merged)
  return resolve_cites(doc, index)
end
