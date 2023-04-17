FROM python:3.7

RUN apt-get update
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt

EXPOSE 80
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
