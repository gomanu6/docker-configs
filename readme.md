## Docker

### Commands
images = lists images available locally
pull = pull image
run = pulls the image and runs container
    -p localport:containerport = binds local port to container port
        -p 3001:3000
    -d = detached mode / daemon
    --name = names the container
    --network = runs in the network
    --net = same as network
    -e variable=value = environment variables
        -e MONGO_INITDB_ROOT_USERNAME=admin

ps = list running images
    -a = list all containers
start = start container
stop = stop container
logs = shows the container logs
    -f stream the log
exec = execute command inside container
    -it = interactive mode
    docker exec -it container_name command
network
    -ls = list networks
    -create network_name = create network 
docker network ls = list networks


docker run -d --name mongodb --net mongo-net -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=mongoadmin -e MONGO_INITDB_ROOT_PASSWORD=secret mongo

docker run -d --name mongoexpress --net mongo-net -p 8081:8081 -e ME_CONFIG_MONGODB_ADMINUSERNAME=mongoadmin -e ME_CONFIG_MONGODB_ADMINPASSWORD=secret -e ME_CONFIG_MONGODB_SERVER=mongodb mongo-express


### Compose