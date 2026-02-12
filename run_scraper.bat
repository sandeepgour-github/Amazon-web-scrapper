@echo off
echo ========================================
echo   AMAZON SCRAPER - Quick Start
echo ========================================
echo.
echo Choose option:
echo.
echo [1] Amazon India Simple (RECOMMENDED - Less Blocking)
echo [2] Amazon.com with Stealth
echo [3] Install Undetected ChromeDriver
echo [4] Exit
echo.
set /p choice="Enter choice (1-4): "

if "%choice%"=="1" (
    echo.
    echo Running Amazon India scraper...
    python amazon_india_simple.py
    pause
) else if "%choice%"=="2" (
    echo.
    echo Running Amazon.com scraper with stealth...
    python amazon_working.py
    pause
) else if "%choice%"=="3" (
    echo.
    echo Installing undetected-chromedriver...
    pip install undetected-chromedriver
    echo.
    echo Done! Now you can create custom scraper using undetected-chromedriver
    pause
) else (
    exit
)
