FROM python

WORKDIR /app

COPY . /app/

ARG DEFAULTPORT=8002
ENV PORT ${DEFAULTPORT}

RUN export PORT=${PORT}
EXPOSE ${PORT}

CMD [ "python", "srv.py" ]