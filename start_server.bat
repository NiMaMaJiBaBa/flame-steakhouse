@echo off
chcp 65001 >nul
title 焰牛排館 FLAME STEAKHOUSE - 本地網站啟動器
echo ========================================================
echo   正在啟動「焰牛排館 FLAME STEAKHOUSE」官方網站...
echo ========================================================
echo.
python "%~dp0server.py"
if %errorlevel% neq 0 (
    echo.
    echo 偵測到 Python 執行異常，正在以預設瀏覽器直接開啟 index.html...
    start "" "%~dp0index.html"
)
pause

