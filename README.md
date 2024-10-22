# Data Cleaning and Normalization Script

## Overview

This script is designed to clean, merge, and normalize data from multiple CSV files. It is specifically tailored to handle datasets related to business information by county, ensuring the data is properly cleaned and ready for analysis. The main goal of the program is to provide a simplified and accurate representation of how many businesses have been helped in each county, relative to the total number of businesses present. 

The script automatically handles cleaning numeric columns, removing redundant spaces and shared indicators from county names, and merging datasets to calculate various normalized values (e.g., min-max normalization and z-scores). By using this script, you can quickly prepare your datasets for further analysis, ensuring data integrity and consistency.

## Features

- **Automatic Data Cleaning**: Ensures that columns containing numbers are properly formatted, removing commas and other non-numeric characters.
- **County Name Cleanup**: Cleans up county names by removing unwanted terms like "(shared)" and unnecessary spaces.
- **Merge and Deduplication**: Combines datasets based on shared fields and removes any duplicate entries.
- **Normalization Calculations**: The script calculates multiple normalized metrics:
  - **Normalized Ratio**: Number of businesses helped divided by the total businesses per county.
  - **Min-Max Normalization**: Scales the normalized ratio between 0 and 1.
  - **Z-Score**: Provides the standardized z-score of the normalized ratio.

## Prerequisites

- **Python 3.x**: Make sure you have Python installed on your system.
    - pandas 2.2.3
- **Pandas Library**: The script uses the `pandas` library to handle the data. If you don’t have it installed, you can i

## How to Use
Place CSV Files: Ensure that the three required CSV files (clients.csv, ecenter.csv, and step4_data.csv) are in the same folder as the script.
Run the Script: Simply run the Python script, and it will generate the normalized data for further analysis.
Review the Output: The output will include a cleaned and merged dataset with calculated normalized values. You can use this data for reporting or further analysis.

## Files Used
clients.csv: Contains data about clients and their county information.
ecenter.csv: Provides additional information about the clients.
step4_data.csv: Includes the total number of businesses per county, used for normalization.
Example Output
After running the script, you will get a table that shows:

* Physical Address County: The county where businesses are located.
* Number of Businesses Helped: How many businesses have been assisted in that county.
* Total Business Per County: The total number of businesses in each county.
* Normalized: The ratio of businesses helped compared to the total businesses in the county.
* Min-Max Normalized: A normalized score scaled between 0 and 1.
* Z-Score: A standardized score based on the mean and standard deviation of the normalized values.

## Author

**Martin De La Cruz**

This script was created to streamline data cleaning and analysis, helping users focus on insights rather than data preparation.h
  pip install pandas
