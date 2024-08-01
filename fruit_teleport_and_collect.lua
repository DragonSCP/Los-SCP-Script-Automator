-- FruitCollectorModule.lua

-- Espera o jogo carregar completamente
if not game:IsLoaded() then
    game.Loaded:Wait()
end

repeat
    task.wait()
until game:GetService("Players") and game:GetService("Workspace") and game:GetService("ReplicatedStorage")

local LocalPlayer = game:GetService("Players").LocalPlayer

-- Função para retornar o HumanoidRootPart
local function returnHRP()
    if not LocalPlayer.Character then
        return
    end
    return LocalPlayer.Character:FindFirstChild("HumanoidRootPart")
end

-- Função para retornar o Humanoid
local function returnHUM()
    if not LocalPlayer.Character then
        return
    end
    return LocalPlayer.Character:FindFirstChild("Humanoid")
end

repeat
    task.wait()
until returnHRP() and returnHUM()

-- Tabela de atributos do HumanoidRootPart
local HrpTable = {
    Velocity = returnHRP().Velocity,
    Transparency = returnHRP().Transparency,
    Rotation = returnHRP().Rotation,
    Size = returnHRP().Size,
    Orientation = returnHRP().Orientation,
    Anchored = returnHRP().Anchored
}

-- Função para spoofar o HumanoidRootPart
local function spoofHRP()
    for i, v in pairs(HrpTable) do
        spoof(returnHRP(), tostring(i), returnHRP():GetAttribute(v))
    end
    return true
end

-- Função para teletransportar o jogador
local function TpTo(CFrame, Refresh)
    if Refresh then
        returnHUM().Health = 0
        LocalPlayer.CharacterAdded:Wait()
        repeat
            task.wait()
        until returnHRP() and returnHUM()
        spoofHRP()
        spoofHUM()
    else
        spoofHRP()
    end
    returnHRP().CFrame = CFrame
    return true
end

-- Função para encontrar e armazenar frutas
local AutoCollectEnabled = false
local function findAndStoreFruits()
    while AutoCollectEnabled do
        local Fruit_InServer = false
        local Fruits_InServer = {}
        local Fruit_InHand = nil

        for _, v in ipairs(workspace:GetChildren()) do
            if v:IsA("Tool") then
                Fruit_InServer = true
                table.insert(Fruits_InServer, v)
            end
        end

        if Fruit_InServer then
            for _, v in pairs(Fruits_InServer) do
                TpTo(v.Handle.CFrame)  -- Teleporta para a fruta
                task.wait(.1)
                Fruit_InHand = string.gsub(v.Name, " Fruit", "")
                Fruit_InHand = Fruit_InHand .. "-" .. Fruit_InHand
                game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer(table.unpack({[1] = "StoreFruit", [2] = Fruit_InHand, [3] = returnHRP().Parent:FindFirstChildOfClass("Tool"),}))
                task.wait(.1)
            end
        end

        task.wait(1) -- Reduz o tempo entre as verificações para 1 segundo
    end
end

-- Função para alternar a coleta automática de frutas
local function toggleAutoCollect()
    AutoCollectEnabled = not AutoCollectEnabled
    if AutoCollectEnabled then
        findAndStoreFruits()
    end
end

-- Retorna as funções para serem usadas pelo script principal
return {
    TpTo = TpTo,
    toggleAutoCollect = toggleAutoCollect
}
