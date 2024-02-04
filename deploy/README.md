# Project Deployment

This folder contains all the files that wrap code into docker containers and deploy them together, alongside [Kafka](https://kafka.apache.org/) and [Postgres](https://www.postgresql.org/).

## Usage

### Running

To run the project in full, use `docker-compose up -d`.

### Adding a Microservice

<!-- TODO: provide template dockerfile -->
1. Create a build file (called `Dockerfile`) for the microservice in the root of it's codebase.
   See the [Dockerfile reference](https://docs.docker.com/engine/reference/builder/) for more info and directive definitions.
2. Add the microservice into the `docker-compose.yml` file's `services:` section: <!-- TODO: expand me -->
```yaml
services:
# other services...
  microservicename:
    # the relative path (in this repo!) of the microservice's codebase - the folder with the Dockerfile in it
    build: relative/path/to/code
    # we're building from source so instead of pulling this image, it'll name the built one like that for convenience
    image: gpig-2023-a/microservicename
```
3. Add any other microservice-specific parts to the file
4. Optionally, run `docker-compose up -d` to update the running configuration to use the new service

> See the [Docker-Compose documentation](https://docs.docker.com/compose/) for more.
