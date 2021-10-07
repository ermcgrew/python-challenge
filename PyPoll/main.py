#Unit 3 Python Challenge--PyPoll election data

#import required modules
import csv
import os

#connect to election_data.csv file
path=os.path.join("Resources", "election_data.csv")

#variables
candidate_list= []
votedict = {}
most_votes = 0

#read csv file and store/calculate required information
with open(path) as location:
    content = csv.reader(location, delimiter=",")
    csv_header = next(content) #store csv headers
    for row in content:
        candidate_name = row[2]
        # check for candidate_name in votedict, if not already present, add as key and +1 vote value     
        if candidate_name not in votedict:
           votedict[candidate_name] = 1
        # if candidate_name already listed in votedict, add +1 vote to value
        else:
            votedict[candidate_name] = votedict[candidate_name] + 1         

#total votes by summing all values in votedict
total=sum(votedict.values())

#calculate percentage of votes each candidate won & add to votedict as another value for each key
for name, votes in votedict.items():
    votedict[name] = [votes, round(((votes/total) *100), 3)]
    #find winner using largest vote value
    if votes >= most_votes: 
        most_votes = votes
        winner = name

#print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total}")
print("-------------------------")

for name, values in votedict.items():
    #print(f"{name}: {percent}% ({votes})")
    print(f"{name}: {values}")



print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#export a text file with the results
outpath = os.path.join("analysis", "PyPoll_output.txt")

with open(outpath, "w") as file:
    file.write ("insert results here")
    #*****************put in strings for results