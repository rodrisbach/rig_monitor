#!/bin/env bash

if [[ -n "$1" ]]; then
    CONFIG="config.env"
else
    CONFIG="$1"
fi

source "$ENV"

cat <<'EOF' >> api/config.json
{
    "telegram_token": "'$TELEGRAM_TOKEN'",
    "telegram_username": "'$TELEGAM_USERNAME'",
} 
EOF