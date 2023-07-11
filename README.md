# Installation
```shell
docker build -t producer:1.0 --target producer .
docker build -t consumer:1.0 --target consumer .
docker run producer:1.0
docker run consumer:1.0
```
