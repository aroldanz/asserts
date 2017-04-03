#!/bin/bash

# Salir inmediatamente si algun comando retorna diferente de cero.
set -e

# Mensaje de inicio
echo "---### Compilando contenedor."

# construir la imagen
docker build -t fluidsignal/fluidasserts-dev:debian .