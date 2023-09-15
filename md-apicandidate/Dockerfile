# pull official base image
FROM python:3.9-slim

# set work directory
WORKDIR /users

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
ENV PORT_MD_APICANDIDATE 9001

# run entrypoint.sh / start up
CMD gunicorn --bind 0.0.0.0:${PORT_MD_APICANDIDATE} manage:app --log-level debug