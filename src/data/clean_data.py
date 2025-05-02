import pandas as pd
import numpy as np

def clean_crime_data(df):
    """
    Clean the crime data by handling missing values, converting data types,
    and standardizing formats.
    
    Args:
        df (pd.DataFrame): Raw crime data
        
    Returns:
        pd.DataFrame: Cleaned crime data
    """
    # Create a copy to avoid modifying the original dataframe
    cleaned_df = df.copy()
    
    # Convert date columns to datetime
    date_columns = ['DATE OCC', 'Date Rptd']
    for col in date_columns:
        if col in cleaned_df.columns:
            cleaned_df[col] = pd.to_datetime(cleaned_df[col])
    
    # Handle missing values
    # For numeric columns, fill with median
    numeric_columns = cleaned_df.select_dtypes(include=[np.number]).columns
    for col in numeric_columns:
        cleaned_df[col] = cleaned_df[col].fillna(cleaned_df[col].median())
    
    # For categorical columns, fill with mode
    categorical_columns = cleaned_df.select_dtypes(include=['object']).columns
    for col in categorical_columns:
        cleaned_df[col] = cleaned_df[col].fillna(cleaned_df[col].mode()[0])
    
    # Drop any remaining rows with missing values
    cleaned_df = cleaned_df.dropna()
    
    # Convert victim age to numeric, replacing invalid values with NaN
    if 'Vict Age' in cleaned_df.columns:
        cleaned_df['Vict Age'] = pd.to_numeric(cleaned_df['Vict Age'], errors='coerce')
        # Remove unrealistic ages (e.g., negative or > 120)
        cleaned_df = cleaned_df[
            (cleaned_df['Vict Age'] >= 0) & 
            (cleaned_df['Vict Age'] <= 120)
        ]
    
    return cleaned_df 