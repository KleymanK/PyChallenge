import csv 
import os

csv_file = os.path.join("election_data.csv")

# initialize values
Total_Votes = 0
candidates_list =[]
vote_dict = {}

# GET TOTAL votes
# get total votes by candidates
# get list of candidates
# get percentage by candidate
# get winner

with open (csv_file,'r') as csvwrapper:
    csvreader = csv.reader(csvwrapper, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:
        Total_Votes += 1

        candidate = row[2]

        if candidate in candidates_list:
            # add a vote to this candidate's vote count
            vote_dict[candidate] +=1
        else:
            candidates_list.append(candidate)
            vote_dict[candidate] = 1



print("Total_Votes = " + str(Total_Votes))
print(f"Candidates are: {candidates_list}")
