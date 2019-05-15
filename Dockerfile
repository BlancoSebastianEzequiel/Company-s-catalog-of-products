FROM python:3.6
ADD . /usr/src/app
WORKDIR /usr/src/app
RUN rm -rf client
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["sh", "scripts/wsgi.sh"]