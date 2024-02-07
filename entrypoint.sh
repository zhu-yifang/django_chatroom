#!/bin/bash

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Create superuser only if environment variables are set
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
  echo "Creating superuser..."
  python manage.py createsuperuser --no-input
else
  echo "Superuser creation skipped."
fi

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input

# Start the application
daphne -b 0.0.0.0 -p 8000 django_chatroom.asgi:application
