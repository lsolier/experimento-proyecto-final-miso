# CORE-APIPERSON

> ## Capabilities

#### POST `/persons` | Save person information
#### GET `/persons/{id}` | Get person information by id
#### POST `/persons/health` | API health status

> ## Runing

### Local

    In order to run the core-apiperson locally, perform the following steps:

    python -m venv venv
    source /venv/bin/activate
    pip install -r requirements.txt
    gunicorn --bind 0.0.0.0:9000 manage:app --log-level debug

### Dockerfile

    In order to run the core-apiperson by dockerfile, perform the following steps:

    docker image build --tag md-apicandidate:1.0.0 .
    docker container run -e CONFIG_PORT=9000 --detach -p 9000:9000 --name core-apiperson core-apiperson:1.0.0

