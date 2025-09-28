# Trabajo Practico N 2

Trabajo practico N°2 para la materia de <strong>Introduccion al desarrollo de software</strong>

## Integrantes
* Lukas Peneff
* Florian Luchinni
* Harold Montaño



## Configuración y Ejecución

El proyecto incluye un script para automatizar la configuración inicial. Los pasos para la instalación y ejecución son:

1.  **Preparar y ejecutar el script de configuración:**
    Este comando da permisos de ejecución y corre el script que crea la estructura de carpetas y el entorno virtual.
    ```bash
    chmod +x crear_proyecto.sh && ./crear_proyecto.sh
    ```

2.  **Activar el entorno virtual:**
    ```bash
    source .venv/bin/activate
    ```

3.  **Instalar las dependencias:**
    ```bash
    pip install Flask
    ```

4.  **Iniciar el servidor de desarrollo:**
    ```bash
    flask run
    ```