FROM python:3.8-slim-buster

RUN apt update
RUN apt install -y mdbtools
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt