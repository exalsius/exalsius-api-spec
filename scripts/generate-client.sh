#!/bin/bash

set -euo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_DIR="$( cd "${SCRIPT_DIR}/.." && pwd )"
CLIENT_SDK_DIR="client-sdk"

log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1"
}

check_docker() {
    if ! command -v docker &> /dev/null; then
        echo "Error: Docker is not installed or not in PATH"
        echo "Please install Docker before running this script"
        exit 1
    fi
}


create_bundle() {
    log "Creating OpenAPI bundle..."
	docker run --init --rm \
		--user $(id -u):$(id -g) \
		-v "${REPO_DIR}:/spec" \
		redocly/cli \
		--config /spec/openapi/redocly.yaml \
		bundle /spec/openapi/openapi.yaml -o /spec/dist/bundle.yaml

}


run_generator() {
    log "Generating client SDK python code..."
    docker run --rm -v "${REPO_DIR}:/local" \
            --user $(id -u):$(id -g) \
            openapitools/openapi-generator-cli generate \
            -i local/dist/bundle.yaml \
            --package-name "exalsius_api_client" \
            -g python \
            -o /local/${CLIENT_SDK_DIR}
}

run_formatter() {
    log "Formatting client SDK python code..."
    docker run --rm -v "${REPO_DIR}:/src" \
            --user $(id -u):$(id -g) \
        --workdir /src/${CLIENT_SDK_DIR} pyfound/black:latest_release black .
}

cleanup() {
    local exit_code=$?
    if [ $exit_code -ne 0 ]; then
        log "Script failed with exit code $exit_code"
    fi
    exit $exit_code
}

trap cleanup EXIT
log "Starting client SDK generation..."
check_docker
create_bundle
run_generator
run_formatter
log "Client SDK generation completed"