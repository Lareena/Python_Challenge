#import dependencies
import os
import csv

#declare file path
csvpath = os.path.join("..","PyBank","budget_data3.csv")

with open("budget_data3.csv","r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
    csv_reader =next(csv_reader)
    output_file = "budget_analysis.txt"

#initialize variables
    revenue_length = 0
    avg_revenue_change = 0
    max_revenue_change = 0
    min_revenue_change = 0
    revenue = []
    revenue_change = []
    months = []


#total number of months included in dataset
    for row in csv_reader:
    
        total_months = 0
        total_months = total_months + 1

    
#net total amount of "Profit/Losses" over the entire period
   
        total_revenue = 0
        total_revenue = total_revenue + int(row[1])
        revenue.append(int(row[1]))
        months.append(int(row[0]))
        


#average of the changes in "Profit/Losses" over the entire period
    for i in range(len(revenue)-1):
        change = int(revenue[i+1]) - int(revenue[i])
        
        avg_revenue_change = int(revenue[i+1]) - int(revenue[i])

        avg_revenue_change = abs(sum(revenue_change)/len(revenue_change))
        



#the greatest increase in profits (date and amount) over the entire period

        
        max_revenue_change= max(revenue_change)
        max_revenue_change_date = str(date[revenue_change.index(max(revenue_change))])

#the greatest decrease in losses (date and amount) over the entire period
        min_revenue_change= min(revenue_change)
        min_revenue_change_date = str(date[revenue_change.index(min(revenue_change))])



#Print the outputs
        print("Financial Analysis")
        print("--------------------")

        print(f"Total Months:  {str(total_months)}")
        print(f"Total Revenue:  {str(total_revenue)}")
        print(f"Average Revenue Change + {str(avg_revenue_change)}")
        print(f"Greatest Increase in Revenue:  {str(max_revenue_change_date) +str(max_revenue_change)}")
        print(f"Greatest Decrease in Revenue:  {str(min_revenue_change_date) +str(min_revenue_change)}")

#Output to text file
output_file = os.path.join("output.csv")
with open(file_to_output,"w") as datafile:
    csvwriter = csv.writer(datafile)
    datafile.writerow("Financial Analysis")
    datafile.write("\n")
    datafile.write(f"Total Months:  {str(total_months)}")
    datafile.write("\n")
    datafile.write(f"Total Revenue:  {str(total_revenue)}")
    datafile.write("\n")
    datafile.write(f"Average Revenue Change + {str(avg_revenue_change)}")
    datafile.write("\n")
    datafile.write((f"Greatest Increase in Revenue:  {str(max_revenue_change_date) +str(max_revenue_change)}")
    datafile.writerow("\n")
    datafile.write(f"Greatest Decrease in Revenue:  {str(min_revenue_change_date) +str(min_revenue_change)}")



