FROM python:3.9.16 as publisher

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "publisher-sync.py"]