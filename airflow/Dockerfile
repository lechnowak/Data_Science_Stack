# airflow/Dockerfile
FROM apache/airflow:2.8.0
USER root
RUN mkdir -p /opt/airflow/logs/scheduler && \
    chown -R airflow:airflow /opt/airflow/logs
USER airflow
RUN pip install --no-cache-dir \
    psycopg2-binary \
    apache-airflow-providers-postgres \
    apache-airflow-providers-amazon \
    apache-airflow-providers-apache-spark
