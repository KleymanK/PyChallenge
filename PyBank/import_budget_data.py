import csv

with open('budget_data.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)
    
    
    for row in csv_reader:
        
        print(row[-1])