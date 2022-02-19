FROM ubuntu:20.04

# Update the repository sources list
RUN apt-get update
#RUN apt-get upgrade
#Install all the languages/compilers we are supporting.
RUN apt-get install -y python
RUN apt-get install -y pip
# Will add more interpreters and compilers here

WORKDIR /code
COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
WORKDIR /code/app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8084"]
