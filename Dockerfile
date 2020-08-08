FROM tensorflow/tensorflow:latest

WORKDIR /app

COPY ./twitter_bot /app/twitter_bot
COPY ./config.json /app
COPY ./requirements.txt /app
COPY ./models /app/models

RUN pip install -r /app/requirements.txt

ENTRYPOINT ["python", "/app/twitter_bot/main.py"]
