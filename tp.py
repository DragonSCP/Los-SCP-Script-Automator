local function returnHRP()
    if not LocalPlayer.Character then
        return
    end
    if not LocalPlayer.Character:FindFirstChild("HumanoidRootPart") then
        return
    else
        return LocalPlayer.Character:FindFirstChild("HumanoidRootPart")
    end
end

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
                returnHRP().CFrame = v.Handle.CFrame
                task.wait(.1)
                Fruit_InHand = string.gsub(v.Name, " Fruit", "")
                Fruit_InHand = Fruit_InHand .. "-" .. Fruit_InHand
                game:GetService("ReplicatedStorage").Remotes.CommF_:InvokeServer(table.unpack({[1] = "StoreFruit", [2] = Fruit_InHand, [3] = returnHRP().Parent:FindFirstChildOfClass("Tool"),}))
                task.wait(.1)
            end
        end

        task.wait(1) -- Reduce the wait time between checks to 1 second
    end
end

local function toggleAutoCollect()
    AutoCollectEnabled = not AutoCollectEnabled
    if AutoCollectEnabled then
        findAndStoreFruits()
    end
end

-- Start the auto collect function
toggleAutoCollect()
