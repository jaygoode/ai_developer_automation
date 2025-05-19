@echo off
if "%~1"=="" (
    echo Usage: %0 "commit message"
    exit /b 1
)

git add .
git commit -m "%*"
git push

echo Done!
pause