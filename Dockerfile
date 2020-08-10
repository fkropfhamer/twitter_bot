FROM python:3.7

WORKDIR /app

COPY ./twitter_bot /app/twitter_bot
COPY ./config.json /app
COPY ./models /app/models

RUN pip install pillow numpy tweepy
RUN pip install https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp37-cp37m-linux_x86_64.whl

ENTRYPOINT ["python", "/app/twitter_bot/main.py"]
