@echo off

@REM %python_version%=''
for /f "tokens=*" %%i in ('py -3 -c "import sys; print('.'.join(map(str, sys.version_info[:2])))"') do set "python_version=%%i"
echo Python version %python_version% is installed.

py -%python_version% "app.py"
start http://127.0.0.1:5000
