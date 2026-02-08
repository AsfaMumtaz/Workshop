# Use official Python 3 image
FROM python:3.11-alpine

# Set working directory
WORKDIR /app

# Copy backend code into container
COPY backend.py .

# Expose port 3000
EXPOSE 3000

# Run the backend
CMD ["python", "backend.py"]
