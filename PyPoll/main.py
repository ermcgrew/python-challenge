#Python Challenge--PyPoll

#import required modules
import csv
import os

#connect to election_data.csv file
path=os.path.join("Resources", "election_data.csv")

#variables
total_votes= 1 #set to one since first row read outside for loop
can1 = ""
can2 = ""
can3 = ""
can4 = ""
can1votes = 1 #set to one since first row read outside for loop
can2votes = 0
can3votes = 0
can4votes = 0

#read csv file and store/calculate required information
with open(path) as location:
    content = csv.reader(location, delimiter=",")
    next(content, None) #skip headers
    #store first row as list
    first_row=next(content)
    #extract first candidate name from first row
    can1=first_row[2]
    print (can1)
    for row in content:
        
        #The total number of votes cast
        total_votes = total_votes + 1
        
        #A complete list of candidates who received votes
        if row[2] == can1:
             #  can2=row[2]
             can1votes = can1votes + 1 
            
        #elif row[2] = 
             #   row[2] 
        
        #The percentage of votes each candidate won
        #The total number of votes each candidate won


#The winner of the election based on popular vote.



#print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"{can1}: ({can1votes})")
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
print("-------------------------")
print(f"Winner: ") #create variable
print("-------------------------")

#export a text file with the results