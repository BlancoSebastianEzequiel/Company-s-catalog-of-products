FROM nikolaik/python-nodejs:latest
ADD . /usr/src/app
WORKDIR /usr/src/app
EXPOSE 4000
RUN pip install --upgrade pip
WORKDIR /usr/src/app/client
RUN rm -rf node_modules
WORKDIR /usr/src/app
RUN sh scripts/install.sh
ENTRYPOINT ["sh","scripts/wsgi.sh"]