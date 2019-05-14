FROM python:3.6
ADD . /usr/src/app
WORKDIR /usr/src/app
RUN rm -rf client
RUN pip install --upgrade pip
RUN sh scripts/install.sh
CMD ["bash", "scripts/wsgi.sh"]