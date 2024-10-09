# airflow/dags/example_spark_dag.py

from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

with DAG('example_spark_dag', default_args=default_args, schedule_interval='@daily') as dag:
    
    spark_task = SparkSubmitOperator(
        task_id='spark_submit_job',
        application='/path/to/your/spark/job.py',  # Update with the path to your Spark application
        conn_id='spark_default',
        verbose=True,
        conf={'spark.executor.memory': '2g'},
    )
    
    spark_task
