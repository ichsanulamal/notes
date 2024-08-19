## Assumptions and Prerequisites

- Data sourced is already deployed on PostgreSQL 
- ETL run is scheduled everyday by full refresh, otherwise you can insert incrementally

# Steps

1. Make sure to import OLTP data from [here](https://www.postgresqltutorial.com/postgresql-getting-started/postgresql-sample-database/) to PostgreSQL
2. Run Airflow
3. Connect database to Airflow from Airflow Web UI
4. Trigger DAG

# Components 

## Data sources used

https://github.com/darshilparmar/Data-Engineer-Tutorial-Series


## Airflow

https://towardsdatascience.com/run-airflow-docker-1b83a57616fb

## MySQL to PostgreSQL Airflow custom operator

https://medium.com/data-folks-indonesia/airflow-create-custom-operator-from-mysql-to-postgresql-a69d95a55c03

https://stackoverflow.com/questions/61663009/reading-sql-file-with-jinja-templates-in-custom-operator-in-airflow

### Connect 

https://stackoverflow.com/questions/69596430/airflow-with-docker-connect-to-a-local-host-postgresql


