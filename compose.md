### Docker Compose

docker compose 
    up = start services
        -d = start in detached mode
        --build = force build a new image

    down = stop services, remove networks
        -v = remove volumes
    
    build = build images without starting containers

    exec = run command in running containers started by docker-compose

    run = run a single command on a service
        -d = detach
        -i = interactive
        -p = ports
        -e = env
        --rm = remove on stop
        --name = assign a name
        docker-compose run [options] servicename [ARGS / Commands]


### Docker compose yaml options

#### Specify an image to be built

image: ngin:stable

build:
    context: local_path
    # context sets the folder where the dockerfile is present and also where the container is built
    # references to any folder outside the context will have to be specified accordingly
    dockerfile: name_of_dockerfile



