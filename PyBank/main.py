import os
import csv

pybankcsv = os.path.join("..","PyBank","pybank.csv")

with open(pybankcsv,'r') as csvfile:
    #skip headers
    next(csvfile)
    csvreader = csv.reader(csvfile, delimiter=",")
    row_count = 0
    stocktotal = 0
    avgcalc = 0
    i = 0
    val = []
    month = []
    rev = []
    
    for row in csvreader:
        #sum 1 to month counter per present row
        row_count +=1
        #add current cell value to previous cell value and for the entire column
        stocktotal += float(row[1])

        #fill a list with all the numbers in the second column as floats
        val.append(float(row[1]))
        #fill a list with the months as strings
        month.append(row[0])
        #determine index of max value profit change
        maxind = val.index(max(val))
        #determine index of min value profit change
        minind = val.index(min(val))
    #while loop for average change calculation where list is appended with+
    #averages, summed, and then divided by the length of it's size
    while i < (len(val)-1):
        
        avgcalc = val[i+1] - val[i]
        rev.append(avgcalc)
        i = i+1
    avgrev = (sum(rev))/(len(rev))
    avgrev = round(avgrev,2)

    #print total ammounts to console
    print(f"Time frame in months is: {row_count}")
    print(f"This is the stock total: {stocktotal}")
    print(f"The average change per month is {avgrev}")
    print(f"The maximum profit obtained this time period is {max(rev)} during the month of {month[maxind]}")
    print(f"The maximum profit loss over the time period is {min(rev)} during the month of {month[minind]}")

output_file = os.path.join("Financialanalysis.txt")
writer = open(output_file, 'w+')    
writer.write(f"Time frame in months is: {row_count} \n")
writer.write(f"Total Profit/Loss: {stocktotal} \n")
writer.write(f"Average Change: {avgrev} \n")
writer.write(f"The maximum profit obtained this time period is {max(rev)} during the month of {month[maxind]}\n") 
writer.write(f"The maximum profit loss over the time period is {min(rev)} during the month of {month[minind]}\n")