import os
import csv

#connect to budget_data.csv file
path = os.path.join("Resources","budget_data.csv")

total_months = 0
net = 0
last_row_change = 0
big_inc = 0
big_dec = 0

with open(path) as file:
    content = csv.reader(file, delimiter=',')
    next(content, None) #skip headers
    for row in content:
        #total number of months (count how many rows)
        total_months = total_months + 1
        
        #net profit/loss 
        net = net + int(row[1])
        
        #sum of change between each row for average change calculation
        sum_change = last_row_change + int(row[1])
        last_row_change = int(row[1])

        #check for bigger increase & store month
        if int(row[1]) >= big_inc:
            big_inc = int(row[1])
            big_inc_month = row[0]
        
        #check for bigger decrease & store month
        if int(row[1]) <= big_dec:
            big_dec = int(row[1])
            big_dec_month = row[0]

#average change = change between each row divided by number of rows
avg_change = round(sum_change/int(total_months), 2)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {big_inc_month} (${big_inc})") 
print(f"Greatest Decrease in Profits: {big_dec_month} (${big_dec})") 