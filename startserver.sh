#!/bin/bash

DB_HOST="db"
DB_PORT="5432"  # Default PostgreSQL port

echo "========================================="
echo "[INFO]: Checking for db service to be up!"
echo "========================================="
# Use netcat (nc) to check if the database port is open
nc -z -w 2 $DB_HOST $DB_PORT

if [ $? -eq 0 ]; then
	echo "=================================="
	echo "[INFO]: DB service is reachable!"
	echo "=================================="
	echo "[INFO]: Make migrations!"
	python manage.py makemigrations
	echo "=================================="
	echo "[INFO]: Migrate!"
	python manage.py migrate
	echo "=================================="
	echo "[INFO]: Start Server!"
	python manage.py runserver 0.0.0.0:8000
	echo "=================================="
else
	echo "=================================="
	echo "[ERROR]: Database is not reachable!"
	exit 1  # Exit with error status code
fi
