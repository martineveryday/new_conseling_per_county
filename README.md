# Report Generator Script

## Overview
This script processes and visualizes data related to counseling service requests. It performs operations such as data cleaning, aggregation, and plotting horizontal bar charts. Outputs include CSV files and PNG charts, organized by counties and centers.

## Features
- **Data Processing**: Reads multiple CSV files and converts numeric columns for analysis.
- **Data Aggregation**: Groups and aggregates data by counties or centers.
- **Customizable Graphs**: Generates horizontal bar charts for visual insights.
- **Configurable**: Uses a JSON configuration file for center mappings.
- **Percentage Calculation**: Computes conversion rates for sessions.

## Prerequisites
### Python Libraries
Make sure the following libraries are installed:
- `pandas`
- `matplotlib`
- `json`

You can install them using pip:
```bash
pip install pandas matplotlib
```

### Files Required
- `centers_mapping.json`: JSON file with mappings for center names.
- CSV files:
  - `req_counseling_FY2024.csv`
  - `conversion_rate_FY2024.csv`
  - `conversion_initial_only.csv`
  - `conversion_initial_hour_or_more.csv`
  - `at_least_30_minutes.csv`

## Usage
### Script Execution
1. Ensure all required files are in the script's directory.
2. Run the script using Python:
   ```bash
   python script_name.py
   ```
3. The script generates the following outputs:
   - Horizontal bar charts saved as PNG files.
   - Aggregated data saved as CSV files.

### Outputs
- **Graphs**:
  - Visualizations of counseling request data.
  - Example: `Number of New Counseling Requests (FY 2024).png`

- **Reports**:
  - Aggregated data by county or center.
  - Example: `Number_of_eCenter_Counseling_Requests_in_Fiscal_Year_2024_By_County.csv`

## Classes and Methods
### `ConfigLoader`
- **`load_json(file_path)`**: Loads a JSON file and returns its content as a dictionary.

### `FileManager`
- **`read_all_files()`**: Reads CSV files into pandas DataFrames.
- **`convert_to_numeric(df)`**: Converts numeric columns in DataFrames.
- **`reassign_centers(center)`**: Reassigns center names using `centers_mapping.json`.

### `DataAggregation`
- **`aggregate_and_calculate(df, groupby_col, aggr_col, transform_func, drop_duplicates, agg_func)`**: Aggregates data by the specified column.

### `GraphData`
- **`graph_horizontal_barchart(df, x, y, title, color)`**: Creates and saves horizontal bar charts.

### `ReportGenerator`
- **`report_county(file)`**: Generates county-level aggregated reports.
- **`report_center(file)`**: Generates center-level aggregated reports.
- **`report_center_omit_some(file, rename_col)`**: Omits specific centers and aggregates data.
- **`calculate_percentage(df1, df2, rename_col, df1_col, df2_col, percent)`**: Computes percentages for conversion rates.

## Example Workflow
1. Process data from `req_counseling_FY2024.csv`.
2. Aggregate by center using `report_center()`.
3. Visualize the data with `graph_horizontal_barchart()`.
4. Calculate conversion rates between `req_counseling_FY2024.csv` and `at_least_30_minutes.csv`.

## Author
**Martin De La Cruz**
