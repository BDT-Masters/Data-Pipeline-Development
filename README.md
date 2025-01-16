# Traffic Accidents Data Analysis Pipeline

## Overview

This Python script provides a complete pipeline for analyzing traffic accidents data. It includes functionalities for loading, cleaning, transforming, and visualizing data, as well as saving processed outputs.

## Features

- **Data Loading**: Validates and loads data from a CSV file.
- **Data Cleaning**: Removes duplicates, trims whitespace, and standardizes categorical columns.
- **Data Transformation**: Adds computed fields such as `Severity Score`, `Fatality Rate`, and `Injury Rate`.
- **Data Aggregation**: Aggregates key metrics (e.g., accidents, fatalities) by country and year.
- **Exploratory Data Analysis (EDA)**: Generates plots to analyze accident trends and patterns.
- **Visualization**: Creates insightful visualizations such as:
  - Total accidents reported by country.
  - Average fatality rates by accident type.
  - Impact of road safety measures on fatality rates.
- **Output**: Saves aggregated and processed data to a CSV file.

## Requirements

- Python 3.7 or higher
- Libraries:
  - `pandas`
  - `matplotlib`
  - `seaborn`

Install dependencies using:
```bash
pip install pandas matplotlib seaborn
```

## How to Use

1. **Prepare the Input File**:
   - Place the input CSV file in the script directory. Ensure the file contains columns like `Year`, `Country`, `Accident Type`, `Accidents Reported`, `Fatalities`, `Injuries`, and `Road Safety Measures`.

2. **Run the Script**:
   ```bash
   python traffic_accidents_analysis.py
   ```
   By default, the script looks for an input file named `traffic_accidents.csv` and saves the processed data as `processed_traffic_data.csv`.

3. **Output Files**:
   - Aggregated data: `processed_traffic_data.csv`
   - Visualization images:
     - `eda_accidents_reported.png`
     - `total_accidents_reported.png`
     - `average_fatality_rate.png`
     - `impact_road_safety_measures.png`

## Functions

- **`load_data(file_path)`**: Reads data from the specified file path.
- **`clean_data(data)`**: Cleans and standardizes the dataset.
- **`transform_data(data)`**: Computes additional fields for analysis.
- **`aggregate_data(data)`**: Aggregates data by `Country` and `Year`.
- **`perform_eda(data)`**: Generates exploratory plots for trends over time.
- **`visualize_data(data)`**: Creates visualizations for key insights.
- **`save_data(data, output_path)`**: Exports processed data to a CSV file.
- **`run_pipeline(file_path, output_path)`**: Executes the entire analysis pipeline.

## Example

To analyze a dataset named `traffic_data_2024.csv` and save results as `output_data.csv`:
```bash
python traffic_accidents_analysis.py traffic_data_2024.csv output_data.csv
```

## Notes

- Ensure input files follow the expected schema with accurate column names.
- Customize the file paths in the `__main__` section for different datasets.
