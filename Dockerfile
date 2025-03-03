# Use Python 3.9 slim as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy script.py into the container
COPY script.py .

# Copy the data folder into the container
COPY data /home/data

# Run the script on container start
CMD ["python", "script.py"]
