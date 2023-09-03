FROM python:3.10-alpine

ADD xpost_update.py /
RUN pip install tweepy
VOLUME /data

ENTRYPOINT [ "python", "./xpost_update.py" ]