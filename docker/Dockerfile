# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /unispy-server

# Copy the requirements file into the container
COPY src/requirements.txt .

# Install the dependencies
RUN apt update && apt install -y curl && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt

# Create non-root user and group
RUN groupadd -g 1000 unispy && \
    useradd -u 1000 -g unispy -d /unispy-server -s /bin/bash unispy && \
    mkdir -p /unispy-server/log

# Copy source code and common files into the container
COPY src /unispy-server/src
COPY common /unispy-server/common

# Ensure non-root user owns the app directory and logs
RUN chown -R unispy:unispy /unispy-server

# Set default python environment variables
ENV PYTHONPATH=/unispy-server/src
ENV UNISPY_CONFIG=/unispy-server/common/config.json