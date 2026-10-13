# Start from the pre-pulled lightweight Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Install required packages
RUN pip install flask redis

# Copy application source code into container
COPY app.py .

# Expose container port
EXPOSE 5000

# Set environment variable defaults
ENV REDIS_HOST=redis_db

# Run the application
CMD ["python", "app.py"]