# Use the official Python base image
FROM python:3.10-slim

# Set environment variables to prevent Python from writing .pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy requirements (optional but good practice)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose the port Render expects (10000)
EXPOSE 10000

# Run the Streamlit app on port 10000
CMD ["streamlit", "run", "app.py", "--server.port=10000", "--server.address=0.0.0.0"]
