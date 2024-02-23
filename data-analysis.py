import csv

def read_csv(filename):
    # Read data from CSV file
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        # Skip header
        next(reader, None)
        # Read data into a dictionary
        data = {row[0]: list(map(int, row[1:])) for row in reader}
    return data

def calculate_total_salary(data):
    # Calculate total salary for each employee
    total_salaries = {name: sum(salaries) for name, salaries in data.items()}
    #print(total_salaries)
    return total_salaries

def main():
    # Specify the CSV filename
    csv_filename = 'employee100_salaries.csv'

    # Read CSV file
    data = read_csv(csv_filename)

    # Calculate total salary for each employee
    total_salaries = calculate_total_salary(data)

    # Print total salaries
    for name, total_salary in total_salaries.items():
        print(f"{name}: ${total_salary}")

if __name__ == "__main__":
    main()
