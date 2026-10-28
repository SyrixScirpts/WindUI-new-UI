with open('C:/Users/luay1/Downloads/WindUI-main/dist/main.lua', 'r', encoding='utf-8') as f:
    content = f.read()

# Add galaxy particles to dist
particles_code = '''local GalaxyBackground = New("Frame", {
	Size = UDim2.new(1, 0, 1, 0),
	BackgroundColor3 = Color3.fromRGB(10, 0, 20),
	BackgroundTransparency = 0,
	ZIndex = -11,
	ClipsDescendants = true,
	Visible = true,
}, {
	New("UIGradient", {
		Color = ColorSequence.new({
			ColorSequenceKeypoint.new(0, Color3.fromRGB(5, 0, 15)),
			ColorSequenceKeypoint.new(0.5, Color3.fromRGB(20, 0, 40)),
			ColorSequenceKeypoint.new(1, Color3.fromRGB(0, 0, 0)),
		}),
		Rotation = 90,
	}),
	New("UICorner", {
		CornerRadius = UDim.new(0, Window.UICorner),
	}),
})

task.spawn(function()
	for i = 1, 100 do
		task.wait(0.01)
		local particle = New("Frame", {
			Size = UDim2.new(0, math.random(1, 2), 0, math.random(1, 2)),
			Position = UDim2.new(math.random(), 0, math.random(), 0),
			BackgroundColor3 = Color3.fromRGB(255, 255, 255),
			BackgroundTransparency = math.random(10, 40) / 100,
			AnchorPoint = Vector2.new(0.5, 0.5),
			ZIndex = -10,
			Parent = GalaxyBackground,
		}, {
			New("UICorner", {
				CornerRadius = UDim.new(1, 0),
			}),
		})
		
		task.spawn(function()
			while particle.Parent do
				local tweenInfo = TweenInfo.new(math.random(20, 40), Enum.EasingStyle.Linear, Enum.EasingDirection.InOut)
				local goal = {Position = UDim2.new(math.random(), 0, math.random(), 0)}
				local tween = game:GetService("TweenService"):Create(particle, tweenInfo, goal)
				tween:Play()
				tween.Completed:Wait()
			end
		end)
	end
end)
'''

# Try to find a place to insert - look for where BGImage is defined in window creation
# Just append before bottom drag frame creation
old = '''local BottomDragFrame = Creator.NewRoundFrame(99, "Squircle", {'''
if old in content and 'GalaxyBackground' not in content:
    content = content.replace(old, particles_code + '\n\n\t' + old)
    print('added')
else:
    print('skip or exists')

with open('C:/Users/luay1/Downloads/WindUI-main/dist/main.lua', 'w', encoding='utf-8') as f:
    f.write(content)
