FROM python:3.10-slim

# Ensure stdout/stderr is not buffered (important for logs in Docker)
ENV PYTHONUNBUFFERED=1

# Set Django settings module (if your settings file is in a custom location)
ENV DJANGO_SETTINGS_MODULE=Nykinsky.settings

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*


# Copy project files into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 (Django default dev server)
EXPOSE 8000

# Default command to run Django dev server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
