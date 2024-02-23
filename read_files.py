import os

# Function to read a file and extract a number
def extract_number_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            # Assuming the file contains a single number per line
            number = float(content.strip())
            return number
    except (FileNotFoundError, ValueError) as e:
        print(f"Error reading file {file_path}: {e}")
        return 0  # Return 0 if there's an error reading the file

# Function to calculate the sum of numbers in all files in a folder
def sum_numbers_in_folder(folder_path):
    total_sum = 0
    try:
        files = os.listdir(folder_path)
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                number = extract_number_from_file(file_path)
                total_sum += number
    except FileNotFoundError as e:
        print(f"Error accessing folder {folder_path}: {e}")
    return total_sum

# Specify the folder path
folder_path = 'data'

# Calculate the sum of numbers in all files in the folder
result = sum_numbers_in_folder(folder_path)

# Print the result
print(f"Sum of numbers in all files: {result}")
