FROM python:3.12.3-slim-bullseye

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD [ "python3", "app.py" ]
