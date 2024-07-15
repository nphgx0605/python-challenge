import csv
import os

csv_path = "/Users/phuongnguyen/python-challenge/PyPoll/Resources/election_data.csv"

# Initialize Variables
total_votes = 0 
candidates = []
candidate_votes = {}
winner = ""
winner_votes = 0

# Read the csv file
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        total_votes +=1
        candidate = row[2]

        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes [candidate] = 0
        candidate_votes [candidate] += 1

# Calculate percentages and determine the winner
results = ""
for candidate in candidates:
    votes = candidate_votes[candidate]
    vote_percentage = (votes/ total_votes) * 100
    results += f"{candidate}: {vote_percentage:.3f}% ({votes})\n"

    if votes > winner_votes:
        winner_votes = votes
        winner = candidate

# Print analysis
results_summary = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
    f"{results}"
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)
print(results_summary)

# Save the results to a text file
output_path = os.path.join('/Users/phuongnguyen/python-challenge/PyPoll/analysis', 'election_results.txt')
with open(output_path, 'w') as textfile:
    textfile.write(results_summary)