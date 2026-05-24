from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

# Define a simple Python function for a PythonOperator
def _extract_data():
    print("Simulating data extraction...")
    # In a real scenario, this would connect to a database, API, or file system
    # and return/store extracted data. For demonstration, we return a string.
    return "raw_data_extracted"

def _transform_data(ti):
    # Access data passed from a previous task using XComs (cross-communication)
    raw_data = ti.xcom_pull(task_ids='extract_data_task')
    print(f"Simulating data transformation on: {raw_data}")
    # In a real scenario, this would process the raw data
    transformed_data = f"transformed_{raw_data}"
    return transformed_data

with DAG(
    dag_id='simple_data_pipeline',
    start_date=datetime(2023, 1, 1),
    schedule_interval=None, # This DAG runs manually or on specific triggers
    catchup=False,
    tags=['example', 'pipeline', 'python'],
    doc_md="""
    ### Simple Data Pipeline DAG
    This DAG demonstrates a basic data processing workflow with Airflow.
    It includes tasks for extraction, transformation, and loading (ETL)
    using both Bash and Python operators, showcasing task dependencies.
    """
) as dag:
    # Task 1: Start message using BashOperator
    start_task = BashOperator(
        task_id='start_pipeline',
        bash_command='echo "Starting the data pipeline..."',
        # BashOperator executes a bash command.
    )

    # Task 2: Extract data using PythonOperator
    extract_data_task = PythonOperator(
        task_id='extract_data_task',
        python_callable=_extract_data,
        # PythonOperator executes a Python function.
        # The return value of the function is pushed to XComs by default.
    )

    # Task 3: Transform data using PythonOperator
    # This task depends on the output of 'extract_data_task' via XComs.
    transform_data_task = PythonOperator(
        task_id='transform_data_task',
        python_callable=_transform_data,
        # 'ti' (TaskInstance) is automatically passed to the callable
        # when 'provide_context=True' (default for PythonOperator).
    )

    # Task 4: Load data using BashOperator
    # This task simulates the final step of loading the processed data.
    load_data_task = BashOperator(
        task_id='load_data_task',
        bash_command='echo "Data loading complete. Transformed data ready!"',
    )

    # Define task dependencies to form the DAG (Directed Acyclic Graph)
    # The pipeline flows sequentially from start -> extract -> transform -> load
    start_task >> extract_data_task >> transform_data_task >> load_data_task
    # The '>>' operator defines the order of execution: task1 >> task2 means task2 runs after task1.
