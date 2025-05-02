import pandas as pd
import numpy as np

def load_crime_data(file_path):
    """Load and parse the crime data CSV file."""
    return pd.read_csv(
        file_path,
        parse_dates=['Date Rptd', 'DATE OCC'],
        dtype={'TIME OCC': str},
        low_memory=False
    )

def preprocess_time_features(df):
    """Extract and standardize time-related features."""
    # Standardize time format and extract hour
    df['HOUR'] = df['TIME OCC'].str.zfill(4).str[:2].astype(int)
    
    # Extract additional time features
    df['Month'] = df['DATE OCC'].dt.month
    df['Year'] = df['DATE OCC'].dt.year
    df['Day'] = df['DATE OCC'].dt.day
    df['DayOfWeek'] = df['DATE OCC'].dt.day_name()
    
    # Calculate time to report
    df['TimeToReport'] = (df['Date Rptd'] - df['DATE OCC']).dt.days
    
    return df

def handle_missing_values(df):
    """Handle missing values in the dataset."""
    df['Vict Sex'] = df['Vict Sex'].fillna('Unknown')
    df['Vict Descent'] = df['Vict Descent'].fillna('Unknown')
    df['Weapon Desc'] = df['Weapon Desc'].fillna('No Weapon/Unknown')
    return df

def clean_crime_data(df):
    """Apply all cleaning steps to the crime data."""
    df = preprocess_time_features(df)
    df = handle_missing_values(df)
    return df 