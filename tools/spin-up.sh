#!/usr/bin/env bash

function barrier() {
  printf '=%.0s' $(seq 1 $(tput cols))
  echo
}

function center_text() {
  local text="$1"
  printf '%*s%s\n' $(( ($(tput cols) - ${#text}) / 2)) '' "$text"
}

function header() {
  local main_text="$1"
  local subtitle="$2"

  echo
  barrier

  center_text "$main_text"
  if [ -n "$subtitle" ]; then
    center_text "$subtitle"
  fi

  barrier
  echo
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

header "DOCKER COMPOSE UP"
docker compose up -d --build
error_handling "ISSUE WITH \`docker compose up -d --build\`"

header "INIT DATABASE"
docker exec -i nexus-pg-1 /bin/sh < db/init.sh
error_handling "ISSUE CREATING TABLES IN DATABASE"

header "SUCCESSFUL INIT"
