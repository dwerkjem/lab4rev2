#!/usr/bin/env bash

set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

CONFIG_FILE="$PROJECT_ROOT/conf/otelcol-config.yaml"
CONTAINER_CONFIG_PATH="/otel-lgtm/otelcol-config.yaml"

LOG_DIR="$PROJECT_ROOT/logs"
CONTAINER_LOG_DIR="/project-logs"

CONTAINER_NAME="otel-lgtm"

if [[ ! -f "$CONFIG_FILE" ]]; then
    echo "Error: expected config file at $CONFIG_FILE" >&2
    exit 1
fi

mkdir -p "$LOG_DIR"

docker rm -f "$CONTAINER_NAME" >/dev/null 2>&1 || true

docker run \
    -d \
    --name "$CONTAINER_NAME" \
    --add-host=host.docker.internal:host-gateway \
    -p 3000:3000 \
    -p 4317:4317 \
    -p 4318:4318 \
    -v "$CONFIG_FILE:${CONTAINER_CONFIG_PATH}:ro" \
    -v "$LOG_DIR:${CONTAINER_LOG_DIR}:ro" \
    --rm \
    grafana/otel-lgtm