#import dependencies
import os
import csv

#declare file path
csvpath = os.path.join("election_data3.csv")

#open csvfile
with open("election_data3.csv","r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
    csv_reader = next(csv_reader)
    output_file = "election_results.txt"


#define variables
vote_count=0
candidates = []
vote_count_candidate = {}




#total number of votes cast
    for row in csv_reader:
        ballot = [row[2] for row in csvreader]
        numVotes = len(ballot)




#complete list of candidates who received votes
        
        candidates = list(set(ballot))

#percentage of votes each candidate won


#total number of votes each candidate won

#winner of the election based on popular vote


