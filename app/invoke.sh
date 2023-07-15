#!/usr/bin/env bash

set -euo pipefail
export PYTHONPATH="$(pwd)"

# Reference: https://opensource.com/article/19/12/help-bash-program
Help()
{
   echo "Helps interact with the app build system."
   echo
   echo "Syntax: sh invoke.sh [help|run|build|redeploy|test_unit|test_integration]"
   echo "options:"
   echo "help               Print this help."
   echo "run                Brings up the docker container from latest image."
   echo "build              Builds the docker image."
   echo "redeploy           Rebuilds and redeploys the docker container."
   echo "test_unit          Run unit tests."
   echo "test_integration   Run integration tests."
   echo
}

case ${1:-} in
    "build")
        echo "Building..."
        docker build -t onigiri-app:latest .
        ;;
    
    "test_unit")
        echo "Running unit tests..."
        poetry run pytest tests/unit
        ;;
    
    "test_integration")
        echo "Running integration tests..."
        poetry run pytest tests/integration
        echo "If tests fail, make sure the app is running with 'sh invoke.sh run'"
        ;;

    "run")
        echo "Running docker container..."
        docker run --rm --name onigiri_app -p 8000:8000 onigiri-app:latest
        ;;
    
    "redeploy")
        echo "Rebuilds and redeploys container..."
        docker build -t onigiri-app:latest .
        docker run --rm --name onigiri_app -p 8000:8000 onigiri-app:latest
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