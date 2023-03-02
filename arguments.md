### Arguments (Build Time)
- available inside dockerfile
- not accessible in CMD or app code


ARG DEFAULT_PORT=80 ----> Set the default arg in docker file

ENV PORT $DEFAULT_PORT ----> use the arg in the same dockerfile

docker build --build-arg DEFAULT_PORT=8000 ----> use for building an image with a different port

### Environment Valiables
- available inside dockerfile and app code

docker run --env, docker run -e


ENV PORT 80 = Set the default value in the dockerfile, for building the image

EXPOSE $PORT = use the variable in the same dockerfile

process.env.PORT = inside code

-p 3000:8000 --env PORT=8000 = set during docker run 
-e = same as --env

--env-file ./.env = point to an env file in the current folder