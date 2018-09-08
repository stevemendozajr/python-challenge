import os
import csv


# creating variable name of incomingCSV to collect the budget data csv file
incomingCSV = os.path.join( "budget_data.csv")


#define lists to hold data we will extract from the csv file
#Months to put each month/date into a list
#ProfitLoss to put each Profit/Loss amount into a list
#ProfitLossChange to put each change in ProfitLoss between each month
Months = []
ProfitLoss = []
ProfitLossChange = []


# Open the csv file using "read" mode. Specify the variable to hold the contents
with open(incomingCSV, 'r', newline='') as csvfile:


    # Initialize csv.reader
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #to skip over header row in the csv file and give it a variale name
    csv_header = next(csvreader)

    #Declare and intiliaze variable name sumchange and set to start at zero
    sumchange = 0

    #loop through each row in csv file and store each row data from specifc column
    #into its own list    
    for row in csvreader:
        
        #stores each date in a list named Months
        Months.append(row[0])
        
        #stores each profit/loss in a list named ProfitLoss
        ProfitLoss.append(int(row[1]))


    #calculates the total number of elements/months of data in the list Months
    #and store it into a variable named totalMonths
    totalMonths = len(Months)


    
    #declore and initialize variable sumPL and set to start at zero
    sumPL = 0
    

    #loop through each row in ProfitLoss list
    #calculates the sum of all the elements in the list ProfitLoss
    #to give us Total Profit Loss
    for num in ProfitLoss:
        
        sumPL += num

    #loop through specifically defined indexes in ProfitLoss list
    #subtracting current element index from next element index, start at index 1
    for numm in range(1,len(ProfitLoss)):


        #finds the difference in ProfitLoss between each month and stores the result
        #into a new list called ProfitLossChange
        #then calculates the sum of all the ProfitLossChange elements and divides
        #by total list length to find the Average Change for the time period
        ProfitLossChange.append(ProfitLoss[numm] - ProfitLoss[numm-1])
        AverageChange = round(sum(ProfitLossChange) / len(ProfitLossChange), 2)

        #finds the greatest increase in Profit between months and stores as variable
        #finds the greatest decrease in Profit between months and stores as variable
        GreatestIncProfits = max(ProfitLossChange)
        GreatestDecLoss = min(ProfitLossChange)

        #finds the index loaction of the max variables
        #with that index we find the index of the related Month, but need to add
        #1 to the index location to get the proper index for date from Month list
        GreatestIncDate = Months[ProfitLossChange.index(max(ProfitLossChange))+1]
        GreatestDecDate = Months[ProfitLossChange.index(min(ProfitLossChange))+1]

   
    #print out of calculations the the console
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {totalMonths}")
    print(f"Total: ${sumPL}")
    print(f"Average Change: ${AverageChange}")
    print(f"Greatest Increase in Profits: {GreatestIncDate} ${GreatestIncProfits}")
    print(f"Greatest Decrease in Profits: {GreatestDecDate} ${GreatestDecLoss}")


#Write to text file
#Set variable for output file
output_file = os.path.join("exported_solution_budget_data.txt")

#  Open the output file
with open(output_file, "w", newline="") as textfile:

    #print out the calculations to the text file
    print("Financial Analysis", file=textfile)
    print("------------------", file=textfile)
    print(f"Total Months: {totalMonths}", file=textfile)
    print(f"Total: ${sumPL}", file=textfile)
    print(f"Average Change: ${AverageChange}", file=textfile)
    print(f"Greatest Increase in Profits: {GreatestIncDate} ${GreatestIncProfits}", file=textfile)
    print(f"Greatest Decrease in Profits: {GreatestDecDate} ${GreatestDecLoss}", file=textfile)



 



   