# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /unispy-server

# Copy the requirements file into the container
COPY src/requirements.txt .

# Install the dependencies
RUN apt update && apt install -y curl && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code and common files into the container
COPY src /unispy-server/src
COPY common /unispy-server/common

# Set default python environment variables
ENV PYTHONPATH=/unispy-server/src
ENV UNISPY_CONFIG=/unispy-server/common/config.json