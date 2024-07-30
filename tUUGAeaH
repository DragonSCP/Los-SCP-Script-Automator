_G.objs = {}

getgenv().spoof = function(obj, property, value)
	local s = pcall(function()
		local lol = obj[property]
	end)
	if s then
		table.insert(_G.objs, {obj, property, value})
	end
end

getgenv().findwithintable = function(o, p)
	for i, v in pairs(_G.objs) do
		if table.find(v, o) and table.find(v, p) then
			return v
		end
	end
	return nil
end

getgenv().unspoof = function(obj, property)
	local lol = findwithintable(obj, property)
	if lol then
		table.remove(_G.objs, table.find(_G.objs, lol))
	end
end


local mt = getrawmetatable(game)
setreadonly(mt, false)
old = mt.__index

mt.__index = newcclosure(function(o, p)
	local t = findwithintable(o, p)
	if t ~= nil then
		return t[3]
	end
	
	return old(o, p)
end)
