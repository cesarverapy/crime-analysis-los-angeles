def print_dataset_info(df):
    """
    Print basic information about the dataset.
    
    Args:
        df (pd.DataFrame): Crime data
    """
    print("\nDataset Information:")
    print("-" * 50)
    print(f"Number of records: {len(df):,}")
    print(f"Number of columns: {len(df.columns)}")
    print(f"\nColumns:\n{df.columns.tolist()}")
    print("\nData types:")
    print(df.dtypes)
    print("\nMissing values:")
    print(df.isnull().sum())

def get_crime_statistics(df):
    """
    Calculate basic statistics about the crime data.
    
    Args:
        df (pd.DataFrame): Crime data
        
    Returns:
        dict: Dictionary containing various statistics
    """
    stats = {}
    
    # Total number of crimes
    stats['total_crimes'] = len(df)
    
    # Crimes by area
    if 'AREA NAME' in df.columns:
        stats['crimes_by_area'] = df['AREA NAME'].value_counts().to_dict()
    
    # Average victim age
    if 'Vict Age' in df.columns:
        stats['avg_victim_age'] = df['Vict Age'].mean()
    
    # Most common crime types
    if 'Crm Cd Desc' in df.columns:
        stats['top_crimes'] = df['Crm Cd Desc'].value_counts().head(10).to_dict()
    
    # Time-based statistics
    if 'DATE OCC' in df.columns:
        stats['crimes_by_year'] = df['DATE OCC'].dt.year.value_counts().sort_index().to_dict()
        stats['crimes_by_month'] = df['DATE OCC'].dt.month.value_counts().sort_index().to_dict()
        stats['crimes_by_day'] = df['DATE OCC'].dt.day_name().value_counts().to_dict()
    
    return stats 