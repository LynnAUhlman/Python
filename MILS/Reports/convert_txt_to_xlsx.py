import pandas as pd
import os

def txt_to_xlsx(txt_file, xlsx_file):
    # Read the .txt file into a DataFrame
    df = pd.read_csv(txt_file, delimiter='\t')  # Adjust delimiter if needed

    # Write the DataFrame to an .xlsx file
    df.to_excel(xlsx_file, index=False)

    print(f"Converted {txt_file} to {xlsx_file}")

def batch_update_txt_to_xlsx(input_directory, output_directory):
    # List all .txt files in the input directory
    txt_files = [f for f in os.listdir(input_directory) if f.endswith('.txt')]

    # Log the number of .txt files found
    print(f"Found {len(txt_files)} .txt files in {input_directory}")

    if not txt_files:
        print(f"No .txt files found in {input_directory}.")
        return

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Convert each .txt file to .xlsx
    for txt_file in txt_files:
        # Define the paths for input and output files
        txt_path = os.path.join(input_directory, txt_file)
        xlsx_file = os.path.join(output_directory, os.path.splitext(txt_file)[0] + '.xlsx')
        
        # Convert .txt to .xlsx
        txt_to_xlsx(txt_path, xlsx_file)

# Specify the input directory containing the .txt files
input_directory = r"G:\Shared drives\MILS -- MIN\Statistics\2024\FLIP"

# Specify the output directory for the .xlsx files
output_directory = r"G:\Shared drives\MILS -- MIN\Statistics\2024\OUTPUT"

batch_update_txt_to_xlsx(input_directory, output_directory)

