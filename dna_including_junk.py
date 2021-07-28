import sys as s
import csv,re
from itertools import groupby
import collections
#print(dir(re))

def main ():
    if len (s.argv) != 3:
        print ('Usage: python dna.py data.csv sequence.txt')
        s.exit(1)
    #print (f"a0:{s.argv[0]} \na1:{s.argv[1]} \na2:{s.argv[2]} \n")

    file = open(s.argv[1])
    reader = csv.reader(file)
    header = next(reader)
    data = [column for column in reader]
    #print(len(header)-1)
    #print(data[0])

    fi = open(s.argv[2]).read()

    AT = []
    temp = []
    AGATC = []
    strs = []
    counter = 0
    """
    matches = re.finditer(header[2],fi)
    mp = [match.start() for match in matches]
    print(mp)
    for i in range(len(mp)-1):
        f = ((mp[i+1] - mp[i]) / len(header[2]))
        #print("f:",f)
        if f == 1:
            counter += 1
            if i == (len(mp)-2):
                print("yes")
                counter += 1
        elif f != 1:
            temp.append(counter+1)
            counter = 0
    temp.append(counter)
    print(temp)
    """


    for j in header[1:]:
        matches = re.finditer(j,fi)
        mp = [match.start() for match in matches]
        temp.clear()
        counter = 1
        #if len(mp) == 1:
            #counter = 1
        for i in range(len(mp)-1):
            f = ((mp[i+1] - mp[i]) / len(j))
            #print("f:",f)
            if f == 1:
                counter += 1
                #if i == (len(mp)-2):
                    #print("yes")
                    #counter += 1
            elif f != 1:
                temp.append(counter+1)
                counter = 0
        temp.append(counter)
        strs.append(max(temp))
    print(strs)

    #print(type(strs))
    for i in data:
        if list(map(int, i[1:])) == strs:
            print (i[0])

            #while ((mp[i+1] - mp[i]) / len(header[1])) == 1:
                #print("yes", end = '')
                #i += 1
                #counter += 1

            #AGATC.append(counter)
        #print (mp[i+1],mp[i],len(header[1]), end='/')
        #print((mp[i+1] - mp[i]) /len(header[1]))



    #print (mp)
    #for i in mp:
        #diff = (int(i[1]-i[0])/len(header[1]))
        #print(diff)
        #difference = [(mp[1][1]-mp[1][0])/5]



"""
    for i in range(len(fi)-4):
        if fi[i] in ('A','T') and fi[i+1] in ('A'):
            AT.append (fi[i:i+4])
        elif fi[i] in ('A') and fi[i+1] in ('G'):
            AGATC.append (fi[i:i+5])
    #print(AT)

    agatc = Hi_Seq_finder(AGATC,'AGATC')
    aatg = Hi_Seq_finder(AT,'AATG')
    tatc = Hi_Seq_finder(AT,'TATC')

    print(agatc,aatg,tatc)
    with open(s.argv[1], newline='') as f:
        cdata = csv.DictReader(f)
        for line in cdata:
            #print(line['AGATC'],agatc)
            if line['AGATC'] == str(agatc) and line['AATG'] == str(aatg) and line['TATC'] == str(tatc):
                print(line['name'])
                return
        print ('No match.')


def Hi_Seq_finder (value,s_value):
    tm = [0]
    k = 0
    c = 0
    d = len(value)
    #print(d)
    while k < (d): # While loop to find AGATC
        if value[k] == s_value:
            c = c + 0
            if k == d-1:
                tm.append(c)
                break
            else:
                while value[k + c] == s_value:
                    #print(c)
                    c = c + 1
                    if k + c == d-1:
                        break
                tm.append(c)
                k = k + c
            c=0
        k += 1
    #print (tm)
    return max(tm)
"""
main()


#print(f'1:{agatc}\n2:{aatg}\n3:{tatc}')


