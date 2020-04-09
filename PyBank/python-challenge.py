import csv 
import os

csv_file = os.path.join("budget_data.csv")

Total_Months = 0
Total = 0
First_Value_YN = False
Greatest_Increase = 0
Greatest_Decrease = 99999999999999

with open (csv_file,'r') as csvwrapper:
    csvreader = csv.reader(csvwrapper, delimiter=',')

    csv_header = next(csvreader)
    print(csv_header)

    for row in csvreader:
        print(row[0],row[1])
        Total_Months += 1
        Total +=int(row[1])
        
        if First_Value_YN is False:
            First_Value = int(row[1])
            First_Value_YN = True
        else:

            Cur_Change = int(row[1]) - Last_Value
            if Cur_Change > Greatest_Increase:
                Greatest_Increase = Cur_Change
                Increase_Month = row[0]
            elif Cur_Change < Greatest_Decrease:
                Greatest_Decrease = Cur_Change
                Decrease_Month = row[0]
        Last_Value = int(row[1])

Average_Change = int(Last_Value) - int(First_Value)

output = f'''Total Months = {Total_Months}
Total Profit/Loss = ${Total}
Average Change = $ {Average_Change}
Greatest Increase = $ {Greatest_Increase}
Greatest Decrease = $ {Greatest_Decrease}
'''
print(output)
output_path = "results.txt"

with open(output_path, 'w') as txt_file:
    txt_file.write(output)