# Modules
import csv

# Set path for file
csvpath = "budget_data.csv"

# variable
month_count = 0
total_profit = 0

# for changes
last_month_profit = 0
changes = []
month_changes = []

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)  

        # count months
        month_count += 1
        
        # add profit
        total_profit += int(row[1])

        # last month profits
        # subtract this month profit - last month profit
        # APPEND that change to the list
    
        # If first row, there is no change
        if (month_count == 1):
                # by definition, this is the first row
                # no change
            last_month_profit = int(row[1])
        else:
            change = int(row[1]) - last_month_profit
            changes.append(change)
            month_changes.append(row[0])

            # reset last month profit
            last_month_profit = int(row[1])


print(month_count)
print(total_profit)
print(len(changes))

avg_change = sum(changes) / len(changes)
print(avg_change)

max_change = max(changes)
max_month_index = changes.index(max_change)
max_month = month_changes[max_month_index]

print(max_change)
print(max_month)

min_change = min(changes)
min_month_index = changes.index(min_change)
min_month = month_changes[min_month_index]

print(min_change)
print(min_month)
