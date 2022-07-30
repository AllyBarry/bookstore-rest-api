FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /usr/src/app

COPY ./app/Pipfile ./app/Pipfile.lock ./

RUN pip install pipenv

RUN pipenv install --system --deploy 

COPY ./app/* ./