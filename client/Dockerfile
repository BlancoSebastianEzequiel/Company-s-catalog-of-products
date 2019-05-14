FROM node:8.4.0
ADD . /usr/src/app
WORKDIR /usr/src/app
# install and cache app dependencies
COPY package.json /usr/src/app/package.json
RUN rm -rf node_modules
RUN  npm i
CMD ["npm", "start"]