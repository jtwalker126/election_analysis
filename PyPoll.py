# The data we need to retrieve and report
# 1. Total number of votes cast
# 2. Complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. Declare a winner of the election based on popular vote.

# Pseudocode
# Create list of all candidates receiving votes
# Tally total number of votes
# count votes correspond to each candidate
# calculate percentages
# declare winner based on highest percentage

import csv
import os

# Assign variable for the file to load from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize variables
total_votes=0
candidate_options=[]
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0


#Open election results and read the file
with open(file_to_load, 'r') as election_data:

    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    
    #Print each row in the CSV file
    for row in file_reader:
        #Calculate total vote count
        total_votes += 1

        #call candidate name for each row
        candidate_name=row[2]

        if candidate_name not in candidate_options:
            #Add candidate name to the candidate list
            candidate_options.append(candidate_name)
            #Add candidate to vote dictionary and start with 0 votes
            candidate_votes[candidate_name] = 0

        #add vote to appropriate candidate
        candidate_votes[candidate_name] += 1

    #Save the results to text file
    with open(file_to_save, 'w') as txt_file:
        
        #Print final vote count to terminal
        election_results = (
            f"\nElection Results\n"
            f"----------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"----------------------------\n")
        print(election_results, end="")

        # Save the final vote count to the text file
        txt_file.write(election_results)

        for candidate in candidate_votes:  
            #retrieve vote count for each candidate
            votes = candidate_votes[candidate]
            #calculate percentage
            vote_percentage = float(votes) / float(total_votes) * 100

            #store candidate name, vote percentage, and votes 
            candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

            #Print candidate results
            print(candidate_results)
            #Save the candidate results to text file
            txt_file.write(candidate_results)

            # Determine the winning count, percentage and candidate
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate

        #Store winning summary
        winning_candidate_summary = (
            f"----------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"----------------------------\n")
        #Print winning candidate summary
        print(winning_candidate_summary) 
        #write winning candidate summary to election results text file     
        txt_file.write(winning_candidate_summary)
#Open function to write data


    #write data to the file
    #txt_file.write("Counties in the Election\n----------------\n")
    #txt_file.write("Arapahoe\nDenver\nJefferson")

