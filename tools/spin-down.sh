#!/usr/bin/env bash

function header() {
  echo
  # print = across whole terminal
  printf '=%.0s' $(seq 1 $(tput cols)); echo
  # center header
  printf '%*s%s\n' $(( ($(tput cols) - ${#1}) / 2)) '' "$1"
  printf '=%.0s' $(seq 1 $(tput cols)); echo -e "\n"
}


function error_handling {
  if [ $? -eq 0 ]; then
    if [ -n "$2" ]; then
      header "$2"
    fi
  else
    header "$1"
    exit 1
  fi
}

header "DOCKER DOWN"
docker compose down --rmi local -v

error_handling "ERROR TERMINATING NEXUS IN DOCKER" "SUCCESSFULLY TERMINATED NEXUS"
