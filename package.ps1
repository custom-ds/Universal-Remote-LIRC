

# List out all of the *.py files in the GUI directory for the user to see
Write-Host "Available Python scripts in the GUI directory:" -ForegroundColor Cyan
Get-ChildItem "GUI" -Filter "*.py" | ForEach-Object { Write-Host $_.Name }
Write-Host ""

# Prompt the user for the python script to package up
$script_name = Read-Host "Enter the name of the Python script to package (without .py extension)"

# Check to see if that script exists, and if not, exit the script
if (-not (Test-Path "GUI\$script_name.py")) {
    Write-Host "The script $script_name.py does not exist. Exiting." -ForegroundColor Red
    exit 1
}

# Remove any existing package directory to start fresh
if (Test-Path "package") {
    Remove-Item -Recurse -Force "package"
}

# Create the package directory if it doesn't exist
if (-not (Test-Path "package")) {
    New-Item -ItemType Directory -Path "package" | Out-Null
}

# Copy the specified Python script into the package directory
Copy-Item "GUI\$script_name.py" -Destination "package\remote.py" -Force
Copy-Item "GUI\requirements.txt" -Destination "package\requirements.txt" -Force

# Zip up the asset files into a single archive for distribution
if (Test-Path "GUI\assets") {
    Compress-Archive -Path "GUI\assets" -DestinationPath "package\assets.zip" -Force
}

# Zip up the lircd config files into a single archive for distribution
if (Test-Path "Pi Configs\lircd.conf.d") {
    Compress-Archive -Path "Pi Configs\lircd.conf.d\*" -DestinationPath "package\lircd.zip" -Force
}

# Copy the install.sh into the distribution folder
if (Test-Path ".\GUI\install.sh") {
    Copy-Item "GUI\install.sh" -Destination "package\" -Force
}

# Copy the remote.service into the distribution folder
if (Test-Path ".\GUI\remote.service") {
    Copy-Item "GUI\remote.service" -Destination "package\" -Force
}

# Zip up everything inside of the package folder into a single distribution archive
Compress-Archive -Path "package\*" -DestinationPath "package\package.zip" -Force

# Delete everything else from the package folder besides the final distribution archive
Get-ChildItem "package" | Where-Object { $_.Name -ne "package.zip" } | Remove-Item -Recurse -Force

Write-Host "Package created successfully!" -ForegroundColor Green

