
# Data Transformation 🛠️

This project performs various data transformations on a DataFrame using Python and pandas. Here's a summary of the steps:

## Steps:

1. **Column Names Transformation 📊**  
   Convert all column names to uppercase 🔠.

2. **CUSTOMER_ID Transformation 💼**  
   Convert the `CUSTOMER_ID` column to integer 🧮.

3. **FIRST_NAME Transformation 👤**  
   - Strip and title-case the `FIRST_NAME` 💁‍♂️.
   - Handle `NaN` values by filling with a random choice from available names 🎲.

4. **LAST_NAME Transformation 🧑‍🦱**  
   - Title-case and strip the `LAST_NAME` 🧑‍🦱.
   - Fill `NaN` values with the name "Olivier" 👨‍🦳.

5. **EMAIL Transformation 📧**  
   - Clean and format the `EMAIL` by stripping and lowercasing ✉️.
   - If email starts with '@', append `FIRST_NAME` and `LAST_NAME` to the email 📝.

6. **PHONE_NUMBER Removal 🚫📱**  
   Drop the `PHONE_NUMBER` column from the DataFrame ❌.

7. **JOIN_DATE Transformation 📅**  
   - Convert `JOIN_DATE` to datetime format 🗓️.
   - Fill `NaT` (Not a Time) values with the current date 🗓️.

8. **CITY Transformation 🏙️**  
   Clean up and title-case the `CITY` names 🏙️.

9. **INCOME Transformation 💵**  
   - Convert `INCOME` to float 💰.
   - Fill `NaN` values with the mean of the column 🧮.

## Tools Used:

- Python 🐍
- pandas 📊
- logging 📜

## Purpose 🎯:

This script helps in cleaning and transforming data to ensure consistency and handle missing or incorrect values effectively.

# Data Transformation 🛠️

This script performs data transformation tasks on a given dataset using **pandas** and logs the progress and errors in a `transform.log` file. To run the script, use the command:

```bash
python transform.py
