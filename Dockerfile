# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Install system dependencies
# gcc, libc-dev, libpq-dev -> required to install psycopg2
# software-properties-common, gnupg, python3-launchpadlib -> to be able to add ppa:jonathonf/ffmpeg-4
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        libc-dev \
        libpq-dev \
        software-properties-common \
        gnupg \
        python3-launchpadlib

# ppa:jonathonf/ffmpeg-4 -> to install ffmpeg
# ffmpeg -> to use moviepy
RUN add-apt-repository ppa:jonathonf/ffmpeg-4 \
    && apt-get install -y --no-install-recommends \
        ffmpeg \
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

# hack to make SmallingoVideo model 'upload_to' dirs exist and prevent moviepy errors
# these must match the values defined in settings.py
# TODO(Hernan): fix this shit
RUN mkdir -p /app/thumbnails
RUN mkdir -p /app/original_video
RUN mkdir -p /app/original_audio
RUN mkdir -p /app/translation_audio
RUN mkdir -p /app/thumbnails

# Run Django makemigrations
RUN python manage.py makemigrations

# Run Django migrate
RUN python manage.py migrate

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the Django development server when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
