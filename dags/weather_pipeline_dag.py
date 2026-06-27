from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
    "retries": 1,
}

with DAG(
    dag_id="weather_etl_pipeline",
    default_args=default_args,
    description="Extract, transform, and load weather data into PostgreSQL",
    schedule_interval=None,
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["weather", "etl"],
) as dag:

    extract = BashOperator(
        task_id="extract_weather",
        bash_command="cd /workspaces/weather-data-pipeline && python scripts/extract_weather.py",
    )

    transform = BashOperator(
        task_id="transform_weather",
        bash_command="cd /workspaces/weather-data-pipeline && python scripts/transform_weather.py",
    )

    load = BashOperator(
        task_id="load_postgres",
        bash_command="cd /workspaces/weather-data-pipeline && python scripts/load_postgres.py",
    )

    plot = BashOperator(
        task_id="plot_weather",
        bash_command="cd /workspaces/weather-data-pipeline && python scripts/plot_weather.py",
    )

    extract >> transform >> load >> plot