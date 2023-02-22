FROM python:3.11

COPY ./Pipfile* /
RUN pip install pipenv
RUN pipenv install --dev --system

RUN mkdir /app
VOLUME /app

COPY . /app
WORKDIR /app

EXPOSE 8082

CMD uvicorn main:app --host 0.0.0.0 --port 8082
