FROM python:3.8-slim-buster

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python" ]

EXPOSE 5000

CMD [ "app.py" ]