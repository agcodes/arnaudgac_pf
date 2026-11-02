# Use an official Python runtime as a parent image
FROM python:3.14-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install minimal system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Set Django environment variables for build-time (collectstatic needs these)
ENV DJANGO_SECRET_KEY=dummy-for-build \
    DJANGO_DEBUG=True \
    DJANGO_ALLOWED_HOSTS=localhost

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port the app runs on (must match fly.toml internal_port=8080)
EXPOSE 8080

# Command to run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "django_cv.wsgi:application"]
