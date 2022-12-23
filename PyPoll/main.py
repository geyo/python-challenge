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

    #initialize lists
    total_votes = 0
    candidates_list = []
    previous_row = ""
    candidates_votes = {}

    # Read each row of data
    for row in csvreader:
        #count total votes
        total_votes += 1
        #add candidate to list
        if row[2] != previous_row:
            candidates_list = 
            
        
        



# print
print("Election Results")
print("-"*30)
print(f'Total Votes: {total_votes}')
print("-"*30)
print(f' {can_1}: {can_1_per} ({can_1_count})')
print(f' {can_2}: {can_2_per} ({can_2_count})')
print(f' {can_3}: {can_3_per} ({can_3_count})')
print("-"*30)
print(f'Winner: {winner}')
print("-"*30)