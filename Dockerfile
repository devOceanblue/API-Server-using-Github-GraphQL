FROM python:3.11

COPY ./Pipfile* /
RUN pip install pipenv
RUN pipenv install --dev --system

RUN mkdir /app
VOLUME /app

COPY . /app
WORKDIR /app

ENV GITHUB_TOKEN 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
ENV LOG_LEVEL 20

EXPOSE 8080

CMD uvicorn main:app --host 0.0.0.0 --reload --port 8080
