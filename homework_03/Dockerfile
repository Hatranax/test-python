# Command to build docker container: docker build . -t app
# Command to run: docker run -it -p 8000:8000 app 

FROM python:3.10.8-bullseye
ENV PYTHONUNBUFFERED=1
WORKDIR /MAIN
RUN pip install --upgrade pip
COPY Pipfile ./
COPY Pipfile.lock ./
RUN pip install pipenv
COPY . .
RUN pipenv install --system
EXPOSE 8000
CMD uvicorn app:application --host 0.0.0.0 --port 8000