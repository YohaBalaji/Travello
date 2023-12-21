FROM python:3.8-buster

ENV PYTHONBUFFERED=1

WORKDIR /django_travello

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:3001"]
