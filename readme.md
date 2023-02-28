## Docker

### Commands
images = lists images available locally
pull = pull image
run = pulls the image and runs container
    -plocalport:containerport = binds local port to container port
    -d = detached mode / daemon
    --name = names the container

ps = list running images
    -a = list all containers
start = start container
stop = stop container
logs = shows the container logs
exec = execute command inside container
    -it = interactive mode
    docker exec -it container_name command

