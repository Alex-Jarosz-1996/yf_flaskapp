@echo off
setlocal enabledelayedexpansion

rem Check if Python is installed
set "python_cmd=python"
set "python_version="
for /f "tokens=*" %%i in ('%python_cmd% -c "import sys; print(sys.version[:3])" 2^>nul') do set "python_version=%%i"

if not "%python_version%"=="" (
    echo Python %python_version% is installed.
    
    rem Execute your Python script
    %python_cmd% app.py

    rem Launch a web browser
    start http://127.0.0.1:5000
) else (
    echo Python is not installed. Please install Python and try again.
)

endlocal
