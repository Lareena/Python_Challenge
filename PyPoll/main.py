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
    categories = ("Voter ID","County","Candidate")
    total_votes = 0
    vote_count = []
    vote_result = {}
    candidate_votes = []
    candidates = []





#total number of votes cast
    total_votes = 0
    total_votes = total_votes + 1



#complete list of candidates who received votes

#percentage of votes each candidate won

#total number of votes each candidate won

#winner of the election based on popular vote


