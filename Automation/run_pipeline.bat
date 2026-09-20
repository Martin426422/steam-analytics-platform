@echo off

REM przejdz do katalogu glownego projektu
cd /d "%~dp0.."

echo ======================
echo STEAM ANALYTICS PIPELINE
echo ======================

echo.
echo [1/3] EXTRACT
python ETL\extract_steam.py

if errorlevel 1 goto error

echo.
echo [2/3] TRANSFORM
python ETL\transform_steam.py

if errorlevel 1 goto error

echo.
echo [3/3] LOAD
python ETL\load_mssql.py

if errorlevel 1 goto error

echo.
echo ======================
echo PIPELINE COMPLETED
echo ======================
pause
exit /b 0

:error
echo.
echo ======================
echo PIPELINE FAILED
echo ======================
pause
exit /b 1