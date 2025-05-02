import pandas as pd
import os

def load_crime_data():
    """
    Load the LA crime data from the CSV file.
    
    Returns:
        pd.DataFrame: The loaded crime data
    """
    data_path = os.path.join('dataset', 'raw', 'crimes.csv')
    
    try:
        df = pd.read_csv(data_path)
        return df
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        raise 