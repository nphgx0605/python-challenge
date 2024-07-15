import csv
import os

# Path to the CSV file
csv_path = "/Users/phuongnguyen/python-challenge/PyBank/Resources/budget_data.csv"


# Initialize variables
total_months = 0
net_total = 0
previous_profit = None
changes = []
months = []

# Read the CSV file
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Skip the header row

    for row in csvreader:
        month, profit = row
        profit = int(profit)

        # Track total months and net total profit
        total_months += 1
        net_total += profit

        # Calculate changes in profit and store months
        if previous_profit is not None:
            change = profit - previous_profit
            changes.append(change)
            months.append(month)

        previous_profit = profit

# Calculate required values
average_change = sum(changes) / len(changes)
greatest_increase = max(changes)
greatest_decrease = min(changes)
greatest_increase_month = months[changes.index(greatest_increase)]
greatest_decrease_month = months[changes.index(greatest_decrease)]

# Print the analysis to the terminal
results = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"
)
print(results)

# Save the results to a text file
output_path = "/Users/phuongnguyen/python-challenge/PyBank/analysis/financial_analysis.txt"
with open(output_path, 'w') as textfile:
    textfile.write(results)

