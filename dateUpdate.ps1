$driveLetter = "C:/"
$files = Get-ChildItem -Path "$driveLetter*" -File -Recurse
$currentDateTime = Get-Date

foreach ($file in $files) {
    
    Write-Host "Checking file: $($file.FullName)"

    if ($file.LastAccessTime -le $currentDateTime) {
        $file.LastAccessTime = $currentDateTime
        Write-Host "File: $($file.FullName) - OK"
    }
}
