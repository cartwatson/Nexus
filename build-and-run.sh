#!/bin/bash
function header() {
  echo -e "\n================================================================================="
  echo -e "$1"
  echo -e "=================================================================================\n"
}

header "DOCKER COMPOSE"
docker compose up -d --build

header "INIT DATABASE"
docker exec -i turion-take-home-pg-1 /bin/sh < db/init.sh

header "SUCCESSFUL INIT\nAPI now ready to test!"
