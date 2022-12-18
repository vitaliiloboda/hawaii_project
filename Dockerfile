FROM python:3.9-slim-buster
ENV PYTHONUNBUFFERED 1

RUN apt-get update

RUN apt-get install -y libpq-dev python3-pip python-dev postgresql postgresql-contrib netcat

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]