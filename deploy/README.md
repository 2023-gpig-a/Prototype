# Project Deployment

This folder contains all the files that wrap code into docker containers and deploy them together, alongside [Kafka](https://kafka.apache.org/) and [Postgres](https://www.postgresql.org/).

**This is not production safe.**

## Usage

### Running

To run the project in full, use `docker-compose up -d`.

### Database Management

The database files are stored in a persistent [Docker volume](https://docs.docker.com/storage/volumes/) called `dbfiles`.

### Adding a Microservice

<!-- TODO: provide template dockerfile -->
1. Create a build file (called `Dockerfile`) for the microservice in the root of it's codebase.
  See the [Dockerfile reference](https://docs.docker.com/engine/reference/builder/) for more info and directive definitions.
 <!-- TODO: expand me -->
2. Add the microservice into the `docker-compose.yml` file's `services:` section:
```yaml
services:
# other services...
  microservicename:
    # the relative path (in this repo!) of the microservice's codebase - the folder with the Dockerfile in it
    build: relative/path/to/code
    # we're building from source so instead of pulling this image, it'll name the built one like that for convenience
    image: gpig-2023-a/microservicename
```
<!-- TODO: persistent env vars passed between containers -->
3. If the microservice needs database access, it's preferred to pass the credentials to it as environment variables rather than hardcoding them.
  Make sure your microservice reads these credentials from it's environment.
  Insert an `env` key into your new service definition:
```yaml
  microservicename:
    # other config...
    env:
      DB_USER: "gpig"
      DB_PASSWORD: "heresapassword"
```
4. Add any other microservice-specific parts to the file
5. Optionally, run `docker-compose up -d` to update the running configuration to use the new service

> See the [Docker-Compose documentation](https://docs.docker.com/compose/) for more.
