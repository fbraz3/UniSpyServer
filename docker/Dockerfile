# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /unispy-server

# Copy the requirements file into the container
COPY src/requirements.txt .

# Install the dependencies and gosu for step-down privileges
RUN apt update && apt install -y curl gosu && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt

# Create non-root user and group
RUN groupadd -g 1000 unispy && \
    useradd -u 1000 -g unispy -d /unispy-server -s /bin/bash unispy && \
    mkdir -p /unispy-server/log

# Copy source code, common files, and entrypoint script into the container
COPY src /unispy-server/src
COPY common /unispy-server/common
COPY docker/docker-entrypoint.sh /unispy-server/docker-entrypoint.sh

# Ensure non-root user owns the app directory and logs, and entrypoint is executable
RUN chmod +x /unispy-server/docker-entrypoint.sh && \
    chown -R unispy:unispy /unispy-server

# Set default python environment variables
ENV PYTHONPATH=/unispy-server/src
ENV UNISPY_CONFIG=/unispy-server/common/config.json

# Set default container user to non-root unispy user
USER unispy

ENTRYPOINT ["/unispy-server/docker-entrypoint.sh"]