local AllIDs = {}
local foundAnything = ""
local actualHour = os.date("!*t").hour
local Deleted = false
local S_T = game:GetService("TeleportService")
local S_H = game:GetService("HttpService")

local File = pcall(function()
	AllIDs = S_H:JSONDecode(readfile("server-hop-temp.json"))
end)
if not File then
	table.insert(AllIDs, actualHour)
	pcall(function()
		writefile("server-hop-temp.json", S_H:JSONEncode(AllIDs))
	end)
end

-- Substitua pelo seu código de convite
local inviteCode = "5239febc246de0448171a058051f078b"

local function TPReturner(placeId)
	local Site;
	if foundAnything == "" then
		Site = S_H:JSONDecode(game:HttpGet('https://games.roblox.com/v1/games/' .. placeId .. '/servers/Public?sortOrder=Asc&limit=100'))
	else
		Site = S_H:JSONDecode(game:HttpGet('https://games.roblox.com/v1/games/' .. placeId .. '/servers/Public?sortOrder=Asc&limit=100&cursor=' .. foundAnything))
	end
	local ID = ""
	if Site.nextPageCursor and Site.nextPageCursor ~= "null" and Site.nextPageCursor ~= nil then
		foundAnything = Site.nextPageCursor
	end
	local num = 0;
	for i, v in pairs(Site.data) do
		local Possible = true
		ID = tostring(v.id)
		if tonumber(v.maxPlayers) > tonumber(v.playing) then
			for _, Existing in pairs(AllIDs) do
				if num ~= 0 then
					if ID == tostring(Existing) then
						Possible = false
					end
				else
					if tonumber(actualHour) ~= tonumber(Existing) then
						local delFile = pcall(function()
							delfile("server-hop-temp.json")
							AllIDs = {}
							table.insert(AllIDs, actualHour)
						end)
					end
				end
				num = num + 1
			end
			if Possible == true then
				table.insert(AllIDs, ID)
				wait()
				pcall(function()
					writefile("server-hop-temp.json", S_H:JSONEncode(AllIDs))
					wait()
					S_T:TeleportToPlaceInstance(placeId, ID, game.Players.LocalPlayer)
				end)
				wait(4)
			end
		end
	end
end

local module = {}
function module:Teleport(placeId)
	while wait() do
		pcall(function()
			-- Aqui você deve substituir a chamada para TPReturner com o código para usar o inviteCode
			-- No entanto, Roblox não tem suporte direto para convite por código de servidor via API pública
			-- Para um servidor específico, você pode usar o método TeleportToPlaceInstance se souber o ID da instância
			-- Exemplo:
			-- S_T:TeleportToPlaceInstance(placeId, instanceId, game.Players.LocalPlayer)

			-- Um código de exemplo para teleportar para um lugar específico:
			local success, result = pcall(function()
				S_T:Teleport(placeId, game.Players.LocalPlayer)
			end)
			
			if not success then
				warn("Failed to teleport: " .. result)
			end

			-- Se foundAnything não estiver vazio, faça uma nova chamada
			if foundAnything ~= "" then
				TPReturner(placeId)
			end
		end)
	end
end
return module
