
import os
import csv
months_count = 0
profit_Loss_sum = 0
profit_loss_change = 0
months_change = []
prev_profit_loss = 0
profit_loss_change_list = []
greatest_increase = []
greatest_decrease = []

csvpath = os.path.join("Resources", "budget_data.csv")
# print(os.path.abspath(csvpath))
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        months_count = months_count + 1
        print(row[1])
        profit_Loss_sum = profit_Loss_sum + int(row[1])

    print(months_count)
    print(profit_Loss_sum) 
   
    
    profit_loss_change = int(row[1]) - prev_profit_loss
    prev_profit_loss = int(row[1])
    profit_loss_change_list = profit_loss_change_list + [profit_loss_change]
    months_change = months_change + (row[2])

    if(profit_loss_change > greatest_increase[1]):
        greatest_increase[0] = row[2]
        greatest_increase[1] = profit_loss_change

if(profit_loss_change < greatest_decrease[1]):
    greatest_decrease[0] = row[2]
    greatest_decrease[1] = profit_loss_change 







   







