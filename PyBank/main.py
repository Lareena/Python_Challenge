#import dependencies
import os
import csv

#declare file path
csvpath = os.path.join("budget_data3.csv")

#open csvfile
with open("budget_data3.csv","r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
    csv_reader = next(csv_reader)
    file_to_output = "Budget_analysis.txt"

#initialize variables
    
    revenue = []
    revenue_change = []
    months = []
    monthly_change = []

#total number of months included in dataset
    for row in csv_reader:
        
        months.append(int(row[0]))
        revenue.append(int(row[1]))
        
        total_months = total_months + 1
        
       
    
#net total amount of "Profit/Losses" over the entire period
       
        total_revenue = 0
        total_revenue = sum(revenue)
        
        
        


#average of the changes in "Profit/Losses" over the entire period
    for i in range(len(revenue)-1):
        
        i = 0   
        change = int(revenue[i+1]) - int(revenue[i])
        
        avg_revenue_change = int(revenue[i+1]) - int(revenue[i])

        avg_revenue_change = abs(sum(revenue_change)/len(revenue_change))
        



#the greatest increase in profits (date and amount) over the entire period

        
        max_revenue_change= max(revenue_change)
        max_revenue_change_date = str(months[revenue_change.index(max(revenue_change))])

#the greatest decrease in losses (date and amount) over the entire period
        min_revenue_change= min(revenue_change)
        min_revenue_change_date = str(months[revenue_change.index(min(revenue_change))])



#Print the outputs
        print("Budget Analysis")
        print("--------------------")

        print(f"Total Months:  {str(total_months)}")
        print(f"Total Revenue:  {str(total_revenue)}")
        print(f"Average Revenue Change + {str(avg_revenue_change)}")
        print(f"Greatest Increase in Revenue:  {str(max_revenue_change_date) +str(max_revenue_change)}")
        print(f"Greatest Decrease in Revenue:  {str(min_revenue_change_date) +str(min_revenue_change)}")

#Output to text file
output_file = os.path.join("output.csv","new.csv")
with open(file_to_output,"w") as datafile:
    csvwriter = csv.writer(datafile)
    
    datafile.writerow("Budget Analysis")
    datafile.writerow(f"Total Months:  {str(total_months)}")
    datafile.writerow(f"Total Revenue:  {str(total_revenue)}")
    datafile.writerow(f"Average Revenue Change + {str(avg_revenue_change)}")
    datafile.writerow(f"Greatest Increase in Revenue:  {str(max_revenue_change_date) +str(max_revenue_change)}")
    datafile.writerow(f"Greatest Decrease in Revenue:  {str(min_revenue_change_date) +str(min_revenue_change)}")




