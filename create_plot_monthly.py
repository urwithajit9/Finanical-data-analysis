import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('employee1000_salaries.csv')

# Calculate total salary for each month
monthly_totals = df.iloc[:, 1:].sum()

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(monthly_totals.index, monthly_totals.values, color='skyblue')
plt.xlabel('Month')
plt.ylabel('Total Salary')
plt.title('Total Salary by Month')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
plt.tight_layout()

# Save the plot as an image (e.g., PNG)
plt.savefig('total_salary_by_month.png')

# Show the plot
#plt.show()
