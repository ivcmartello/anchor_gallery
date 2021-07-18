# Anchor Gallery

[![Build Status](https://travis-ci.com/ivcmartello/registrobrepp.svg?branch=master)](https://travis-ci.com/ivcmartello/anchor_gallery.svg?token=YxevxaQeJibtDDNh8ij8&branch=main)

This project implement an application that can store photos and comments from them (Ex. Wedding).

- The main page is a list of photos, uploaded by people. Each photo can be commented clicking on it. Also the people can click on like button too.
- There is a page used to upload photos where you can provide information and attach the photo to upload.
- After any upload, the admin user needs to approve to show the photo in gallery. It will be done on admin site.

[Demo](https://anchor-gallery-test.herokuapp.com/)

User for the admin site:

```
Username: admin

Password: 123456
```

## Some technologies approached

- Python >= 3.7.7

- Django >= 3.2

- Memcached

- PostgreSQL

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes (Mac OS or Linux).

### Prerequisites

What things you need to install if you don't have:

- ### [Python](https://github.com/pyenv/pyenv) >= 3.7.7

- ### [pip](https://pip.pypa.io/en/stable/installing/)

- ### [PostgreSQL](https://www.postgresql.org/download/)

- ### Memcached

```
## On Ubuntu

> sudo apt-get update
> sudo apt-get install -y gcc libmemcached11 libmemcachedutil2 libmemcached-dev libz-dev
```

- ### [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) - Optional

### Installing

Follow the instructions to get a development environment running:

The application will use PostgreSQL as the default database, so you need to install and configure it first.

## **All the commands need to be done on main project folder (The folder where you cloned or unzip the files).**

Create a file .env with your configurations:

```
PYTHON=venv/bin/python
VENV=venv
BIN=venv/bin
DEBUG=False

#Recommended config to test.
DATABASE=postgres
DB_NAME=db_test
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432

SECRET_KEY=YOUR SECRET KEY

#Optional
AWS_ACCESS_KEY_ID=YOUR AWS ACCESS KEY ID
AWS_SECRET_ACCESS_KEY=YOUR AWS SECRET ACCESS KEY
AWS_S3_REGION_NAME=YOUR AWS REGION
```

There is a Makefile with some shortcuts. To show the help menu type:

```
> make
```

```
help                 Show this help
venv                 Make a new virtual environment
install              Make venv and install requirements
migrate              Make and run migrations
super                Create super user to access admin system
test                 Run tests
run                  Run the Django server
start                Install requirements, apply migrations, then start development server
```

If you prefer keep following the instructions instead make commands feel free.

Create a virtual environment:

```
> python3 -m venv venv
```

Active the virtual environment:

```
> source venv/bin/activate
```

Install requirements:

```
> pip install -r requirements-dev.txt
```

Run migrations:

```
> python3 manage.py migrate
```

Create a super user:

```
> python3 manage.py createsuperuser
```

Run the application:

```
> python3 manage.py runserver
```

Access the address on your browser:

<http://localhost:8000>

## Running the tests

How to run the tests:

```
> DJANGO_SETTINGS_MODULE=anchor_gallery.settings_test coverage erase && coverage run manage.py test --verbosity=2 --failfast && coverage report -m
```

## Running project on Docker

How to run the application on docker (use "--build" parameter just in the first time):

```
> docker-compose up -d --build
```

Create super user to access admin site:

```
> docker-compose exec web python manage.py createsuperuser
```

Access the address on your browser:

<http://localhost:8000>

Closing:

```
> docker-compose down
```
