import os
import random

# Function to generate a random number between 3000 and 6000
def generate_random_number():
    return random.uniform(3000, 6000)

# Function to create a text file with a random number
def create_text_file(file_path):
    number = generate_random_number()
    with open(file_path, 'w') as file:
        file.write(str(number))

# Function to create 50 text files with random numbers and store them in a data folder
def create_and_store_files(folder_path, num_files=50):
    try:
        # Create the data folder if it doesn't exist
        os.makedirs(folder_path, exist_ok=True)
        
        # Create and store 50 text files
        for i in range(1, num_files + 1):
            file_name = f"file_{i}.txt"
            file_path = os.path.join(folder_path, file_name)
            create_text_file(file_path)
            print(f"File {file_name} created with a random number.")

    except Exception as e:
        print(f"Error: {e}")

# Specify the data folder path
data_folder_path = 'data'

# Create and store 50 text files in the data folder
create_and_store_files(data_folder_path)
