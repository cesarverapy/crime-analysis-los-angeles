# Los Angeles Crime Analysis

A data analysis project exploring crime patterns in Los Angeles.

## Project Structure
```
crime-analysis-los-angeles/
├── dataset/                    # Data files
│   ├── raw/                   # Original data files
│   └── processed/             # Processed data files
├── notebooks/                 # Jupyter notebooks
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_cleaning.ipynb
│   └── 03_analysis.ipynb
├── src/                       # Source code
│   ├── data/                 # Data processing scripts
│   │   └── process_data.py
│   ├── visualization/        # Visualization functions
│   │   └── plotting.py
│   └── utils/               # Utility functions
│       └── data_info.py
└── requirements.txt          # Project dependencies
```

## Setup
1. Create a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Workflow
1. Data Exploration (`notebooks/01_data_exploration.ipynb`):
   - Initial data loading and exploration
   - Basic visualizations
   - Understanding data structure and quality

2. Data Cleaning (`notebooks/02_data_cleaning.ipynb`):
   - Handle missing values
   - Standardize formats
   - Feature engineering
   - Save cleaned data

3. Analysis (`notebooks/03_analysis.ipynb`):
   - Load cleaned data
   - Generate insights
   - Create visualizations
   - Statistical analysis

## Code Organization
- `src/data/process_data.py`: Functions for loading and cleaning crime data
- `src/visualization/plotting.py`: Functions for creating crime analysis visualizations
- `src/utils/data_info.py`: Utility functions for dataset information and statistics