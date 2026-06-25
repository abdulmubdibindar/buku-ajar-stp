local counter_file = "soal_counter.txt"

function Div(el)
  if el.classes:includes("soal-evaluasi") then
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
      pandoc.Strong({pandoc.Str("Soal Evaluasi " .. count .. ": ")})
    })
    table.insert(el.content, 1, prefix)
    return el
  end
end
