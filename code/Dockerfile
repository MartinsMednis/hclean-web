# Pull base image
FROM python:3.7
MAINTAINER Martins M.<mrt@mednis.info>
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get -qq -y install python-dev
RUN apt-get -qq -y install libpq-dev

# Set work directory
WORKDIR /code

# Install dependencies
# COPY Pipfile Pipfile.lock /code/
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# RUN pip install pipenv && pipenv install --system
# Copy project
COPY . /code/

# CMD ["./run_app.sh"]

# EXPOSE 8000
