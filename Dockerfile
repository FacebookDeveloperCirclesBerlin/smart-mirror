FROM python:3.6

RUN apt-get update && apt-get install -y python3-tk

RUN pip install -U python-dotenv dnspython requests

COPY . /var/www/mirror

RUN cd /var/www/mirror

CMD ["python", "/var/www/mirror/mirror.py"]
