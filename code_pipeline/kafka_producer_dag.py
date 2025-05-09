from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys

# Thêm đường dẫn đến thư mục chứa kafka_producer.py
sys.path.append('/home/ducvm/PROJECT/MT_App_Project/code')
from kafka_producer import run_producer

default_args = {
    'owner': 'Le Huynh Duc',
    'retries': 1,
    'retry_delay': timedelta(seconds=10),
}

with DAG(
    dag_id='kafka_producer_dag',
    default_args=default_args,
    description='Run Kafka producer every minute',
    schedule_interval='* * * * *',  # mỗi phút
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['kafka', 'producer'],
) as dag:
    
    task_run_kafka = PythonOperator(
        task_id='run_kafka_producer',
        python_callable=run_producer,
    )

    task_run_kafka
