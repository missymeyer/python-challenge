 # Import modules 
import os
import csv

# Define variables
votes = 0
vote_count = []
candidates = []
csv_reader = ['1','2']

# Define path and open csv
csvpath = os.path.join('..', 'PyPoll','Resources', 'election_data.csv')
with open(csvpath, 'r', newline='') as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)

# Loop through the dataset and calc homework values
    for row in csv_reader:
        votes = votes + 1
        candidate = row[2]
        if candidate in candidates:
           candidate_index = candidates.index(candidate)
           vote_count[candidate_index] = vote_count[candidate_index] + 1
        else:
           candidates.append(candidate)
           vote_count.append(1)

percentages = []
most_votes = vote_count[0]
most_votes_index = 0

for count in range(len(candidates)):
    vote_percentage = vote_count[count]/votes*100
    percentages.append(vote_percentage)
    if vote_count[count] > most_votes:
        print(most_votes)
        most_votes_index = count

winner = candidates[most_votes_index]

percentages = [round (i,3) for i in percentages]

# Display output via terminal screen   
print("--------------------------------")
print("Election Results")
print("--------------------------------")
print(f"Total Votes: {votes}")
print("--------------------------------")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_count[count]})")
print("--------------------------------")
print(f"Winner:  {winner}")
print("--------------------------------") 

# Create output path
output_path = os.path.join('..', 'PyPoll','Analysis',"Election_Results.txt")
with open(output_path, 'w', newline='') as text_file:

# Write the report to a text file within the Output folder
    print("--------------------------------",file=text_file)
    print("Election Results", file=text_file)
    print("--------------------------------", file=text_file)
    print(f"Total Votes: {votes}", file=text_file)
    print("--------------------------------", file=text_file)
    for count in range(len(candidates)):
        print(f"{candidates[count]}: {percentages[count]}% ({vote_count[count]})", file=text_file)
    print("--------------------------------", file=text_file)
    print(f"Winner:  {winner}", file=text_file)
    print("--------------------------------", file=text_file) 