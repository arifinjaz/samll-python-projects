import sys as s
import csv
import re

if len(s.argv) != 3:
    print('Usage: python dna.py data.csv sequence.txt')
    s.exit(1)
    
file = open(s.argv[1])
reader = csv.reader(file)

# To just assign the first column to hrader variable
header = next(reader)

# Rest of the data goes into data.
data = [column for column in reader]

# fi stores all dna data in a string
fi = open(s.argv[2]).read()
strs = []
temp = []
counter = 0
for j in header[1:]:    # to starting iteation from index 1
    counter = 0
    matches = re.finditer(j, fi)
    mp = [match.start() for match in matches]   # this shall save all index numbers where then row in first column matches.
    temp.clear()
    if len(mp) == 1:
        counter = 1
    for i in range(len(mp)-1):
        f = ((mp[i+1] - mp[i]) / len(j))    # Formula to check sequence.. 1 = sequence.
        if f == 1:
            counter += 1
            if i == (len(mp)-2):
                counter += 1
        elif f != 1:
            temp.append(counter+1)
            counter = 0
    temp.append(counter)
    strs.append(max(temp))
    
# loop to compare the the STRs from the file
for i in data:
    if list(map(int, i[1:])) == strs:
        print(i[0])
        s.exit(0)
print("No match.")