### Container to outside internet
- works automatically


### Container to Host Machine
- e.g db running on localhost

- change localhost to host.docker.internal


mongoose.connect('mongodb://localhost:27017') --> mongoose.connect('mongodb://host.internal.docker:27017')

