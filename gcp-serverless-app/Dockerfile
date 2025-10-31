# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy dependencies first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app
COPY . .

# Set environment variable for Flask port
ENV PORT=8080
EXPOSE 8080

# Run the app using Gunicorn (production-grade WSGI server)
CMD exec gunicorn --bind :$PORT app:app
