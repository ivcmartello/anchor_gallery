# Anchor Gallery

[![Build Status](https://travis-ci.com/ivcmartello/registrobrepp.svg?branch=master)](https://travis-ci.com/ivcmartello/anchor_gallery.svg?token=YxevxaQeJibtDDNh8ij8&branch=main)

This project implement an application that can store photos and comments from them (Ex. Wedding).

Some techs approached:

Python >= 3.7.7

Django >= 3.2

Memcached

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install if you don't have:

- ### [Python](https://github.com/pyenv/pyenv) >= 3.7.7

- ### [pip](https://pip.pypa.io/en/stable/installing/)

- ### [PostgreSQL](https://www.postgresql.org/download/) or using [docker](https://hub.docker.com/_/postgres)

### Installing

Follow the instructions to get a development environment running:

The application will use PostgreSQL as the default database.

Create a file .env with your configurations:

```
PYTHON=venv/bin/python

VENV=venv

BIN=venv/bin

DEBUG=False

DJANGO_SETTINGS_MODULE_TEST=anchor_gallery.test_settings

DB_NAME=YOUR DATABASE NAME

DB_USER=YOUR DATABASE USER

DB_PASSWORD=YOUR DATABASE PASSWORD

DB_HOST=localhost OR YOUR DATABASE HOST

DB_PORT=5432 OR YOUR DATABASE PORT

SECRET_KEY=YOUR SECRET KEY

ALLOWED_HOSTS=*

#Optional

AWS_ACCESS_KEY_ID=YOUR AWS ACCESS KEY ID

AWS_SECRET_ACCESS_KEY=YOUR AWS SECRET ACCESS KEY
```

## **All the commands need to be done on main project folder (The folder where you cloned or unzip the files).**

If your environment supports Makefiles and have permission to execute, try some shortcuts:

To show the help menu type:

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

Create a super user to administrate the application:

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
> python3 manage.py test . --verbosity=2 --parallel --failfast --settings=anchor_gallery.test_settings
```
