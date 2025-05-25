# Base image
FROM python:3.12-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    libmysqlclient-dev \
    gcc \
    && apt-get clean

# Set working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the application
COPY . .

# Expose port (Django default)
EXPOSE 8000

# Default command (you can customize this)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
