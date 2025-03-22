import logging
import pandas as pd
import random

# Set up logging for the transform step
transform_logger = logging.getLogger('transform')

def transform_data(df):
    try:
        transform_logger.info("Starting data transformation")

        # Example transformation: Convert all column names to lowercase
        transform_logger.info("Transforming column names to uppercase")
        df.columns = df.columns.str.upper()

        # CUSTOMER_ID transformation: Convert to integer
        transform_logger.info("Transforming 'customer_id' to integer")
        df['CUSTOMER_ID'] = df['CUSTOMER_ID'].astype(int)

        # FIRST_NAME transformation: Clean up and apply random choice for NaN values
        transform_logger.info("Transforming 'first_name': stripping, title casing, and handling NaN values")
        df['FIRST_NAME'] = df['FIRST_NAME'].str.strip().str.title()
        df['FIRST_NAME'] = df['FIRST_NAME'].apply(
            lambda x: random.choice(df['FIRST_NAME'].dropna().tolist()) if pd.isna(x) else x
        )

        # LAST_NAME transformation: Title casing and filling NaN values with default name
        transform_logger.info("Transforming 'last_name': title casing and filling NaN values")
        df['LAST_NAME'] = df['LAST_NAME'].str.title().str.strip()
        df['LAST_NAME'] = df['LAST_NAME'].fillna('Olivier')

        # EMAIL transformation: Clean up and format
        transform_logger.info("Transforming 'email': filling NaN, stripping, and formatting")
        df['EMAIL'] = df['EMAIL'].fillna('user_invalid@gmail.com')
        df['EMAIL'] = df['EMAIL'].str.strip().str.lower()

        # Apply email correction by adding first and last name if starts with '@'
        transform_logger.info("Correcting 'email' by appending first and last name if email starts with '@'")
        df['EMAIL'] = df.apply(
            lambda row: f"{row['FIRST_NAME']}_{row['LAST_NAME']}".lower() + row['EMAIL'] if row['EMAIL'].startswith('@') else row['EMAIL'],
            axis=1
        )

        # Drop PHONE_NUMBER column
        transform_logger.info("Dropping 'phone_number' column")
        df.drop(columns='PHONE_NUMBER', inplace=True)

        # JOIN_DATE transformation: Convert to datetime and handle NaT values
        transform_logger.info("Transforming 'join_date': converting to datetime and filling NaT")
        df['JOIN_DATE'] = pd.to_datetime(df['JOIN_DATE'], errors='coerce')
        df['JOIN_DATE'] = df['JOIN_DATE'].fillna(pd.Timestamp('now')).dt.date

        # CITY transformation: Clean up city names
        transform_logger.info("Transforming 'city': stripping and title casing")
        df['CITY'] = df['CITY'].str.strip().str.title()

        # INCOME transformation: Convert to float and fill NaN with mean
        transform_logger.info("Transforming 'income': converting to float and filling NaN with mean")
        df['INCOME'] = df['INCOME'].astype(float)
        df['INCOME'] = df['INCOME'].fillna(df['INCOME'].mean())

        transform_logger.info("Data transformation completed successfully")

        # Log a brief summary of the data (instead of the full data)
        transform_logger.info(f"Transformed Data Sample:\n{df.head()}")

        return df

    except Exception as e:
        transform_logger.error(f"Data transformation failed: {e}")
        raise

