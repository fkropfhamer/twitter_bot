FROM python:3

WORKDIR /app

COPY ./twitter_bot /app/twitter_bot

ENTRYPOINT ["python", "/app/twitter_bot/main.py"]
