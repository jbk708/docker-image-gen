FROM python:3.11-slim

WORKDIR /app

# Copy application files
COPY app.py .
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Run the application
CMD ["python", "app.py"]

