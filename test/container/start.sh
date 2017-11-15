#!/bin/bash

# habilitar depuración
if [ -n "$VERBOSE" ]; then
  set -x
fi

# Salir inmediatamente si algun comando retorna diferente de cero.
set -e

# importar entorno
source $(git rev-parse --show-toplevel)/test/env.sh

# Mensaje de inicio
echo "---### Iniciando contenedor."

# crear red de contenedores si no ha iniciado
if [ -z $(docker network ls -q -f name="$NET_NAME") ]; then
  echo "Red de contenedores no establecida, creando red..."
  docker network create \
        --subnet="$NET_IP" \
        "$NET_NAME"
else
  echo "Red ya configurada, reutilizando red..."
fi

# iniciar contenedor si no ha iniciado
if [ -z $(docker ps -q -f name="$SERVICE") ]; then
  echo "Contenedor no ha iniciado, iniciando contenedor..."

  # Crear dinamicamente claves de acceso al contenedor
  # La ruta de configuración SSH tambien esta parametrizado en test/setup/hosts
  mkdir -p ~/.ssh/
  cp "$PROJECT_DIR"/test/provision/ssh_config "$PROJECT_DIR"/build/config.facont
  echo -e "y\n" | ssh-keygen -b 2048 -t rsa -f "$PROJECT_DIR"/build/facont_id_rsa -q -N ""

  docker run \
        --detach \
        --name="$SERVICE" \
        --hostname="$SERVICE" \
        --net "$NET_NAME" \
        --ip "$IP" \
        --publish-all \
        --volume=/tmp:/host/tmp \
        --volume=/var/run/docker.sock:/var/run/docker.sock \
        -e SSH_KEY="$(cat $PROJECT_DIR/build/facont_id_rsa.pub)" \
        fluidsignal/fluidasserts:"$SERVICE"

  echo "Esperando que el puerto 22 de SSH este abierto."
  until nc -z $IP 22; do : sleep 0.2; done
  echo "Puerto SSH (22) abierto en contenedor."
else
  echo "Contenedor ya inicio, reutilizando contenedor."
fi
