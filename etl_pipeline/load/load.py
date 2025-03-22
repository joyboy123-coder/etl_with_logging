
import logging 
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

load_logger = logging.getLogger('load')


snowflake_config = {
    'user': 'your_user',
    'password': 'your_password',
    'account': 'your_account',
    'warehouse': 'your_warehouse',
    'database': 'your_database',
    'schema': 'your_schema'
}

def load_data_to_snowflake(df,table_name,snowflake_config):
    try:
        load_logger.info(f"Starting data load into Snowflake table {table_name}")
        conn = snowflake.connector.connect(
            user=snowflake_config['user'],
            password=snowflake_config['password'],
            account=snowflake_config['account'],
            warehouse=snowflake_config['warehouse'],
            database=snowflake_config['database'],
            schema=snowflake_config['schema']
        )
        success,nchunks,nrows, _ = write_pandas(conn,df,table_name)
        if success:
            load_logger.info(f"Successfully loaded {nrows} rows into {table_name}")
        else:
            load_logger.error("Data load failed")
    except Exception as e:
        load_logger.error(f"Data load failed: {e}")
        raise