#!/bin/bash

DB_HOST="db"
DB_PORT="5432"  # Default PostgreSQL port
MAX_ATTEMPTS=60  # Maximum number of attempts
SLEEP_INTERVAL=5  # Sleep interval in seconds

echo "========================================="
echo "[INFO]: Checking for db service to be up!"
echo "========================================="

attempt=1

# Loop to check the database availability
while [ $attempt -le $MAX_ATTEMPTS ]; do
    echo "[INFO]: Attempt $attempt/$MAX_ATTEMPTS - Checking database availability..."

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
        echo "[INFO]: Database is not reachable. Retrying in $SLEEP_INTERVAL seconds..."
        sleep $SLEEP_INTERVAL
        ((attempt++))
    fi
done

echo "=================================="
echo "[ERROR]: Maximum attempts reached. Database is still not reachable."
exit 1  # Exit with error status code

