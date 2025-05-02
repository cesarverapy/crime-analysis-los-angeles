import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def setup_plotting_style():
    """Set up consistent plotting style for all visualizations."""
    plt.style.use('seaborn-v0_8')
    sns.set_palette("husl")

def plot_victim_age_distribution(df, figsize=(12, 6)):
    """Plot the distribution of victim ages."""
    plt.figure(figsize=figsize)
    sns.histplot(data=df, x='Vict Age', bins=30)
    plt.title('Victim Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Number of Victims')
    plt.tight_layout()
    return plt.gcf()

def plot_crime_by_area(df, figsize=(12, 6)):
    """Plot the distribution of crimes by area."""
    plt.figure(figsize=figsize)
    area_counts = df['AREA NAME'].value_counts()
    sns.barplot(x=area_counts.values, y=area_counts.index)
    plt.title('Crime Distribution by Area')
    plt.xlabel('Number of Crimes')
    plt.ylabel('Area')
    plt.tight_layout()
    return plt.gcf()

def plot_crime_trends(df, figsize=(12, 6)):
    """Plot crime trends over time."""
    plt.figure(figsize=figsize)
    monthly_crimes = df.groupby(['Year', 'Month']).size().reset_index(name='Count')
    monthly_crimes['Date'] = pd.to_datetime(monthly_crimes[['Year', 'Month']].assign(DAY=1))
    sns.lineplot(data=monthly_crimes, x='Date', y='Count')
    plt.title('Monthly Crime Trends')
    plt.xlabel('Date')
    plt.ylabel('Number of Crimes')
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt.gcf() 