#modules
import os
import csv

#specify file path
csvpath = os.path.join(".","PyBank","budget_data3.csv")

#initialize variables
total_revenue = 0
total_months = 0
revenue_length = 0
avg_revenue_change = 0




with open (csvpath) as csvfile:

    csvreader=csv.reader(csvfile, delimiter=',')
    
    print(csvreader)

print("-------------------------------------------------------------------")
#total number of months included in dataset
with row in csvfile:
    total_months = total_revenue + 1

    total_revenue = total_revenue + int(row[1])

   

print("-------------------------------------------------------------------")
#net total amount of "Profit/Losses" over the entire period


print("-------------------------------------------------------------------")
#average of the changes in "Profit/Losses" over the entire period


print("-------------------------------------------------------------------")
#the greatest increase in profits (date and amount) over the entire period


print("-------------------------------------------------------------------")
#the greatest decrease in losses (date and amount) over the entire period
