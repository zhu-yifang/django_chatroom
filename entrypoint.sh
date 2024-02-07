#!/bin/bash

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Create superuser only if environment variables are set and the superuser does not already exist
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
  echo "Checking for existing superuser..."
  SUPERUSER_EXISTS=$(echo "from django.contrib.auth.models import User; print(User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists())" | python manage.py shell)
  if [ "$SUPERUSER_EXISTS" = "False" ]; then
    echo "Creating superuser..."
    python manage.py createsuperuser --no-input
  else
    echo "Superuser already exists. Skipping creation."
  fi
else
  echo "Superuser creation skipped."
fi

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input

# Start the application
daphne -b 0.0.0.0 -p 8000 django_chatroom.asgi:application
