###

docker-compose 
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
