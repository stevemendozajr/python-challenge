import os
import csv


# creating variable name of incomingCSV to collect the budget data csv file
incomingCSV = os.path.join( "election_data.csv")


#define lists to hold data we will extract from the csv file
#VoterID to put each voter id into a list
#County to put each county into a list
#Candiate to put each canidate into a list
VoterID = []
Canidates = []
KhanVotes = []
CorreyVotes = []
LiVotes = []
OTooleyVotes = []


# Open the csv file using "read" mode. Specify the variable to hold the contents
with open(incomingCSV, 'r', newline='') as csvfile:


    # Initialize csv.reader
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #to skip over header row in the csv file and give it a variale name
    csv_header = next(csvreader)

    #loop through each row in csv file and store each row data from specifc column
    #into its own list  
    for row in csvreader:

        #store each voter id into list named VoterID so we can count total votes later
        VoterID.append(row[0])

        #store each candiate voted for into a list
        #so we can find unique canidates who received votes
        Canidates.append(row[2])

        #if statement to store every different canidate vote
        #into its own list so we can count and find percentages
        if row[2] == 'Khan':
            KhanVotes.append(row[2])
        elif row[2] == 'Correy':
            CorreyVotes.append(row[2])
        elif row[2] == 'Li':
            LiVotes.append(row[2])
        else:
            OTooleyVotes.append(row[2])

    
    #calculation of total votes received
    TotalVotes = len(VoterID)
    
    #a set/list of all canidates who received votes
    UniqueCanidates = set(Canidates)

    #calculation to find total Khan votes and percent of total votes
    TotalKhanVotes = len(KhanVotes)
    KhanPercent = round(int(TotalKhanVotes) / int(TotalVotes) * 100, 2)

    #calculation to find total Correy votes and percent of total votes
    TotalCorreyVotes = len(CorreyVotes)
    CorreyPercent = round(int(TotalCorreyVotes) / int(TotalVotes) * 100, 2)

    #calculation to find total Li votes and percent of total votes
    TotalLiVotes = len(LiVotes)
    LiPerecent = round(int(TotalLiVotes) / int(TotalVotes) * 100, 2)

    #calculation to find total OTooley votes and percent of total votes
    TotalOTooleyVotes = len(OTooleyVotes)
    OTooleyPercent = round(int(TotalOTooleyVotes) / int(TotalVotes) * 100, 2)

    
    #print out of calculations the the console
    print("Election Results")
    print("------------------")
    print(f"Total Votes: {TotalVotes}")
    print("------------------")
    print(f"Khan: {KhanPercent}% ({TotalKhanVotes})")
    print(f"Correy: {CorreyPercent}% ({TotalCorreyVotes})")
    print(f"Li: {LiPerecent}% ({TotalLiVotes})")
    print(f"O'Tooley: {OTooleyPercent}% ({TotalOTooleyVotes})")
    print("------------------")
    print(f"Winner:")
    print("------------------")
    
    

#Write to text file
#Set variable for output file
output_file = os.path.join("exported_solution_election_data.txt")

#Open the output file
with open(output_file, "w", newline="") as textfile:

    print("Election Results", file=textfile)
    print("------------------", file=textfile)
    print(f"Total Votes: {TotalVotes}", file=textfile)
    print("------------------", file=textfile)
    print(f"Khan: {KhanPercent}% ({TotalKhanVotes})", file=textfile)
    print(f"Correy: {CorreyPercent}% ({TotalCorreyVotes})", file=textfile)
    print(f"Li: {LiPerecent}% ({TotalLiVotes})", file=textfile)
    print(f"O'Tooley: {OTooleyPercent}% ({TotalOTooleyVotes})", file=textfile)
    print("------------------", file=textfile)
    print(f"Winner:", file=textfile)
    print("------------------", file=textfile)