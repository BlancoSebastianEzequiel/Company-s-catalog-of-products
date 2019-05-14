FROM node:8.4.0
ADD . /usr/src/app
WORKDIR /usr/src/app
RUN pip install --upgrade pip
WORKDIR /usr/src/app/client
RUN rm -rf node_modules
WORKDIR /usr/src/app
RUN sh scripts/install.sh
ENTRYPOINT ["npm","run", "server"]