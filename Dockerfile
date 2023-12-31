# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=config.settings

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

RUN pip install -r requirements.txt

# Make port 1111 available to the world outside this container
EXPOSE 1111

# Run django server
CMD ["python", "escaperoom/manage.py", "runserver", "0.0.0.0:1111"]
# let docker sleep
# CMD ["sleep", "infinity"]