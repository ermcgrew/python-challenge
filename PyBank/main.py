#Unit 3 python challenge Profit/Loss data

#import modules
import os
import csv

#connect to budget_data.csv file
path = os.path.join("Resources","budget_data.csv")

#variables for calculations
last_row_pl = 0
pl_dict = {}
total_months = 0
net = 0
sum_change = []
big_inc = 0
big_dec = 0

with open(path) as file:
    content = csv.reader(file, delimiter=',')
    csv_header = next(content)
    for row in content:

        #store profit/loss & month as variables
        current_pl = (int(row[1]))
        current_month = row[0]

        #calculate change between current row and previous row
        current_change = current_pl - last_row_pl

        #add month, p/l, change to dictionary
        pl_dict[current_month] = current_pl, current_change
        
        #save current profit/loss for next loop
        last_row_pl = current_pl
 
#total months of data 
total_months = len(pl_dict)

#loop through dictionary values
for month, values in pl_dict.items():
    net = net + values[0] #calculate total p/l
    sum_change.append(values[1]) #create list of changes for average calculation
    if values[1] >= big_inc: #find month with biggest positive change
        big_inc = values[1]
        big_inc_month = month
    if values[1] <= big_dec: #find month with biggest negative change
        big_dec = values[1]
        big_dec_month = month

#exclude the first change from 0 to first month p/l
sum_change.pop(0)
#average change
avg_change = round(((sum(sum_change))/(len(sum_change))), 2)

#print results to terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {big_inc_month} (${big_inc})") 
print(f"Greatest Decrease in Profits: {big_dec_month} (${big_dec})") 

#print results to text file
outpath = os.path.join("analysis", "PyBank_output.txt")

with open(outpath, "w") as file:
    file.write(f"Financial Analysis\n----------------------------")
    file.write(f"\nTotal Months: {total_months}\nTotal: ${net}\nAverage Change: ${avg_change}")
    file.write(f"\nGreatest Increase in Profits: {big_inc_month} (${big_inc})")
    file.write(f"\nGreatest Decrease in Profits: {big_dec_month} (${big_dec})")    