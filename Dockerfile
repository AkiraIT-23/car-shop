FROM python:3.10-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

COPY requirements.txt ./
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /app
COPY . /app