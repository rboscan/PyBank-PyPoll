import os
import csv

csvpath = os.path.join("..","PyPoll","PyPoll.csv")

candidates = []
votecounts = []
totalvotes = 0
majority = 0
x = 0
y = 0
z = 0

with open(csvpath, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        totalvotes += 1
        candidates.append(row[2])

candidates = list( dict.fromkeys(candidates))

while x < (len(candidates)):
    with open(csvpath, newline= "") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        header = next(csvreader)
        votecounter = 0
        for row in csvreader:
            if candidates[x] == row[2]:
                votecounter = votecounter + 1           
    votecounts.append(votecounter)
    x = x + 1
    
print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalvotes}")
print("-------------------------")

while y < (len(candidates)):
    if votecounts[y] > majority:
        majority = votecounts[y]
        majoritycandidate = y
    percentage = ((votecounts[y])/(sum(votecounts)))*100
    percentage = round(percentage, 3)
    print(f"{candidates[y]}: {percentage}% {votecounts[y]}")
    y = y + 1

print("-------------------------")
print(f"Winner: {candidates[majoritycandidate]}")
print("-------------------------")

output_file = os.path.join("voteresults.txt")
writer = open(output_file, 'w+') 
writer.write("Election Results\n")
writer.write("-------------------------\n")
writer.write(f"Total Votes: {totalvotes} \n")
writer.write("-------------------------\n")
while z < (len(candidates)):
    percentage = ((votecounts[z])/(sum(votecounts)))*100
    percentage = round(percentage, 3)
    writer.write(f"{candidates[z]}: {percentage}% {votecounts[z]}\n")
    z = z + 1
writer.write("-------------------------\n")
writer.write(f"Winner: {candidates[majoritycandidate]} \n")
writer.write("-------------------------\n")