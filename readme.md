## Docker

### Commands
images = lists images available locally
pull = pull image
push = push image to repository

ps = list running images
    -a = list all containers
    -q = quiet, only display container ids
        docker ps -q

kill = kill a container
    -s = signal to send the container
        docker kill $(docker ps -q) = kills all running containers

rm = remove container
logs = shows the container logs
    -f stream the log
    docker logs container_name

exec = execute command inside an existing container
    -it = interactive mode
    docker exec -it container_name command
network
    -ls = list networks
    -create network_name = create network 
    docker network ls = list networks


login = login to docker
logout = logout of docker

volume
    -ls = list
    -create
    -inspect
    -rm
    -prune

pause container_name

unpause container_name

history = show history of container
    -H = Human readable dates, sizes
    -q = quiet
        docker history container_name

info = shows info about host docker install

top = shows info for running processes inside container
    docker top container_name

search 

### Run Command

run = pulls the image and runs a NEW container
    -p localport:containerport = binds local port to container port
        -p 3001:3000
    -d = detached mode / daemon
    -it = run cont in interactive mode and expose a tty shell
    -rm = removes the container on exit
    --name = names the container
    --network = runs in the network
        --network network_name
    --net = same as network
    -v = list volumes
        -v name:/path/inside/container
    -e variable=value = environment variables
        -e MONGO_INITDB_ROOT_USERNAME=admin
    --init = runs the container with tini>init to respond to Ctrl + C signal
    




### Docker Images

build
    -t = tag name eg myapp:1.0 (repo_name:tag)

    docker build [options] location_dockerfile

rmi = remove image

push = push to repo

tag = rename the image
    docker tag old_name:ver new_name:ver

image = manage images
    prune = delete all images without any tags
        -a = delete all images
    inspect = show details of the image
        docker image inspect image_name

docker image inspect


### Manage Running Containers
- Builds up on the image
- thin command layer on top of the images
- multiple container share data from the image

start = start a container
    -a = attached mode (not interactive)
    -i = interactive mode

stop = stop a running container

restart = restart, may not restart if the running app doesnt recognise restart and may hard restart

attach = attach to a running container
    docker container attach container_name

logs = print the past log entries
    -f = follow mode
    docker logs -f cont_name

cp = copy file to or from the container
    docker cp local_path container_name:container_path

docker container prune = deletes all stopped container

docker container inspect name


docker run -d --name mongodb --net mongo-net -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=mongoadmin -e MONGO_INITDB_ROOT_PASSWORD=secret mongo

docker run -d --name mongoexpress --net mongo-net -p 8081:8081 -e ME_CONFIG_MONGODB_ADMINUSERNAME=mongoadmin -e ME_CONFIG_MONGODB_ADMINPASSWORD=secret -e ME_CONFIG_MONGODB_SERVER=mongodb mongo-express



###  Docker Ignore

.dockerignore
- specify which files/folders not to be copied to the container


### Compose

docker-compose
    -f = file path

up = start services
down = stops containers and removes network