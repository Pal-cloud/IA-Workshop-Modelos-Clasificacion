@echo off
echo ========================================
echo  Iniciando Aplicacion Web
echo  Tarea de Investigacion - ML
echo ========================================
echo.
echo Verificando dependencias...
python -c "import flask" 2>nul
if errorlevel 1 (
    echo [!] Flask no esta instalado
    echo [+] Instalando dependencias...
    pip install -r requirements.txt
)
echo.
echo [OK] Dependencias verificadas
echo.
echo ========================================
echo  Servidor iniciando...
echo  Abre tu navegador en: http://localhost:5000
echo ========================================
echo.
python app.py
pause
