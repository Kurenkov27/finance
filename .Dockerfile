FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . ./

ENTRYPOINT [ "python" ]

EXPOSE 5000

CMD [ "app.py" ]