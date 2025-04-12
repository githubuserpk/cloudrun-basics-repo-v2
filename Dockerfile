# Dockerfile (optional simplification)
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Only Flask needed for now
RUN pip install --no-cache-dir flask google-cloud-storage

WORKDIR /app
COPY app.py .

CMD ["python", "app.py"]

EXPOSE 8081