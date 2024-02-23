import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('employee_salaries.csv')

# Calculate total monthly salary for each employee
df['TotalSalary'] = df.iloc[:, 1:].sum(axis=1)

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(df['Name'], df['TotalSalary'], color='skyblue')
plt.xlabel('Employee Name')
plt.ylabel('Total Monthly Salary')
plt.title('Total Monthly Salary by Employee')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
plt.tight_layout()


# Save the plot as an image (e.g., PNG)
plt.savefig('total_salary_chart.png')

# Show the plot
#plt.show()
