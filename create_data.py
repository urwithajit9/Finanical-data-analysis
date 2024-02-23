"""
This script generates random monthly salaries for 50 employees and writes them to a CSV file named `employee_salaries.csv`. 
You can modify the `csv_filename` variable to choose a different filename.
"""
import csv
import random

employee_count =100
employee_names = [f"Employee_{i+1}" for i in range(employee_count)]
# List of 12 months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
csv_filename = f'employee{employee_count}_salaries.csv'



# Write data to CSV file
filep = open(csv_filename, mode='w', newline='')
writer = csv.writer(filep)
# Write header
writer.writerow(['Name'] + [month for month in months])
for i in range(employee_count):  
    salary = [random.randint(4000, 6000) for _ in range(12)] 
    data = [employee_names[i]]+salary
    print(data)     
    # Write data
    writer.writerow(data)
filep.close()    
print(f"CSV file '{csv_filename}' created successfully.")
