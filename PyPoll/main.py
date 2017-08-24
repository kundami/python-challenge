#pypoll
# Dependencies
# --------------------------------------
import csv

# Files to Load / Output
# --------------------------------------
file_to_load = "Resources/election_data_2.csv"
file_to_output = "Output/election_analysis_2.txt"

# Variables to Track
# --------------------------------------
# [{"Khan": 5}, {"Li": 2}, {"Correy": 70}]
candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0

total_votes = 0

greatest_vote_candidate = ""
greatest_vote_percentage = 0

# Main Process 
# --------------------------------------
# Reading the file
with open(file_to_load) as election_data:
  reader = csv.DictReader(election_data)

  # For Each row...
  for row in reader:

    # Total Votes
    total_votes = total_votes + 1

    # Build our Array of Unique Candidates 
    if row["Candidate"] not in candidate_options:

      # Add the candidate as an option
      candidate_options.append(row["Candidate"])

      # Set that candidate's initial vote count to 0
      candidate_votes[row["Candidate"]] = 0

    # If the candidate is NOT unique
    candidate_votes[row["Candidate"]] =  candidate_votes[row["Candidate"]] + 1

  # Iterate through the candidate_votes
  for candidate in candidate_votes:

    votes = candidate_votes[candidate]
    vote_percentage = (votes / total_votes)  * 100
    print(votes)
    print(total_votes)
    print("-----------------")
    print(vote_percentage)
    print("-----------------")

    if(vote_percentage > greatest_vote_percentage):

      greatest_vote_candidate = candidate
      greatest_vote_percentage = vote_percentage

  # Printing The Winner
  print("The winning candidate is " + greatest_vote_candidate)
  print("The greatest vote percentage is: " + str(greatest_vote_percentage))
      