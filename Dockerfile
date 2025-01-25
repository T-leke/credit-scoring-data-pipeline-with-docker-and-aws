# Use an official Python runtime as the base image
FROM python:3.11-slim  

# Set the working directory in the container
WORKDIR /app

# Install system dependencies required for Python and distutils
RUN apt-get update && apt-get install -y \
    python3-distutils \
    python3-apt \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip, setuptools, and wheel
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Copy the requirements file first to leverage Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Specify the command to run your Python application
CMD ["python", "main.py"]

