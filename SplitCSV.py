import os
import pandas as pd

def split_csv(input_file, rows_per_file, output_folder):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Output folder '{output_folder}' created.")

    chunk_size = rows_per_file  # Number of rows per split file
    print(f"Reading {input_file} in chunks of {chunk_size} rows each...")

    # Create an iterator that reads the input file in chunks
    reader = pd.read_csv(input_file, chunksize=chunk_size)

    # Iterate through each chunk and write it to a new CSV file in the output directory
    for i, chunk in enumerate(reader):
        output_file = os.path.join(output_folder, f'output_part_{i+1}.csv')
        print(f"Writing chunk {i+1} to {output_file}...")
        chunk.to_csv(output_file, index=False)
        print(f'{output_file} created successfully.')

    print("CSV file has been split successfully.")

# Example usage
input_file = r'[insert file path]'  # Adjust to the large file path
rows_per_file = 10000  # Adjust the number of rows per file
output_folder = r'[insert file path]'  # Adjust to the desired output folder path


print(f"Starting to split {input_file} into smaller files in the folder '{output_folder}'...")
split_csv(input_file, rows_per_file, output_folder)
print("Process completed.")


