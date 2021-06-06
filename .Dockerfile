FROM python:3.8-slim-buster

RUN mkdir -p /app
WORKDIR /app
ENV PYTHONPATH "${PYTHONPATH}:/app"

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY . ./

ENTRYPOINT [ "python" ]

EXPOSE 5000

CMD [ "app.py" ]