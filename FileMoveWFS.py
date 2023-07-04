import os
import shutil
import logging

# Configure logging
logging.basicConfig(filename='file_move.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def move_files_with_folders(source_folder, destination_folder, file_list):
    for file_path, dest_path in file_list:
        source_file = os.path.join(source_folder, file_path)
        destination_file = os.path.join(destination_folder, dest_path)
        
        try:
            # Create the destination directory if it doesn't exist
            os.makedirs(os.path.dirname(destination_file), exist_ok=True)
            
            # Move the file
            shutil.move(source_file, destination_file)
        except FileNotFoundError as e:
            logging.error(f"Error: File '{source_file}' not found. {str(e)}")
        except shutil.Error as e:
            logging.error(f"Error: Failed to move file '{source_file}'. Reason: {str(e)}")
        except Exception as e:
            logging.error(f"Error: An unexpected error occurred while moving file '{source_file}'. Error message: {str(e)}")

# Specify the path to the input file containing source and destination folders
input_file = r'C:/Temp/FileMoveWFS/input_folders.txt'

# Read the source and destination folders from the input file
with open(input_file, 'r') as f:
    lines = f.readlines()
    source_folder = lines[0].strip()
    destination_folder = lines[1].strip()

# Specify the path to the input file containing file paths and destination paths
file_input_file = r'C:/Temp/FileMoveWFS/input_files.txt'

# Read the file list from the file input file
file_list = []
with open(file_input_file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        file_path, dest_path = line.strip().split(';')
        file_list.append((file_path, dest_path))

# Move files with the same folder and subfolder structure to the destination folder
move_files_with_folders(source_folder, destination_folder, file_list)
