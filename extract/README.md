# Extract with Logging 🛠️📊

This project implements a simple ETL (Extract, Transform, Load) process with logging for the extraction step. It reads data from a CSV file and logs the success or failure of the extraction process. 📂➡️📝

## Files 📁
1. **extract.py**: Contains the logic for extracting data from a CSV file and logging the process. 🧑‍💻
2. **sample_data.csv**: Example CSV file (100 rows of dummy data) to demonstrate the extraction process. 📊

## How it Works 🔄

- The script reads a CSV file using `pandas.read_csv()`. 📑
- A logger (`extract_logger`) is set up to log messages about the extraction process. 📜
- The logger writes informational messages when the data extraction starts and completes successfully. ✅
- If an error occurs, the logger will capture and log the exception with an error message. ❌

## Requirements ⚙️
- Python 3.x 🐍
- pandas (`pip install pandas`) 📦

## Example Usage 🎬

1. Replace the file path in the `extract_data()` function with your own CSV file path. 📂
2. Run the script, and check the console for logs indicating the success or failure of the data extraction. 💻

## Logging 📝
- Logs are saved to a file named `extract.log`. 📜
- Logs include timestamps and log levels (INFO and ERROR). ⏱️🔴

## License 📄
This project is licensed under the MIT License. 📝

