import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
from src.data.load_data import load_crime_data
from src.data.clean_data import clean_crime_data
from src.visualization.visualize import (
    setup_plotting_style,
    plot_victim_age_distribution,
    plot_crime_by_area,
    plot_crime_trends
)
from src.data.data_info import print_dataset_info, get_crime_statistics

def test_data_loading():
    """Test if the data loading function works correctly."""
    try:
        print("\nTesting data loading...")
        df = load_crime_data()
        assert isinstance(df, pd.DataFrame), "Data loading failed: returned object is not a DataFrame"
        assert not df.empty, "Data loading failed: DataFrame is empty"
        print("✓ Data loading test passed!")
        return df
    except Exception as e:
        print(f"✗ Data loading test failed: {str(e)}")
        return None

def test_data_cleaning(df):
    """Test if the data cleaning function works correctly."""
    if df is None:
        print("✗ Skipping data cleaning test due to failed data loading")
        return None
    
    try:
        print("\nTesting data cleaning...")
        cleaned_df = clean_crime_data(df)
        assert isinstance(cleaned_df, pd.DataFrame), "Data cleaning failed: returned object is not a DataFrame"
        assert not cleaned_df.empty, "Data cleaning failed: DataFrame is empty"
        assert cleaned_df.isna().sum().sum() < df.isna().sum().sum(), "Data cleaning failed: no reduction in missing values"
        print("✓ Data cleaning test passed!")
        return cleaned_df
    except Exception as e:
        print(f"✗ Data cleaning test failed: {str(e)}")
        return None

def test_data_info_functions(df):
    """Test if the data information functions work correctly."""
    if df is None:
        print("✗ Skipping data info test due to failed data cleaning")
        return
    
    try:
        print("\nTesting data info functions...")
        print_dataset_info(df)
        stats = get_crime_statistics(df)
        assert isinstance(stats, dict), "Crime statistics failed: returned object is not a dictionary"
        print("✓ Data info functions test passed!")
    except Exception as e:
        print(f"✗ Data info functions test failed: {str(e)}")

def test_visualization_functions(df):
    """Test if the visualization functions work correctly."""
    if df is None:
        print("✗ Skipping visualization test due to failed data cleaning")
        return
    
    try:
        print("\nTesting visualization functions...")
        setup_plotting_style()
        
        # Test each visualization function
        plot_victim_age_distribution(df)
        plt.close()
        
        plot_crime_by_area(df)
        plt.close()
        
        plot_crime_trends(df)
        plt.close()
        
        print("✓ Visualization functions test passed!")
    except Exception as e:
        print(f"✗ Visualization functions test failed: {str(e)}")

def main():
    """Run all tests."""
    print("Starting tests for LA Crime Analysis project...")
    
    # Run tests in sequence
    raw_df = test_data_loading()
    cleaned_df = test_data_cleaning(raw_df)
    test_data_info_functions(cleaned_df)
    test_visualization_functions(cleaned_df)
    
    print("\nAll tests completed!")

if __name__ == "__main__":
    main() 