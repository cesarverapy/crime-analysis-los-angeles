# Los Angeles Crime Analysis

Data Analysis exploring crime patterns in Los Angeles.

## Project Structure
```
crime-analysis-los-angeles/
├── data/                    # Raw and processed data
│   ├── raw/                # Original data files
│   └── processed/          # Processed data files
├── notebooks/              # Jupyter notebooks
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_cleaning.ipynb
│   └── 03_analysis.ipynb
├── src/                   
│   ├── data/              # Data processing scripts
│   ├── visualization/     # Visualization functions
│   └── utils/            
├── reports/               # Generated reports and visualizations
└── requirements.txt       # Project dependencies
```

## Setup
1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Workflow
1. Data Exploration: `notebooks/01_data_exploration.ipynb`
2. Data Cleaning: `notebooks/02_data_cleaning.ipynb`
3. Analysis: `notebooks/03_analysis.ipynb`