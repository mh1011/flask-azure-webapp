FROM python:3.11.8-alpine

WORKDIR /hello-world

COPY requirements.txt /hello-world

RUN pip install -r requirements.txt --no-cache-dir

COPY . /hello-world

CMD python3 app.py
