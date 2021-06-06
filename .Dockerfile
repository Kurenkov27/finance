FROM python:3.8-slim-buster

COPY requirements.txt app/requirements.txt

WORKDIR /app

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python" ]

EXPOSE 5000

CMD [ "app.py" ]