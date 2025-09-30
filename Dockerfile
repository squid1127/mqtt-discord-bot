# Use Python Alpine image for small size
FROM python:3.11-alpine

# Set working directory
WORKDIR /app

# Copy requirements first for better Docker layer caching
COPY requirements.txt .

# Install Python dependencies (discord.py has pre-built wheels for Alpine)
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY bot.py .
COPY .env* ./

# Create non-root user for security
RUN adduser -D -s /bin/sh botuser
USER botuser

# Run the bot
CMD ["python", "bot.py"]