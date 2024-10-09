# mlflow/Dockerfile
FROM ghcr.io/mlflow/mlflow:latest

# Install psycopg2 for PostgreSQL support
RUN pip install psycopg2-binary

EXPOSE 5000

# Start MLflow server
CMD ["mlflow", "server", "--host", "0.0.0.0", "--port", "5000"]
