#import dependencies
import os
import csv

#u.s. state abbreviations
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',}

#declare pathname of file

csvpath = os.path.join("employee_data3.csv")


#open csvfile
with open("employee_data3.csv","r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
    csv_reader = next(csv_reader)

#read file    

    employee_csv = [row for row in csv_reader]

#create new list adding header line
    employee_csv.append(["Emp ID","First Name","Last Name","DOB","SSN","State"])

#loop through originial list to get variation information

    for emp in employee_csv:
    #split first and last name
        name = emp[1].split(",")
        firstName = name[0]
        lastName = name[0]
        print(name)

    #reformat DOB
        DOB = emp[2].split("-")
        yearDOB = str(DOB[0])
        monthDOB = str(DOB[1])
        dayDOB = str(DOB[2]) 
        birthDate = monthDOB + "/" + dayDOB + "/" + yearDOB
        print(DOB)

     # Hide the SSN
        SSN = emp[3].split("-")
        secureSSN = "***-**-" + ssn[2]
        stateAbb = us_state_abbrev[emp[4]]
        print(secureSSN)
        print(stateAbb)
    #Create employee list in new format
    output_path = ("output", "new.csv")
    employee_csv.append(["EMP ID", "First Name", "Last Name","DOB", "SSN", "State"])

    #Create output file
with open('employee_data_reformatted.csv', 'w', newline="") as resultfile:
        csvwriter = csv.writer(csvfile, delimiter = ",")
        writer = csv.writer(resultfile)
        writer.writerows("EMP ID", "First Name", "Last Name","DOB", "SSN", "State")

