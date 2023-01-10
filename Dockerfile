FROM python:3.9.16 as producer

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "producer-sync.py"]

FROM python:3.9.16 as consumer

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "consumer-sync.py"]