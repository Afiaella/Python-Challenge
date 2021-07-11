import os
import csv

csvpath = os.path.join("Python-Challenge", "PyBank","Resources", "budget_data.csv")
print(os.path.abspath(csvpath))
with open(csvpath) as csvfile: 
 csvreader = csv.reader(csvfile, delimiter=",") 
 print(csvreader)

 csv_header =next(csvreader)
 print(f"CSV Header: {csv_header}")

 for row in csvreader:
     print(row)
csvreader:('Date').count 




