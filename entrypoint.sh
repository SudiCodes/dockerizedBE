#!/bin/sh

# Wait for the database container to be ready
# wait-for-it db:5432 -s -t 30

# ANSI escape sequence for orange color
ORANGE='\033[0;33m'
# ANSI escape sequence to reset text color
RESET='\033[0m'

# Create the database
echo  "${ORANGE}Installing pg-client ...${RESET}"
apt-get update -y && apt-get install -y postgresql-client

echo  "${ORANGE}Setting up database ...${RESET}"
export PGPASSWORD="admin"
psql -U postgres -h db -p 5432 -c "CREATE DATABASE dockerized_db;"

# Change to the appropriate directory
echo  "${ORANGE}Changing the working directory ...${RESET}"
cd /app/mt_backend

# Migrate the database
echo  "${ORANGE}Running migrations for django ...${RESET}"
python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate

# Install pwgen
echo  "${ORANGE}Installing pwgen ...${RESET}"
apt-get install -y pwgen

# Set up the superuser
echo  "${ORANGE}Creating superuser ...${RESET}"
export DJANGO_SUPERUSER_PASSWORD=$(pwgen 32 1)
python manage.py createsuperuser --no-input --email admin@felxiend.com --first_name admin --last_name $(hostname)

# Create a non-root user
echo  "${ORANGE}Creating an appuser...${RESET}"
adduser -u 5678 --disabled-password --gecos "" appuser
chown -R appuser /app

# Start the Gunicorn server
echo  "${ORANGE}Starting up gunicorn ...${RESET}"
exec gunicorn --bind 0.0.0.0:8000 mt_backend.wsgi
