#!/usr/bin/env bash

source "$(dirname "$0")/shared.sh"

header "DOCKER DOWN"
docker compose down --rmi local -v

error_handling "ERROR TERMINATING NEXUS IN DOCKER" "SUCCESSFULLY TERMINATED NEXUS"

echo "Thanks for using..."
main_header; echo
