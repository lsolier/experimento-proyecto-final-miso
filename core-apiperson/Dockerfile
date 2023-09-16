# pull official base image
FROM python:3.9-slim

# set work directory
WORKDIR /core-apiperson

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt /users/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY src /users/src
COPY manage.py /users

# set environment variable for port
ENV PORT_CORE_APIPERSON 9000

# run entrypoint.sh / start up
CMD gunicorn --bind 0.0.0.0:${PORT_CORE_APIPERSON} manage:app --log-level debug