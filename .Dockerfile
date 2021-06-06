FROM python:3.8-slim-buster

ENV PYTHONPATH "${PYTHONPATH}"

COPY .requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python", "app.py" ]