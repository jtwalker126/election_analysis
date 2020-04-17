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

#Assign variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename for the output file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open election results and read the file
with open(file_to_load, 'r') as election_data:

    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)
    #for row in file_reader:
        #print(row[0])

#Open function to write data
with open(file_to_save, 'w') as txt_file:

    #write data to the file
    txt_file.write("Counties in the Election\n----------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

