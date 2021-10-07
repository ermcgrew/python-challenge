#Unit 3 Python Challenge--PyPoll election data

#import required modules
import csv
import os

#connect to election_data.csv file
path=os.path.join("Resources", "election_data.csv")

#variables
candidate_list= []
votedict = {}

#read csv file and store/calculate required information
with open(path) as location:
    content = csv.reader(location, delimiter=",")
    csv_header = next(content) #store csv headers
    for row in content:
        candidate_name = row[2]
        #A complete list of candidates who received votes      
        if candidate_name not in votedict:#candidate_list:
           #candidate_list.append(candidate_name)
           votedict[candidate_name] = 1
        else:
        # add + 1 vote to candidate_name value
            votedict[candidate_name] = votedict[candidate_name] + 1         

#total votes using .values on votedict
values = votedict.values()
total=sum(values)

#calculate percentage of votes each candidate won & add to votedict
for key, value in votedict.items():
    votedict[key] = [value, round(((value/total) *100), 3)]

#The winner of the election based on popular vote. ************************




#check dictionary:
print(votedict)


#print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total}")
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