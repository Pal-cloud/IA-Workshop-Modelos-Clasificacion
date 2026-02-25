#!/bin/bash

echo "========================================"
echo " Iniciando Aplicación Web"
echo " Tarea de Investigación - ML"
echo "========================================"
echo ""

echo "Verificando dependencias..."
if ! python3 -c "import flask" 2>/dev/null; then
    echo "[!] Flask no está instalado"
    echo "[+] Instalando dependencias..."
    pip3 install -r requirements.txt
fi

echo ""
echo "[OK] Dependencias verificadas"
echo ""

echo "========================================"
echo " Servidor iniciando..."
echo " Abre tu navegador en: http://localhost:5000"
echo "========================================"
echo ""

python3 app.py
