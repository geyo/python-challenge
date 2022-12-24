# Import dependencies
# OS helps us create a filepath across operating systems. 
# CSV is a module for reading csv files. 
import os
import csv

# Path to collect budget data from Resources folder
csvpath = os.path.join("Resources", "election_data.csv")

# CSV reader specifies delimiter and variable that holds contents
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # skip the header
    header = next(csvreader)

    #initialize variables 
    total_votes = 0
    candidates_dict = {}
    candidate_list = []
  
    # Read each row of data
    for row in csvreader:
        #count total votes
        total_votes += 1
        #count votes for candidates
        #if candidate is in dictionary, add 1 to their vote. 
        if row[-1] in candidates_dict:
            candidates_dict[row[-1]] += 1
        #otherwise, add them to dictionary, and add 1 to their vote
        else: 
           candidates_dict.update({row[-1]: 1})
           #candidate_list.append(row[2])

    #assign and dictionary to list, and find % of votes
    candidate_list = list(candidates_dict.keys())
    
    can_1 = candidate_list[0]
    can_1_count = candidates_dict[can_1]
    can_1_per = round((can_1_count / total_votes) * 100, 3)

    can_2 = candidate_list[1]
    can_2_count = candidates_dict[can_2]
    can_2_per = round((can_2_count / total_votes) * 100, 3)

    can_3 = candidate_list[2]
    can_3_count = candidates_dict[can_3]
    can_3_per = round((can_3_count / total_votes) * 100, 3)

    #find winner by using a max value applied to a dictionary
    winner = max(candidates_dict, key=candidates_dict.get)

# print message
msg = f"""
Election Results
------------------------------
Total Votes: {total_votes}
------------------------------
{can_1}: {can_1_per}% ({can_1_count})
{can_2}: {can_2_per}% ({can_2_count})
{can_3}: {can_3_per}% ({can_3_count})
------------------------------
Winner: {winner}
------------------------------
"""
print(msg)

#export results to terminal
f = open("Analysis/results.txt","w")
f.write(msg)