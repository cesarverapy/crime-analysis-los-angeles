import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def setup_plotting_style():
    """Set up the plotting style for consistent visualizations."""
    plt.style.use('default')  # Use default style instead of seaborn
    sns.set_theme()  # Apply seaborn theme
    plt.rcParams['figure.figsize'] = (12, 6)
    plt.rcParams['font.size'] = 12
    sns.set_palette("husl")

def plot_victim_age_distribution(df):
    """
    Plot the distribution of victim ages.
    
    Args:
        df (pd.DataFrame): Crime data with 'Vict Age' column
    """
    if 'Vict Age' not in df.columns:
        raise ValueError("DataFrame does not contain 'Vict Age' column")
    
    plt.figure(figsize=(12, 6))
    sns.histplot(data=df, x='Vict Age', bins=50)
    plt.title('Distribution of Victim Ages')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

def plot_crime_by_area(df):
    """
    Plot crime counts by area.
    
    Args:
        df (pd.DataFrame): Crime data with 'AREA NAME' column
    """
    if 'AREA NAME' not in df.columns:
        raise ValueError("DataFrame does not contain 'AREA NAME' column")
    
    plt.figure(figsize=(14, 6))
    area_counts = df['AREA NAME'].value_counts()
    sns.barplot(x=area_counts.values, y=area_counts.index)
    plt.title('Number of Crimes by Area')
    plt.xlabel('Number of Crimes')
    plt.ylabel('Area')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

def plot_crime_trends(df):
    """
    Plot crime trends over time.
    
    Args:
        df (pd.DataFrame): Crime data with 'DATE OCC' column
    """
    if 'DATE OCC' not in df.columns:
        raise ValueError("DataFrame does not contain 'DATE OCC' column")
    
    # Resample data by month
    monthly_crimes = df.set_index('DATE OCC').resample('M').size()
    
    plt.figure(figsize=(15, 6))
    monthly_crimes.plot(kind='line')
    plt.title('Crime Trends Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Crimes')
    plt.grid(True, alpha=0.3)
    plt.tight_layout() 