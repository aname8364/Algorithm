local function reduce(arr, callback, val)
    local x = val or 0
    for i,v in ipairs(arr) do
        x = callback(x, v)
    end
    return x
end

local n = io.read("n")
local t = {} for i=1, n do t[#t+1] = io.read("n") end
local v = io.read("n")

print(reduce(t, function(x,y)return y==v and x+1 or x end))