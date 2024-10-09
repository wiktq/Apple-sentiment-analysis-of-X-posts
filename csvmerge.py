import os
import pandas as pd

# Define the directory where your CSV files are located
directory = "/Users/wiktoria/Documents/master/Master thesis/March 5, 2010"  # Replace with your actual path

# Define the output file path
output_file = "March_5_2010_merged.csv"  # You can change the output filename if needed

# Get the list of CSV files in the directory
csv_files = sorted([file for file in os.listdir(directory) if file.endswith(".csv")])

# Initialize a list to store dataframes
dfs = []

# Loop through the CSV files and append them
for idx, file in enumerate(csv_files):
    file_path = os.path.join(directory, file)
    
    if idx == 0:
        # For the first file, include the header
        df = pd.read_csv(file_path)
    else:
        # For subsequent files, skip the header
        df = pd.read_csv(file_path, header=0)
    
    dfs.append(df)

# Concatenate all dataframes
merged_df = pd.concat(dfs, ignore_index=True)

# Save the merged dataframe to a new CSV file
merged_df.to_csv(os.path.join(directory, output_file), index=False)

print(f"CSV files merged into {output_file}")
