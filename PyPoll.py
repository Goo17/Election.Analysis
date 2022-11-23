# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1 Initialize a total vote counter 
total_votes = 0

# Candidate Options
candidate_options = []

# Candidate Dict
candidate_votes = {}

# Winning Candidate and Winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2 Add to the total vote count
        total_votes += 1
        
        # print the canidate name
        candidate_name = row[2]

        # If the canidate does not match any existing canidate
        if candidate_name not in candidate_options:
            
            # Add the canidate name to the list
            candidate_options.append(candidate_name)

            # 2 Begin tracking that canidates vote
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes per candidate

# Iterate through the candidate list
for candidate_name in candidate_votes:
    #retrieve vote count for each candidate
    votes = candidate_votes[candidate_name]
    #calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    #print candidate name and percentage of votes
    print(f"{candidate_name}: {votes} ({vote_percentage:.1f}%)")

# Dertermine if the vote count and candidate
# 1 Determine if the votes are greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #if true then set  winning_count = votes and winning percent =
        #vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # Set the winning_candidate equal to the candidate's name
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"------------------------\n")

print(winning_candidate_summary)