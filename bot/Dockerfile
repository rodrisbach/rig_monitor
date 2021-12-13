
FROM python:3.9.5-slim-buster

WORKDIR /app

COPY src/ ./

COPY requirements.txt ./

RUN pip install -r requirements.txt

CMD [ "python", ".py" ]