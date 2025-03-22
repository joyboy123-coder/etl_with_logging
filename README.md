# 🚀 ETL Pipeline with Logging  

## 📌 Project Overview  
This project is an **ETL (Extract, Transform, Load) pipeline** designed to process customer data and load it into **Snowflake**. The pipeline includes **logging** to track execution, handle errors, and monitor the status of the ETL process.  

## 🔄 How It Works  
The pipeline follows three main stages:  

1. **📥 Extract** – Reads raw data from a specified file.  
2. **🔄 Transform** – Cleans and processes the extracted data.  
3. **📤 Load** – Uploads the transformed data to **Snowflake**.  

✅ Logging is implemented using `try-except` blocks to capture errors, and logs are recorded at every stage.  

---

## ⚙️ Setup and Installation  

### 📌 Step 1: Install Dependencies  
Ensure you have Python installed, then navigate to the project directory and run:  

```sh
pip install -r requirements.txt
```  

### 🔑 Step 2: Configure Snowflake Credentials  
- Open **load.py**  
- Update the script with your **Snowflake credentials** (account, user, password, database, warehouse, etc.)  

### 📂 Step 3: Update the File Path  
- Open **etl_pipeline.py**  
- Modify the `file_path` variable to point to your dataset  

### 🏗️ Step 4: Create the Target Table  
Ensure that the target table exists in Snowflake before running the pipeline. You can manually create it based on your data schema.  

### ▶️ Step 5: Run the Pipeline  
Execute the ETL process using:  

```sh
python etl_pipeline.py
```  

---

## 📝 Logging Details  
✅ Logs for each stage (**extract, transform, load**) are stored in their respective folders.  
✅ The **etl_pipeline.log** file is created at the root of the project to track overall pipeline execution.  
✅ The logging system records process flow, errors, and execution time to help with debugging and monitoring.  

---

## 🚨 Error Handling  
The pipeline uses `try-except` blocks to capture errors at every stage. If an error occurs, it is logged for further debugging, ensuring smooth execution and failure tracking.  

📌 **In case of issues, check the logs for insights into what went wrong!**  

🚀 **Happy Data Processing!** 🎯  
