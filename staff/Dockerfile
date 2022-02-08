# syntax=docker/dockerfile:1
FROM python:3.8.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /home/abed/ALISTTECH/staff
COPY requirements.txt /home/abed/ALISTTECH/staff/
RUN pip install -r requirements.txt
COPY . /home/abed/ALISTTECH/staff/
