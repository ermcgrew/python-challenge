import os
import csv

#connect to budget_data.csv file
path = os.path.join("Resources","budget_data.csv")

total_months = 0
net = 0
last_row = 0

with open(path) as file:
    content = csv.reader(file, delimiter=',')
    next(content, None) #skip headers
    for row in content:
        #total number of months (count how many rows)
        total_months = total_months + 1
        #net profit/loss 
        net = net + int(row[1])
        #average change = change between each row divided by number of rows
        last_row = int(row[1])
        avg_change = last_row + int(row[1])

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: ") #name variable
print(f"Greatest Decrease in Profits: ") #name variable