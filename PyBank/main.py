#Unit 3 python challenge Profit/Loss data

#import modules
import os
import csv

#connect to budget_data.csv file
path = os.path.join("Resources","budget_data.csv")

#variables for calculations
total_months = 0
net = 0
last_row = 0
sum_change = 0
big_inc = 0
big_dec = 0

with open(path) as file:
    content = csv.reader(file, delimiter=',')
    next(content, None) #skip headers
    for row in content:
        #total number of months (count how many rows)
        total_months = total_months + 1
        
        #store profit/loss as integer variable 
        pl = (int(row[1]))

        #net profit/loss 
        net = net + int(row[1])
        
        #change between current row and previous row***********************
        current_change = (int(row[1])) - (last_row)
        #if

        #sum of change between each row for average change calculation
        sum_change = sum_change + current_change

        #save current profit/loss for next loop
        last_row = int(row[1])

        #check for bigger increase & store month
        if current_change >= big_inc:
            big_inc = current_change
            big_inc_month = row[0]
        
        #check for bigger decrease & store month
        if current_change <= big_dec:
            big_dec = current_change
            big_dec_month = row[0]

#average change = change between each row divided by number of rows
avg_change = round(sum_change/int(total_months), 2)

#print results to terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {big_inc_month} (${big_inc})") 
print(f"Greatest Decrease in Profits: {big_dec_month} (${big_dec})") 

#print results to text file***************