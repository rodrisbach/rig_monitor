#!/bin/env bash

if [[ -z "$1" ]]; then
    CONFIG="config.env"
else
    CONFIG="$1"
fi

source "$CONFIG"

cat <<EOF > api/config.json
{
    "telegram_token": "${TELEGRAM_TOKEN}",
    "telegram_username": "${TELEGRAM_USERNAME}",
} 
EOF
