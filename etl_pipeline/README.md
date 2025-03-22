# ETL Pipeline Overview 🧑‍💻

This ETL pipeline extracts, transforms, and loads data into Snowflake with detailed logging for each step.

### 1. Extract 📥
- The **`extract_data`** function reads data from a CSV file (`file_path`) and loads it into a pandas DataFrame. This function is crucial for pulling raw data that will later be transformed and loaded into Snowflake.
- **Logging**: After extraction, the number of rows extracted is logged for tracking.

### 2. Transform 🔄
- The **`transform_data`** function processes the extracted data (DataFrame) to clean, reshape, or modify it according to the business rules.
- **Logging**: After transformation, the number of rows post-transformation is logged.

### 3. Load 📤
- The **`load_data_to_snowflake`** function takes the transformed data and loads it into a Snowflake database using the provided connection details (`snowflake_config`).
- **Logging**: Logs confirm whether the data was successfully loaded into the specified Snowflake table.

### 4. Logging 📚
- The entire ETL pipeline is logged. There are individual log files for each step (**Extract**, **Transform**, **Load**), as well as a final log for the entire ETL process.

### Key Functions:
- **`extract_data(file_path)`**: Extracts data from the given file.
- **`transform_data(df)`**: Transforms the extracted data for further processing.
- **`load_data_to_snowflake(df, table_name, snowflake_config)`**: Loads the transformed data into Snowflake.

### Important Note 📝:
Before running the pipeline, ensure that you write your own **Snowflake connection credentials** in the `snowflake_config` dictionary, which is passed to the **`load_data_to_snowflake`** function. This will ensure that your pipeline can successfully connect to your Snowflake account and load the data.

---

This pipeline helps automate the process of transferring data from a raw CSV file into a Snowflake database, ensuring that the process is clean, efficient, and well-logged.

### To Run the Pipeline:
```bash
python etl_pipeline.py
