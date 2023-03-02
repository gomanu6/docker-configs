FROM image_name

ENV key=value

RUN command

COPY source_host container_dest

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

EXPOSE 80 = expose port 80 in the image

CMD = command is run when the container is started
    CMD ['node', 'server.js']


VOLUME [ "/path/inside/container" ] = Anonymous volume
the code needs to support files being written on a different file system

volumes - managed by docker
    anonymous = exists as long as container is running
    named
bind mounts - managed by you


