# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables to optimize pip
ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Upgrade pip
RUN #python -m pip install --upgrade pip

# Copy only the requirements first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application
COPY . /app

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define command to run the app
CMD ["python", "./app/main.py"]
