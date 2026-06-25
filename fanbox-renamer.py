import os
import re
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description="Rename image files in a directory")
parser.add_argument("directory", help="Path to the directory containing image files")

# Parse the arguments
args = parser.parse_args()

# Get the directory from the arguments
directory = args.directory

# Define the pattern for the filenames
pattern = r'(\d{2})\s*-\s*(\d{2})'

# Check if the directory exists
if not os.path.isdir(directory):
    print(f"The directory {directory} does not exist.")
else:
    # Loop through the files in the specified directory
    for filename in os.listdir(directory):
        # Check if the filename matches the pattern
        match = re.search(pattern, filename)
        if match:
            # Extract the number you want to keep
            number = match.group(1)
            # Create the new filename
            new_filename = f"{number}{os.path.splitext(filename)[1]}"
            # Get the full paths
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed: {filename} -> {new_filename}")
