FROM image_name

ENV key=value

RUN command

USER username

RUN mkdir /home/node/code --> create and owns the dir

WORKDIR /home/node/code --> will create if doesnt exist (but owned by root) 

RUN npm ci --> instead of install, uses package-lock.json

COPY --chown=user:group source_host container_dest

ADD --chown=user:group source_host container_dest
add can do additionally
    - retrieve a file from the network / internet
    - unzip files 

CMD ["node", "server.js"] = entrypoint command

### Instructions


FROM = base image name

WORKDIR = set the working directory in the container
    WORKDIR container_dir


COPY = copy the files/folders
    src = source
    dst = destination
    COPY src dst

RUN = runs command in containers working dir
        is executed wheever the image is buing built

EXPOSE 80 = expose port 80 in the image, use with -P flag while ducker run to choose a randon port on the localhost to bind to
    docker run --it -P 
        -P exposes all the ports mentioned in the dockerfile to random local ports

CMD = command is run when the container is started
    CMD ['node', 'server.js']

ENTRYPOINT = sets the context for commands run during docker run
    ENTRYPOINT ["npm"]
        - allows to append any npm command during docker run
        - protects from running any other commands in the container shell 
        docker run -it -v local_path:cont_path imagename init --> instead of npm init


VOLUME [ "/path/inside/container" ] = Anonymous volume
the code needs to support files being written on a different file system

volumes - managed by docker
    anonymous = exists as long as container is running
    named
bind mounts - managed by you


ENV PORT 80 = Set the default value in the dockerfile, for building the image

EXPOSE $PORT = use the variable in the same dockerfile

process.env.PORT = inside code

-p 3000:8000 --env PORT=8000 = set during docker run 
-e = same as --env

--env-file ./.env = point to an env file in the current folder
