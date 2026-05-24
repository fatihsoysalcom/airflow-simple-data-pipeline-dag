# Airflow Simple Data Pipeline DAG

This example defines a basic Apache Airflow Directed Acyclic Graph (DAG) in Python. It demonstrates how to create a data processing pipeline with sequential tasks using `BashOperator` and `PythonOperator`, including task dependencies and simple data passing via XComs. This file represents the core Python code a developer writes to define an Airflow workflow.

## Language

`python`

## How to Run

1. Ensure you have an Apache Airflow environment set up and running.
2. Place this `simple_data_pipeline.py` file into your Airflow DAGs folder (e.g., `AIRFLOW_HOME/dags`).
3. Airflow will automatically discover and parse the DAG. You can then enable and trigger it from the Airflow UI.

## Original Article

This example accompanies the Turkish article: [Python'dan Üretim Hattına: Apache Airflow ile Pratik Bir Kılavuz](https://fatihsoysal.com/blog/pythondan-uretim-hattina-apache-airflow-ile-pratik-bir-kilavuz/).

## License

MIT — see [LICENSE](LICENSE).
