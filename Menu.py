-- GUI Creation
local ScreenGui = Instance.new("ScreenGui")
local Frame = Instance.new("Frame")
local AutoCollectButton = Instance.new("TextButton")
local ExitButton = Instance.new("TextButton")
local ScriptName = Instance.new("TextLabel")
local MinimizeButton = Instance.new("TextButton")
local FloatingButton = Instance.new("TextButton")
local Minimized = false

ScreenGui.Parent = game.CoreGui

Frame.Parent = ScreenGui
Frame.BackgroundColor3 = Color3.fromRGB(0, 0, 0)
Frame.Position = UDim2.new(0.5, -150, 0.5, -200)
Frame.Size = UDim2.new(0, 300, 0, 200)
Frame.BackgroundTransparency = 0.5
Frame.BorderSizePixel = 0

AutoCollectButton.Parent = Frame
AutoCollectButton.BackgroundColor3 = Color3.fromRGB(0, 0, 0)
AutoCollectButton.Size = UDim2.new(1, 0, 0.3, 0)
AutoCollectButton.Position = UDim2.new(0, 0, 0, 0)
AutoCollectButton.Font = Enum.Font.SourceSans
AutoCollectButton.Text = "Toggle Auto Collect"
AutoCollectButton.TextColor3 = Color3.fromRGB(255, 255, 255)
AutoCollectButton.TextSize = 14

ExitButton.Parent = Frame
ExitButton.BackgroundColor3 = Color3.fromRGB(0, 0, 0)
ExitButton.Size = UDim2.new(1, 0, 0.3, 0)
ExitButton.Position = UDim2.new(0, 0, 0.3, 0)
ExitButton.Font = Enum.Font.SourceSans
ExitButton.Text = "Sair do Mapa"
ExitButton.TextColor3 = Color3.fromRGB(255, 255, 255)
ExitButton.TextSize = 14

ScriptName.Parent = Frame
ScriptName.BackgroundColor3 = Color3.fromRGB(0, 0, 0)
ScriptName.Size = UDim2.new(1, 0, 0.2, 0)
ScriptName.Position = UDim2.new(0, 0, 0.9, 0)
ScriptName.Font = Enum.Font.SourceSans
ScriptName.Text = "Dragon Script - Fruit Hunter"
ScriptName.TextColor3 = Color3.fromRGB(255, 255, 255)
ScriptName.TextSize = 14

MinimizeButton.Parent = Frame
MinimizeButton.BackgroundColor3 = Color3.fromRGB(255, 0, 0)
MinimizeButton.Size = UDim2.new(0.1, 0, 0.1, 0)
MinimizeButton.Position = UDim2.new(0.9, 0, 0, 0)
MinimizeButton.Font = Enum.Font.SourceSans
MinimizeButton.Text = "-"
MinimizeButton.TextColor3 = Color3.fromRGB(255, 255, 255)
MinimizeButton.TextSize = 14

FloatingButton.Parent = ScreenGui
FloatingButton.BackgroundColor3 = Color3.fromRGB(0, 0, 0)
FloatingButton.Size = UDim2.new(0, 50, 0, 50)
FloatingButton.Position = UDim2.new(0.9, 0, 0.9, 0)
FloatingButton.Font = Enum.Font.SourceSans
FloatingButton.Text = "DragonSCP"
FloatingButton.TextColor3 = Color3.fromRGB(255, 255, 255)
FloatingButton.TextSize = 12
FloatingButton.Visible = true

MinimizeButton.MouseButton1Click:Connect(function()
    if Minimized then
        Frame.Visible = true
        FloatingButton.Visible = false
        MinimizeButton.Text = "-"
    else
        Frame.Visible = false
        FloatingButton.Visible = true
        MinimizeButton.Text = "+"
    end
    Minimized = not Minimized
end)

FloatingButton.MouseButton1Click:Connect(function()
    Frame.Visible = true
    FloatingButton.Visible = false
    Minimized = false
    MinimizeButton.Text = "-"
end)

AutoCollectButton.MouseButton1Click:Connect(toggleAutoCollect)
ExitButton.MouseButton1Click:Connect(function()
    local module = loadstring(game:HttpGet("https://raw.githubusercontent.com/DragonSCP/Los-SCP-Script-Automator/main/lk_serverhop.lua"))()
    module:Teleport(game.PlaceId)
end)

-- Be nice and leave the credits in!
for i = 1, 100 do
    print("Dragon Script - Fruit Hunter by DragonSCP\nMore scripts here: extorius.ezyro.com\nBe nice and leave the credits in")
end
