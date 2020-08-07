FROM python:3

WORKDIR /app

COPY ./twitter_bot /app/twitter_bot
COPY ./config.json /app
COPY ./requirements.txt /app

RUN pip install -r /app/requirements.txt

ENTRYPOINT ["python", "/app/twitter_bot/main.py"]
