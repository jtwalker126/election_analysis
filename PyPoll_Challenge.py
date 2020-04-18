# The data we need to retrieve and report
# 1. Total number of votes cast
# 2. Number of votes from each county
# 3. Percentage of votes each county contributed to the election
# 4. County with the largest turnout
# 5. Complete list of candidates who received votes
# 6. The percentage of votes each candidate won
# 7. The total number of votes each candidate won
# 8. Declare a winner of the election based on popular vote.

# Pseudocode
# Tally total number of votes
# Create list of counties
# Tally votes by county
# calculate percentage by county
# Create list of all candidates receiving votes
# count votes correspond to each candidate
# calculate percentages for candidate
# declare winner based on highest percentage
# output data

#add dependencies
import csv
import os

# Assign variable for the file to load from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize variables to be used in analysis
total_votes=0
candidate_options=[]
candidate_votes = {}
county_options=[]
county_votes={}
largest_county_turnout = 0
winning_county=""
winning_candidate = ""
winning_count = 0
winning_percentage = 0


#Open election results and read the file
with open(file_to_load, 'r') as election_data:

    file_reader = csv.reader(election_data)

    #Read headers
    headers = next(file_reader)
    
    #Print each row in the CSV file
    for row in file_reader:
        #Calculate total vote count
        total_votes += 1

        #call county name for each row
        county_name=row[1]

        if county_name not in county_options:
            #add county name to county options list
            county_options.append(county_name)
            #add county name to county votes dictionary and set to 0
            county_votes[county_name] = 0
        
        #add vote to appropriate county dictionary
        county_votes[county_name] += 1

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
        
        #store total votes and headers in variable
        election_results = (
            f"\nElection Results\n"
            f"----------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"----------------------------\n")

        #Print final vote count to terminal
        print(election_results, end="")

        # Save the final vote count to the text file
        txt_file.write(election_results)

        #write header for county votes
        county_header = (f"\nCounty Votes:\n")
        print(county_header)
        txt_file.write(county_header)

        #calculate, print, and write county level results
        for county in county_votes:
            #retrive vote number for given county
            votes = county_votes[county]

            #calculate percentage for county vote
            vote_percentage = float(votes) / float(total_votes) * 100

            #store county results for vote percentage and total votes
            county_results = (f"{county}: {vote_percentage:.1f}% ({votes:,})\n")

            #print county results to terminal
            print(county_results, end="")

            #write county results to txt file
            txt_file.write(county_results)

            #determine winning county based on county with highest number of votes
            if votes > largest_county_turnout:
                largest_county_turnout = votes
                winning_county = county

        #store county turnout summary
        county_turnout_summary = (
            f"\n----------------------------\n"
            f"Largest County Turnout: {winning_county}\n"
            f"----------------------------\n")
        
        #print county turnout 
        print(county_turnout_summary)

        #write county turnout summary to txt file
        txt_file.write(county_turnout_summary)

        # calculate, print, and write candidate level results
        for candidate in candidate_votes:  

            #retrieve vote count for each candidate
            votes = candidate_votes[candidate]
            #calculate percentage
            vote_percentage = float(votes) / float(total_votes) * 100

            #store candidate name, vote percentage, and votes 
            candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

            #Print candidate results
            print(candidate_results, end="")

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
