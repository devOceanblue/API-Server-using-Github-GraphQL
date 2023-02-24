# Tridge-Coding-Assignments

## Run
```shell
docker-compose up -d
```

## API Documentation
http://localhost:8080/docs#

## Description
### 1. how it is implemented
MVC Pattern is used to implement API server.
Controller(routes) layer handles requests and service Layer focuses on business logic.
there is no repository layer because there is no requirements to access database.

build docker image to run API server 

```shell
docker-compose up -d
```
you can try API, run
```shell
curl -X 'GET' \
  'http://localhost:8080/repository?request=facebook' \
  -H 'accept: application/json'
```

you can test 
```shell
 python -m pytest tests/test_repository_info.py 
```

environment variable saved in dockerfile and environment variable is configured in config.py 

### 2. GraphQL usages
  - used GraphQL to fetch data from github graphQL API
### 3. Possible improvements
  - GraphQL exception handling seems a bit tricky. there might be more exceptions. we need to catch and handle the exceptions more carefully.
