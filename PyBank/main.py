import os
import csv

#connect to budget_data.csv file
path = os.path.join("Resources","budget_data.csv")

total_months = 0

with open(path) as file:
    content = csv.reader(file, delimiter=',')
    next(content, None) #skip headers
    for row in content:
        #total number of months (count how many rows)
        total_months = total_months + 1
        #net profit/loss 


print (total_months)



