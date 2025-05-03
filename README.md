# Los Angeles Crime Analysis

Data Analysis exploring crime patterns in Los Angeles.

## Project Structure
```
crime-analysis-los-angeles/
├── dataset/                    # Data files
│   ├── raw/                   # Original data files
│   └── processed/             # Processed data files
├── src/                       # Source code
│   ├── data/                 # Data processing scripts
│   │   ├── load_data.py     # Data loading functions
│   │   └── clean_data.py    # Data cleaning functions
│   ├── visualization/        # Visualization functions
│   │   └── visualize.py     # Crime data visualization
│   └── utils/               # Utility functions
│       └── data_info.py     # Dataset information utilities
├── test_code.py             # Test suite for project functionality
└── requirements.txt         # Project dependencies
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

## Project Features
1. Data Loading and Cleaning:
   - Load crime data from CSV files
   - Clean and preprocess data
   - Handle missing values and data types

2. Data Analysis:
   - Generate dataset statistics
   - Analyze crime patterns
   - Visualize crime trends

3. Visualization:
   - Victim age distribution
   - Crime counts by area
   - Crime trends over time

## Code Organization
- `src/data/load_data.py`: Functions for loading crime data
- `src/data/clean_data.py`: Functions for cleaning and preprocessing data
- `src/visualization/visualize.py`: Functions for creating crime analysis visualizations
- `src/utils/data_info.py`: Utility functions for dataset information and statistics
- `test_code.py`: Test suite to verify project functionality

## Future

- Add more visualization
- Add more types of analysis
