import os
import pandas as pd

# Define paths for each 15-day occurrence (example)
occurrences = {
    "occurrence_1": ["aug_17_2011.csv", "aug_18_2011.csv", "aug_19_2011.csv", "aug_20_2011.csv", "aug_21_2011.csv", 
                     "aug_22_2011.csv", "aug_23_2011.csv", "aug_24_2011.csv", "aug_25_2011.csv", "aug_26_2011.csv", 
                     "aug_27_2011.csv", "aug_28_2011.csv", "aug_29_2011.csv", "aug_30_2011.csv", "aug_31_2011.csv"],
    # Add other occurrences here (e.g. occurrence_2, etc.)
}

# Directory where your CSV files are located
directory = "/Users/wiktoria/Documents/master/Master\ thesis/August\ 24\,\ 2011\ -\ Steve\ Jobs\ resignation\ copy "

# Function to merge CSVs for each occurrence
def merge_csvs(files, output_file):
    dataframes = []
    for file in files:
        path = os.path.join(directory, file)
        if os.path.exists(path):
            df = pd.read_csv(path)
            dataframes.append(df)
        else:
            print(f"File {file} not found!")
    
    merged_df = pd.concat(dataframes, ignore_index=True)
    merged_df.to_csv(output_file, index=False)
    print(f"CSV files merged into {output_file}")

# Merge CSVs for each occurrence
for occurrence, files in occurrences.items():
    output_file = f"{occurrence}_merged.csv"
    merge_csvs(files, output_file)
