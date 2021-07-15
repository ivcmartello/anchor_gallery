# anchor_gallery

[![Build Status](https://travis-ci.com/ivcmartello/registrobrepp.svg?branch=master)](https://travis-ci.com/ivcmartello/anchor_gallery.svg?token=YxevxaQeJibtDDNh8ij8&branch=main)

This project implement an application that can store photos and comments from an event (Ex. Wedding).

Some techs approached:

Django >= 3.2
Memcached

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install if you don't have:

- ### [Python](https://github.com/pyenv/pyenv) >= 3.7.7

- ### [pip](https://pip.pypa.io/en/stable/installing/)

### Installing

Follow the instructions to get a development env running:

The application will use PostgreSQL as the default database and AWS S3 to store the images, so you need to provide some configurations in the .env file.

Create a file .env with your configurations:

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
ALLOWED_HOSTS=\*

AWS_ACCESS_KEY_ID=YOUR AWS ACCESS KEY ID
AWS_SECRET_ACCESS_KEY=YOUR AWS SECRET ACCESS KEY

## **All the commands need to be done on main project folder (The folder where you cloned or unzip the project).**

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

Run the application:

```
> python3 manage.py runserver
```

Open the browser and access the address:

<http://localhost:8000>

## Running the tests

How to run the tests:

```
> python3 manage.py test . --verbosity=2 --parallel --failfast --settings=anchor_gallery.test_settings
```
