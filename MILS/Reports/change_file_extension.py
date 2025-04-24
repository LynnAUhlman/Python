import os
import glob

def change_file_extension(directory, old_ext, new_ext):
    # Get all files with the old extension in the directory
    files = glob.glob(os.path.join(directory, f"*{old_ext}"))

    # Log the number of files found
    print(f"Found {len(files)} {old_ext} files in {directory}")

    if not files:
        print(f"No {old_ext} files found.")
        return

    for file in files:
        # Define the new file name
        new_file = file[:-len(old_ext)] + new_ext

        # Rename the file
        os.rename(file, new_file)
        print(f"Renamed {file} to {new_file}")

# Specify the directory containing the files
directory = r"G:\Shared drives\MILS -- MIN\Bib Counts\202503"
old_extension = ".xls"
new_extension = ".txt"

change_file_extension(directory, old_extension, new_extension)

