#import dependencies
import re
import os

#define variables
numlines = 0
numwords = 0
numchars = 0
avg_numwords = []
numletters_list = []
lineslist =[]

#open csvfiles
filepath = os.path.join("paragraph_2.txt")
with open("paragraph_2.txt", "r") as text_file:
    
#Count of sentences
    lineslist = re.split("[?<=.!?] +", str(text_file))
    numlines = len(lineslist)
    
    for line in text_file:
        #Count of words
        wordslist = line.split()
        numwords += len(wordslist)

        #Count of letters per word
        for words in wordslist:
            numletters = len(words)
            numletters_list.append(numletters)
        avg_numwords = sum(numletters_list)/(numwords)

        #Average Sentence length        
        avg_line_len = (numwords)/(numlines)

#Printing all the values
print("Paragraph Analysis")
print("-----------------")
print("Approximate Word Count: " + str(numwords))
print("Approximate Sentence Count:" + str(numlines))
print("Average Letter Count:" + str(avg_numwords))
print("Average Sentence Length:" + str(avg_line_len))

#write to output file
output_file = os.path.join("output.csv","new.csv")
with open(file_to_output,"w") as datafile:
    csvwriter = csv.writer(datafile)
    
    datafile.write("Paragraph Analysis")
    datafile.write("Approximate Word Count: " + str(numwords))
    datafile.write("Approximate Sentence Count:" + str(numlines))
    datafile.write(("Average Letter Count:" + str(avg_numwords))
    datafile.write(("Average Sentence Length:" + str(avg_line_len))
    