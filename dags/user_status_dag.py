from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.hooks.mysql_hook import MySqlHook
from datetime import datetime
import csv

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 12, 1),
    'email': ['brianjrmo@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True
}

class ReturningMySqlOperator(MySqlOperator):
    def execute(self, context):
        self.log.info('Executing: %s', self.sql)
        hook = MySqlHook(mysql_conn_id=self.mysql_conn_id,
                         schema=self.database)
        table_data = hook.get_records(self.sql,parameters=self.parameters)
        with open('/opt/airflow/logs/usertable.csv','w') as out:
            csv_out=csv.writer(out)
            csv_out.writerows(table_data)
    
    
with DAG('user_status_dag', 
         catchup=False, 
         default_args=default_args,
         schedule_interval= '*/5 * * * *'
         ) as dag:
    start = DummyOperator(task_id='Start')
    
    t1 = ReturningMySqlOperator(
        task_id='select_mysql_task',
        mysql_conn_id='airflow_mysql_db',
        sql="""select * from usertable;"""
        )
    
    end = DummyOperator(task_id='End')

    start >> t1 >> end