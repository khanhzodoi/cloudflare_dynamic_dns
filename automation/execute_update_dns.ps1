# Activate the Python virtual environment
$virtualEnvPath = "F:\Labs\cloudflare_dynamic_dns\venv\Scripts\Activate.ps1"
$scriptDirectory = "F:\Labs\cloudflare_dynamic_dns"



if (Test-Path $virtualEnvPath) {
    Write-Host "Activating Python virtual environment..."
    . $virtualEnvPath
} else {
    Write-Host "Python virtual environment not found at $virtualEnvPath."
    exit 1
}

# Change to the directory containing your main.py script
Set-Location -Path $scriptDirectory

# Run the main.py script
Write-Host "Running main.py..."
python main.py