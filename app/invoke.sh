#!/usr/bin/env bash

set -euo pipefail

source .openai_credentials.env
export PYTHONPATH="$(pwd)"

# Reference: https://opensource.com/article/19/12/help-bash-program
Help()
{
    echo "Helps interact with the app build system."
    echo
    echo "Syntax: sh invoke.sh [help|run|build|redeploy|down|test_unit|test_integration]"
    echo "options:"
    echo "help               Print this help."
    echo "run                Brings up the docker container from latest image."
    echo "build              Builds the docker image."
    echo "redeploy           Rebuilds and redeploys the docker container."
    echo "down               Stops the docker container."
    echo "test_unit          Run unit tests."
    echo "test_integration   Run integration tests."
    echo
}

case ${1:-} in
    "test_unit")
        echo "Running unit tests..."
        poetry run pytest tests/unit
        ;;
    
    "test_integration")
        echo "Running integration tests..."
        poetry run pytest tests/integration
        echo "If tests fail to run, make sure the app is running with 'sh invoke.sh run'"
        ;;

    "build")
        echo "Building..."
        docker build -t onigiri-app:latest .
        ;;

    "run")
        echo "Running docker container..."
        docker run -d --rm --name onigiri_app -p 8000:8000 onigiri-app:latest
        ;;
    
    "redeploy")
        echo "Stop, re-build and redeploying container..."
        docker stop onigiri_app || true
        docker build -t onigiri-app:latest .
        docker run -d --rm --name onigiri_app -p 8000:8000 onigiri-app:latest
        ;;
    
    "down")
        echo "Stopping container..."
        docker stop onigiri_app
        ;;

    "help")
        Help
        ;;
    
    *)
        echo "Unknown command: $1"
        Help
        exit 1
        ;;
esac
    