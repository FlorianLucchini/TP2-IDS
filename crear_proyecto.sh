#!/bin/bash

echo "Iniciando configuración del proyecto."

mkdir -p static/css
mkdir -p static/images
mkdir -p templates

if [ ! -d ".venv" ]; then
    echo "Creando ambiente virtual en .venv/"
    python3 -m venv .venv
    echo "Ambiente virtual creado."
else
    echo "La carpeta .venv ya existe"
fi


if [ ! -f "app.py" ]; then
    echo "Creando archivo app.py"
    touch app.py
else
    echo "El archivo app.py ya existe"
fi

echo "Configuración del proyecto finalizada."
