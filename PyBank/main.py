#Unit 3 python challenge Profit/Loss data

#import modules
import os
import csv

#connect to budget_data.csv file
path = os.path.join("Resources","budget_data.csv")

#variables for calculations
total_months = 0
net = 0
last_row_pl = 0
sum_change = []
big_inc = 0
big_dec = 0

with open(path) as file:
    content = csv.reader(file, delimiter=',')
    next(content, None) #skip headers ***********rubric says "store", is this ok?
    for row in content:
        #total number of months (count how many rows)
        total_months = total_months + 1
        
        #store profit/loss as integer variable 
        current_pl = (int(row[1]))

        #net profit/loss 
        net = net + current_pl
        
        #change between current row and previous row
        current_change = current_pl - last_row_pl

        #sum of change between each row for average change calculation
        sum_change.append(current_change)    

        #save current profit/loss for next loop
        last_row_pl = current_pl

        #check for bigger increase & store month
        if current_change >= big_inc:
            big_inc = current_change
            big_inc_month = row[0]
        
        #check for bigger decrease & store month
        if current_change <= big_dec:
            big_dec = current_change
            big_dec_month = row[0]

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

#print results to text file***************this is an ugly way, save what prints to terminal in a list?
outpath = os.path.join("analysis", "PyBank_output.txt")

with open(outpath, "w") as file:
    file.write(f"Financial Analysis\n----------------------------\nTotal Months: {total_months}\nTotal: ${net}\nAverage Change: ${avg_change}\nGreatest Increase in Profits: {big_inc_month} (${big_inc})\nGreatest Decrease in Profits: {big_dec_month} (${big_dec})")    