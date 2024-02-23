import pandas as pd
import matplotlib.pyplot as plt

# List of 12 months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Read the CSV file into a DataFrame
df = pd.read_csv('employee1000_salaries.csv')

# Calculate total salary for each month
monthly_totals = df[months].sum()

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(monthly_totals, labels=months, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Distribution of Total Salary Across Months')

# Save the plot as an image (e.g., PNG)
plt.savefig('total_salary_distribution_pie.png')

# Show the plot
plt.show()
