#Python Challenge--PyPoll

#import required modules
import csv
import os

#connect to election_data.csv file
path=os.path.join("Resources", "election_data.csv")

#variables
total_votes= 0 
can1 = "Khan"
can2 = "Correy"
can3 = "Li"
can4 = "O'Tooley"
can1votes = 0 
can2votes = 0
can3votes = 0
can4votes = 0

#read csv file and store/calculate required information
with open(path) as location:
    content = csv.reader(location, delimiter=",")
    csv_header=next(content)
    for row in content:
        
        #The total number of votes cast
        total_votes = total_votes + 1
       
        currentcan=row[2]
        #The total number of votes each candidate won
        if currentcan == can1:
            can1votes = can1votes + 1
        elif currentcan == can2:
            can2votes = can2votes + 1
        elif currentcan == can3:
            can3votes = can3votes + 1
        else:
            can4votes = can4votes + 1

#The percentage of votes each candidate won
can1percent = round((can1votes/total_votes) * 100, 3)
can2percent = round((can2votes/total_votes) * 100, 3)
can3percent = round((can3votes/total_votes) * 100, 3)
can4percent = round((can4votes/total_votes) * 100, 3)

#The winner of the election based on popular vote
if can1votes >= can2votes and can1votes >= can3votes and can1votes >= can4votes:
    winner = can1
elif can2votes >= can1votes and can2votes >= can3votes and can2votes >= can4votes:
    winner = can2
elif can3votes >= can1votes and can3votes >= can2votes and can3votes >= can4votes:
    winner = can3
else:
    winner = can4

#print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"{can1}: {can1percent}% ({can1votes})")
print(f"{can2}: {can2percent}% ({can2votes})")
print(f"{can3}: {can3percent}% ({can3votes})")
print(f"{can4}: {can4percent}% ({can4votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#export a text file with the results
outpath = os.path.join("analysis", "PyPoll_output.txt")

with open(outpath, "w") as file:
    file.write (f"Election Results\n-------------------------\nTotal Votes: {total_votes}\n-------------------------\n{can1}: {can1percent}% ({can1votes})\n{can2}: {can2percent}% ({can2votes})\n{can3}: {can3percent}% ({can3votes})\n{can4}: {can4percent}% ({can4votes})\n-------------------------\nWinner: {winner}\n-------------------------")
