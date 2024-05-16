# Modules
import csv

# Set path for file
csvpath = "election_data.csv"

# variable
vote_count = 0
candidates = {}

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Read each row after the header
    for row in csvreader:
        
        # increase the vote counter by 1
        vote_count += 1

        # candidates list
        candidate = row[2]
        if candidate not in candidates:
            candidates[candidate] = [1,0]
        else:
            candidates[candidate][0] += 1

        
print("Election Results")
print(f"Total Votes: {vote_count}")

most_votes = list(candidates.values())[0][0]
# loop to get the percentage of votes for each candidate
for candidate in candidates:
    candidate_total = candidates.get(candidate)[0]
    candidates[candidate][1] = candidate_total/vote_count

    if most_votes < candidate_total:
        most_votes = candidate_total 

winner = ""
for i in range(len(list(candidates.values()))):
    if most_votes in list(candidates.values())[i]:
        winner = list(candidates.keys())[i]

for i in range(len(candidates)):
    print(f"{list(candidates.keys())[i]}: {format(list(candidates.values())[i][1], '.3%')} ({list(candidates.values())[i][0]})")

print(f"Winner: {winner}")

with open("Pypoll.txt", "w") as file:
    file.write(f"Election Results\n")
    file.write(f"Total Votes: {vote_count}\n")
    for i in range(len(candidates)):
        file.write(f"{list(candidates.keys())[i]}: {format(list(candidates.values())[i][1], '.3%')} ({list(candidates.values())[i][0]})\n")
    file.write(f"Winner: {winner}")