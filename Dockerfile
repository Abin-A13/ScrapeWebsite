FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt


EXPOSE 8080

ENV env WORLD

CMD ["flask", "run","--host=0.0.0.0"]