# MD-APICANDIDATES

> ## Capabilities

### Get candidate information

    obtains the candidate's information by validating the JWT token received.

> ## Runing

### Local

    In order to run the md-apicandidate locally, perform the following steps:

    python -m venv venv
    source /venv/bin/activate
    pip install -r requirements.txt
    gunicorn --bind 0.0.0.0:9001 manage:app --log-level debug

### Dockerfile

    In order to run the md-apicandidate by dockerfile, perform the following steps:

    docker image build --tag md-apicandidate:1.0.0 .
    docker container run -e CONFIG_PORT=9001 --detach -p 9001:9001 --name md-apicandidate md-apicandidate:1.0.0

