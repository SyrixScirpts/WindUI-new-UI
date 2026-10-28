with open('C:/Users/luay1/Downloads/WindUI-main/dist/main.lua', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('Background=Color3.fromHex("#101010")', 'Background=Color3.fromHex("#000000")')
content = content.replace('Accent=Color3.fromHex("#18181b")', 'Accent=Color3.fromHex("#4B0082")')
content = content.replace('Dialog=Color3.fromHex("#1a1a1a")', 'Dialog=Color3.fromHex("#0a0014")')
content = content.replace('ElementBackground=Color3.fromHex("#2A2A2C")', 'ElementBackground=Color3.fromHex("#1a0b2e")')
content = content.replace('Button=Color3.fromHex("#52525b")', 'Button=Color3.fromHex("#6b46c1")')
content = content.replace('Icon=Color3.fromHex("#a1a1aa")', 'Icon=Color3.fromHex("#ffffff")')
content = content.replace('Placeholder=Color3.fromHex("#a1a1a1")', 'Placeholder=Color3.fromHex("#a78bfa")')
content = content.replace('Outline=Color3.fromHex("#FFFFFF")', 'Outline=Color3.fromHex("#8a2be2")')
content = content.replace('PanelBackground=Color3.fromHex("#FFFFFF")', 'PanelBackground=Color3.fromHex("#0a0014")')
content = content.replace('Primary=Color3.fromHex("#0091FF")', 'Primary=Color3.fromHex("#8b5cf6")')
content = content.replace('Slider=Color3.fromHex("#0091FF")', 'Slider=Color3.fromHex("#8b5cf6")')
content = content.replace('Checkbox=Color3.fromHex("#0091FF")', 'Checkbox=Color3.fromHex("#8b5cf6")')

with open('C:/Users/luay1/Downloads/WindUI-main/dist/main.lua', 'w', encoding='utf-8') as f:
    f.write(content)

print('done')
