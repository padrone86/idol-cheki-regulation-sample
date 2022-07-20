FROM python:3.9-slim

COPY Pipfile .
COPY Pipfile.lock .

RUN pip install pipenv --no-cache-dir
RUN pipenv sync --system  

COPY main.py .
CMD pipenv run server
