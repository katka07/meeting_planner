FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && apt-get install netcat-traditional -y

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app/

#ENV DJANGO_SETTINGS_MODULE=meeting_planner.settings

#EXPOSE 8000

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
