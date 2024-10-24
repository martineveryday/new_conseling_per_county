# Author: Martin De La Cruz

import pandas as pd
import matplotlib.pyplot as plt


filenames = ['ecenter.csv', 'clients.csv', 'step4_data.csv']

def clean_numeric_columns(df):
    """
    Convert columns containing 'Total' in their name from strings to numeric values.
    """
    for col in df.columns:
        if 'Total' in col and df[col].dtype == 'object':
            df[col] = pd.to_numeric(df[col].str.replace(',', ''), errors='coerce')

def read_all_files(filenames):
    """
    Read all CSV files from the provided filenames and clean numeric columns.
    """
    dfs = {name: pd.read_csv(name) for name in filenames}
    for df in dfs.values():
        clean_numeric_columns(df)
    return dfs

def merge_dfs_with_cleanup(df1, df2, col, join_type='inner', drop_dup_col=None, rename_cols=None):
    """
    Merge two dataframes on the specified column, optionally remove duplicates, and rename columns.
    """
    merged_df = pd.merge(df1, df2, how=join_type, on=col)
    if drop_dup_col:
        merged_df.drop_duplicates(subset=drop_dup_col, inplace=True)
    if rename_cols:
        merged_df.rename(columns=rename_cols, inplace=True)
    return merged_df

def clean_county_name(county):
    """
    Clean up county names by removing '(shared)' and any spaces.
    """
    return county.replace("(shared)", "").replace(" ", "")

def graph_results(final_df):
    """
    Graph the results of the final data frame on a bar chart .
    """
    plt.figure(figsize=(10, 6))
    plt.bar(final_df['Physical Address County'], final_df['Penetration Rate Per County'])
    plt.xticks(rotation=90)
    plt.title('Counseling Penetration Rate for Business in PA in Fiscal Year 2024')
    plt.xlabel('County')
    plt.ylabel('Number of Businesses Helped')
    plt.tight_layout()
    return plt.show()

dfs = read_all_files(filenames)
df_client, df_ecenter, df_step4 = dfs['clients.csv'], dfs['ecenter.csv'], dfs['step4_data.csv']

merged_df = merge_dfs_with_cleanup(df_client, df_ecenter, 'Client', drop_dup_col='Client')

clients_by_county = merged_df.groupby(['Physical Address County'])['Client'].count().reset_index()
clients_by_county.rename(columns={'Client': 'Number of Businesses Helped'}, inplace=True)


df_step4['Physical Address County'] = df_step4['Physical Address County'].apply(clean_county_name)
bus_per_county = df_step4[['Physical Address County', 'Total']].drop_duplicates()


final_df = merge_dfs_with_cleanup(
    clients_by_county, 
    bus_per_county, 
    'Physical Address County', 
    rename_cols={'Total': 'Total Business Per County'}
)
final_df['Penetration Rate Per County'] = final_df['Number of Businesses Helped'] / final_df['Total Business Per County']
final_df['Penetration Rate Per County %'] = final_df['Penetration Rate Per County'].apply(lambda x: f'{x * 100: .2f}%')
final_df.dropna(inplace=True)


graph_results(final_df)
final_df.to_csv('Counseling Penetration Rate for Business in PA in Fiscal Year 2024.csv')

