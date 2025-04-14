# Dockerfile (optional simplification)
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


# Create a non-root user
RUN useradd -m appuser

# Set working directory
WORKDIR /src

# Copy code first (requirements.txt needed before pip install)
COPY . /src/


# Change ownership of the /app directory to the non-root user
RUN chown -R appuser:appuser /src
# Create a non-root user and use it to run the app
USER appuser

# Create and activate a virtual environment
RUN python -m venv venv
ENV PATH="/app/venv/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt


# Expose the port
EXPOSE 8081

# Run the app as the non-root user
CMD ["python", "app.py"]



