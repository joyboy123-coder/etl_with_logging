
import logging
from extract.extract import extract_data
from transform.transform import transform_data
from load.load import load_data_to_snowflake
from logging import setup_logging

# Set up logging for the entire ETL pipeline
etl_logger = setup_logging()

def etl_pipeline(file_path, table_name, snowflake_config):
    try:
        etl_logger.info("ETL Pipeline started")

        # Step 1: Extract - Extract data using the file path
        df = extract_data(file_path)  # extract_data() returns a DataFrame
        etl_logger.info(f"Extracted {len(df)} rows from {file_path}")

        # Step 2: Transform - Transform the extracted data
        transformed_data = transform_data(df)  # data is passed here
        etl_logger.info(f"Data transformed. {len(transformed_data)} rows after transformation")

        # Step 3: Load - Load the transformed data into Snowflake
        load_data_to_snowflake(transformed_data, table_name, snowflake_config)
        etl_logger.info(f"Data successfully loaded into {table_name} on Snowflake")

        etl_logger.info("ETL Pipeline completed successfully")
    except Exception as e:
        etl_logger.error(f"ETL Pipeline failed: {e}")

if __name__ == '__main__':
    file_path = 'data.csv'  # Input data file path
    table_name = 'your_table_name'  # Snowflake target table
    snowflake_config = {}  # Snowflake connection config (replace with actual config)
    etl_pipeline(file_path, table_name, snowflake_config)  # Calling the pipeline function with the file path
