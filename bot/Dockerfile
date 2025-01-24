FROM python:3.9-alpine3.16
WORKDIR /bot
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .
CMD python3 app.py

