# pull official base image
FROM python:3

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install os dependencies
RUN apt-get update && apt-get install -y \
        gcc \
        libmemcached11 \
        libmemcachedutil2 \
        libmemcached-dev \
        libz-dev \
        netcat

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

RUN chmod 755 docker-entrypoint.sh

# run docker-entrypoint.sh
ENTRYPOINT ["/usr/src/app/docker-entrypoint.sh"]