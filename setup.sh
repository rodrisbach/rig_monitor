#!/bin/env bash

if [[ -z "$1" ]]; then
    CONFIG="config.env"
else
    CONFIG="$1"
fi

source "$CONFIG"

DEVICE_METRICS_TABLE=${DEVICE_METRICS_TABLE:-"device_metrics"}
POOL_METRICS_TABLE${POOL_METRICS_TABLE:-"pool_metrics"}
cat <<EOF > api/config.json
{
    "telegram_token": "${TELEGRAM_TOKEN}",
    "telegram_username": "${TELEGRAM_USERNAME}",
} 
EOF

cat <<EOF > scheduler/config.json
{
    "rig_url": "${RIG_URL}",
    "rig_password": "${RIG_PASSWORD}",
    "min_hashrate": "${MIN_HASHRATE}",
    "wallet_address": "${WALLET_ADDRESS}",
    "coin": "${COIN}",
    "flexpool_api": "${FLEXPOOL_API}",
    "log_path": "${LOG_PATH}",
    "db_user": "${MYSQL_USER}",
    "db_passwoord": "${MYSQL_PASSWORD}",
    "db_host": "${}",
    "db_name": "${MYSQL_DATABASE}"
    "device_metrics_table": "${DEVICE_METRICS_TABLE}",
    "pool_metrics_table": "${POOL_METRICS_TABLE}"
}
EOF