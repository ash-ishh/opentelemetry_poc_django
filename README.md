# Opentelemetry POC Django

Setup:

1 - Create and activate virtual environment
```shell script
python3 -m venv venv
source venv/bin/activate
```

2 - Install dependencies
```shell script
pip install -r requirements.txt
```

3 - Setup Jaeger for collection and visualization

docker-compose.yml
```
version: '3'

services:
  jaeger:
    image: jaegertracing/all-in-one:latest
    container_name: jaeger
    restart: on-failure
    ports:
      - 14250:14250
      - 16686:16686

```
`$ docker-compose up -d`

4 - Running application with gunicorn  
```shell script
gunicorn -c gunicorn.conf.py opentelemetry_poc_django.wsgi -b 0.0.0.0:8000
```

5 - Testing Endpoint

http://localhost:8000/fibonacci/?n=4

6 - Jaeger UI URL

http://localhost:16686/
