import sys as s
import csv

def main ():
    if len (s.argv) != 3:
        print ('Usage: python dna.py data.csv sequence.txt')
        s.exit(1)
    #print (f"a0:{s.argv[0]} \na1:{s.argv[1]} \na2:{s.argv[2]} \n")
    fi = open(s.argv[2]).read()
    AT = []
    AGATC = []
    #print (fi)

    for i in range(len(fi)-4):
        if fi[i] in ('A','T') and fi[i+1] in ('A'):
            AT.append (fi[i:i+4])
        elif fi[i] in ('A') and fi[i+1] in ('G'):
            AGATC.append (fi[i:i+5])
    print(AT)

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
            c = 0
            if k == d-1:
                tm.append(c)
                break
            else:
                while value[k + c] == s_value:
                    c += 1

                tm.append(c)
                k = k + c
                c=0
        k += 1
    #print (tm)
    return max(tm)

main()


#print(f'1:{agatc}\n2:{aatg}\n3:{tatc}')


