# Dockerfile
FROM python:3.7
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev-is-python3 build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]