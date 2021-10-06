#Python Challenge--PyPoll

import csv
import os

path=os.path.join("Resources", "election_data.csv")

#variables
total_votes= 0

with open(path) as location:
    content = csv.reader(location, delimiter=",")
    next(content, None) #skip headers
    for row in content:
        total_votes = total_votes + 1


print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
#  Khan: 63.000% (2218231)
 # Correy: 20.000% (704200)
  #Li: 14.000% (492940)
  #O'Tooley: 3.000% (105630)
print("-------------------------")
print(f"Winner: ") #create variable
print("-------------------------")
    







#The total number of votes cast
#A complete list of candidates who received votes
# The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.


#print the analysis to the terminal

#export a text file with the results