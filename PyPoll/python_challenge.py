import csv 
import os

csv_file = os.path.join("election_data.csv")

Total_Votes = 0
Total = 0

with open (csv_file,'r') as csvwrapper:
    csvreader = csv.reader(csvwrapper, delimiter=',')

    csv_header = next(csvreader)
    print(csv_header)

    for row in csvreader:
        print(row[0],row[1])
        Total_Votes += 1




print("Total Number Of Votes = " + str(Total_Votes))
