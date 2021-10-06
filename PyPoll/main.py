#Unit 3 Python Challenge--PyPoll election data

#import required modules
import csv
import os

#connect to election_data.csv file
path=os.path.join("Resources", "election_data.csv")

#variables
candidate_list= []
testdict = {}

#read csv file and store/calculate required information
with open(path) as location:
    content = csv.reader(location, delimiter=",")
    csv_header = next(content) #store csv headers
    for row in content:
        
        #The total number of votes cast
        #total_votes = total_votes + 1
        
        candidate_name = row[2]
        #A complete list of candidates who received votes      
        #if row[2] candidate name is *not in* candidate_list, add to list
        if candidate_name not in candidate_list:
           candidate_list.append(candidate_name)
           testdict[candidate_name] = 0

        # add + 1 vote to testdict candidate
        testdict[candidate_name] = testdict[candidate_name] + 1 ##syntax?        

#The percentage of votes each candidate won ***************


#The winner of the election based on popular vote. ************************


#print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
#print(f"{can1}: {can1percent}% ({can1votes})")
#print(f"{can2}: {can2percent}% ({can2votes})")
#print(f"{can3}: {can3percent}% ({can3votes})")
#print(f"{can4}: {can4percent}% ({can4votes})")
print("-------------------------")
#print(f"Winner: {winner}")
print("-------------------------")

#export a text file with the results
outpath = os.path.join("analysis", "PyPoll_output.txt")

with open(outpath, "w") as file:
    file.write ("insert results here")
    #*****************put in strings for results