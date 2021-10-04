import os
import csv

#connect to budget_data.csv file
path = os.path.join("Resources","budget_data.csv")

with open(path) as file:
    content = csv.reader(file, delimiter=',')
    print(f"this worked {content}")



