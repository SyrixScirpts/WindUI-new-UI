$c = [System.IO.File]::ReadAllText('C:\Users\luay1\Downloads\WindUI-main\dist\main.lua')
$matches = [regex]::Matches($c, 'GalaxyBackground')
Write-Output $matches.Count
