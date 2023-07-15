# Onigiri App

The Onigiri App is a dockerized Python application. This README guides you on how to use the provided bash script to interact with the application's build system.

## Prerequisites

Ensure that you have Docker, Poetry, and pytest installed in your local system. You also need a Unix-like command-line interface to run the bash script.

## Bash Script

The bash script `invoke.sh` is the entry point for managing the Onigiri App. It provides various commands to build, run, test and redeploy the application.

### Usage

Use the following syntax to run the bash script:

```
sh invoke.sh [help|run|build|redeploy|test_unit|test_integration]
```

The available commands are:

- `help`: Print a help message with information about the available commands.
- `run`: Brings up the Docker container from the latest image.
- `build`: Builds the Docker image.
- `redeploy`: Rebuilds and redeploys the Docker container.
- `test_unit`: Run unit tests.
- `test_integration`: Run integration tests.

For example, to build the Docker image, use the following command:

```
sh invoke.sh build
```

### Commands

#### `build`

This command builds a Docker image of the application. The image is tagged as `onigiri-app:latest`.

#### `run`

This command runs the application in a Docker container. The container is named `onigiri_app` and it exposes the application on port `8000`.

#### `redeploy`

This command rebuilds the Docker image of the application and redeploys it in a new Docker container. 

#### `test_unit`

This command runs the unit tests of the application. It uses pytest to execute the tests located in the `tests/unit` directory.

#### `test_integration`

This command runs the integration tests of the application. It uses pytest to execute the tests located in the `tests/integration` directory.

#### `help`

This command prints a help message with information about the available commands.

For any command not listed above, the script will print an error message and the help message, then exit with status code 1.