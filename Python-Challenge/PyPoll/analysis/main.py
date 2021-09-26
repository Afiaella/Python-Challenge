import os
import csv

csvpath = os.path.join("..","Resources", "election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    print(f"CSV Header: {csv_header}")

    total_number_votes = 0
    list_candidates = 0
    candidates_percentage = 0
    total_votes_candidates = 0
    winner = ""

    for row in csvreader:
        total_number_votes = total_number_votes + 1



    