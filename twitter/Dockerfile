FROM python:3.9.4-slim

RUN apt-get update
RUN apt-get upgrade -y

# Setup
COPY . /app/
WORKDIR /app
RUN pip install -r requirements.txt

CMD python twitter_stream_to_kafka.py