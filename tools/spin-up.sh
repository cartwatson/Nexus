#!/usr/bin/env bash

source "$(dirname "$0")/shared.sh"

main_header

header "DOCKER COMPOSE UP"
docker compose up -d --build
error_handling "ISSUE WITH \`docker compose up -d --build\`"

header "INIT DATABASE"
docker exec -i nexus-pg-1 /bin/sh < db/init.sh
error_handling "ISSUE CREATING TABLES IN DATABASE" "SUCCESSFUL INIT"
