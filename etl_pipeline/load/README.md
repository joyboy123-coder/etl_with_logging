# 🚨 **Important Note on Snowflake Data Loading!** 🚨

This script allows you to **load data into a Snowflake database** from a pandas DataFrame using the `snowflake-connector-python` library. 🌨️

Please **do not forget** to replace the Snowflake credentials in the `snowflake_config` dictionary with your own details to establish a successful connection. Here’s what each part of the process does:

---

### **Step-by-Step Explanation:**

1. **Snowflake Configuration 📜:**
   - First, you'll need to **input your Snowflake credentials** (username, password, account, etc.) into the `snowflake_config` dictionary. Make sure these credentials are correct and provided to establish a secure connection.

2. **Logging 📊:**
   - A **logger** is set up for logging important actions and errors. This ensures you’ll be able to **track the success or failure** of your data load operations in an easily accessible log file.

3. **Connecting to Snowflake 🌐:**
   - The script connects to Snowflake using the `snowflake.connector.connect()` function. This connects to your specified Snowflake account using the credentials you provided earlier.

4. **Loading Data 🔄:**
   - The function `write_pandas` is used to load your **pandas DataFrame** (`df`) into the specified Snowflake table. It efficiently writes the data into the Snowflake table and returns a success status, row count, and other details.

5. **Error Handling ⚠️:**
   - If an error occurs during the data load process, the script logs the error and raises it, helping you identify any issues that may have occurred.

---

### **How to Run the Script 🏃‍♂️:**

Once you've replaced the **Snowflake credentials** with your own and provided a **valid pandas DataFrame** (`df`), you can execute the script by simply running the following command in your terminal or command prompt:

```bash
python load.py

