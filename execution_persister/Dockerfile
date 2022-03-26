FROM ubuntu:20.04

# Update the repository sources list
RUN apt-get update

# Install python
RUN apt-get install -y python3
RUN apt-get install -y pip

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
WORKDIR /code/app
#CMD ["python", "main.py"]
