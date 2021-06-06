FROM python:3.8-slim-buster

RUN mkdir -p /app
WORKDIR /app
ENV PYTHONPATH "${PYTHONPATH}:/app"



COPY . .

EXPOSE 5000

CMD [ "python", "app.py" ]