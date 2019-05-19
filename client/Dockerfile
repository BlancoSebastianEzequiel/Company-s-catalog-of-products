FROM node:8.4.0
ADD ./client /usr/src/app
WORKDIR /usr/src/app
RUN rm -rf node_modules
RUN  npm i
EXPOSE 3000
CMD ["npm", "start"]