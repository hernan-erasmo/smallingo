# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        libc-dev \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to begin downloading packages
COPY ./requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Run Django makemigrations
RUN python manage.py makemigrations

# Run Django migrate
RUN python manage.py migrate

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the Django development server when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
