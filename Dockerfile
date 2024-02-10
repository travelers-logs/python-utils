FROM python:3.10-slim

# Set directory in the container
WORKDIR /app

# create logger directory structure
RUN mkdir -p /app/utils/logger

# Copy folders into the container
COPY utils /app/utils
