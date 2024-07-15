import csv
import os

# Path to the CSV file
csv_path = os.path.join("/Users/phuongnguyen/python-challenge/PyBank/Resources/budget_data.csv")


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

# Displaying results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Save the results to a text file
output_path = "/Users/phuongnguyen/python-challenge/PyBank/analysis/financial_analysis.txt"
with open(output_path, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("----------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${net_total}\n")
    txt_file.write(f"Average Change: ${average_change:.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")

