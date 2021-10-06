#Unit 3 Python Challenge--PyPoll election data

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
candidate_list= []
testdict = {}

#read csv file and store/calculate required information
with open(path) as location:
    content = csv.reader(location, delimiter=",")
    csv_header = next(content) #store csv headers
    for row in content:
        
        #The total number of votes cast
        total_votes = total_votes + 1
        
        #A complete list of candidates who received votes      
        #if row[2] candidate name is *not in* candidate_list, add to list
        #if row[2] not in candidate_list:
         #   candidate_list.append(row[2])
        
        

        #if row[2] not in testdict:
           # testdict["cand1"] = row[2]

        for name in candidate_list:
            testdict[name] = eval(name)

        
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


#print (candidate_list)
print(testdict)
#The percentage of votes each candidate won


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