import pandas as pd

def print_dataset_info(df):
    """Print comprehensive information about the dataset."""
    print("Dataset Overview:")
    print("-" * 50)
    print(f"Number of Records: {len(df):,}")
    print(f"Time Period: {df['DATE OCC'].min().year} to {df['DATE OCC'].max().year}")
    print(f"Number of Unique Crime Types: {df['Crm Cd Desc'].nunique()}")
    print(f"Number of Areas: {df['AREA NAME'].nunique()}")
    print("\nMissing Values:")
    print(df.isnull().sum())

def get_crime_statistics(df):
    """Calculate and return key crime statistics."""
    stats = {
        'total_crimes': len(df),
        'unique_crime_types': df['Crm Cd Desc'].nunique(),
        'unique_areas': df['AREA NAME'].nunique(),
        'time_period': f"{df['DATE OCC'].min().strftime('%Y-%m-%d')} to {df['DATE OCC'].max().strftime('%Y-%m-%d')}",
        'avg_time_to_report': df['TimeToReport'].mean(),
        'most_common_crime': df['Crm Cd Desc'].mode().iloc[0],
        'most_common_area': df['AREA NAME'].mode().iloc[0]
    }
    return stats 