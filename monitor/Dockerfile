
FROM python:3.9.5-slim-buster

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "src/monitor.py" ]
