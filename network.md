### Container to outside internet
- works automatically


### Container to Host Machine
- e.g db running on localhost

- change localhost to host.docker.internal


mongoose.connect('mongodb://localhost:27017') --> mongoose.connect('mongodb://host.internal.docker:27017')


### Container to container

- create a network
    docker network create network_name
- Run the containers in the same network
    docker run --network network_name

- use the container name inside the code to connect to the other container
