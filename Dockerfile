FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DJANGO_SETTINGS_MODULE=meeting_planner.settings

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]
