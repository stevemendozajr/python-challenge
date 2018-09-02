import os
import csv

# creating variable name of Path to collect the budget data csv file
incomingCSV = os.path.join( "budget_data.csv")


#define lists to hold data
Months = []
ProfitLoss = []



# Open the file using "read" mode. Specify the variable to hold the contents
with open(incomingCSV, 'r', newline='') as csvfile:

    # Initialize csv.reader
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #to skip over header row
    csv_header = next(csvreader)

    #loop through each row in csv file
    for row in csvreader:

        Months.append(row[1])

        totalMonths = len(Months)

    print(f"Total Months: {totalMonths}")




#define the function and have it accept csv 'financial analysis' as its sole parameter
#def getAnalysis(budgetData):

   # Total number of months in data set
   #totalMonths = int(len(budgetData[1]))

   #print(f"Total Months: {str(totalMonths)}")


 



   