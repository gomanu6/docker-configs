### Utility Containers

#### Docker exec


docker exec container_name command = run command inside container
    -it = interactive mode
    -d = detached 

docker run -it node npm init = overites the default command (as specified in the node image) and runs npm init


#### Use Bind Mounts to share a folder with a container and run commands inside container to create package.json

##### Create Node Image

FROM node:14-alpine

WORKDIR /app

docker build -t nutil 

##### Run container and execute command inside container

docker run it -v local_path:cont_path nutil npm init
