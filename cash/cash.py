import math

quarters = 25
dimes = 10
nickels = 5
pennies = 1
i = 0

while True:
    try:
        cash = float(input('Change owed: '))
    except ValueError:
        continue
    if cash > 0.00:
        break

cent = cash * 100

if cent >= quarters:
    i += cent // quarters
    cent -= (quarters * i)

if cent >= dimes:
    i += cent // dimes
    cent -= (dimes * (cent // dimes))
    
if cent >= nickels:
    i += cent // nickels
    cent -= (nickels * (cent // nickels))
    
if cent >= pennies:
    i += cent // pennies
    cent -= (pennies * (cent // pennies))

print(round(i))
