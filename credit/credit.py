import sys
while True:
    try:
        card = int(input('Number: '))
    except ValueError:
        continue
    length = len(str(card))
    if length < 13:
        print('INVALID')
        break
    else:
        break

card_list = [int(x) for x in str(card)]

od = card_list[-1::-2]
ed = card_list[-2::-2]
checksum = 0
checksum += sum(od)
temp = 0

for i in range(len(ed)):
    temp = ed[i] * 2
    if temp > 9:
        temp1 = [int(x) for x in str(temp)]
        temp = sum(temp1)
    checksum += temp

if checksum % 10 != 0:
    print('INVALID')
    sys.exit()

if length == 13 or length == 16 and card_list[0] == 4:
    print('VISA')
elif length == 15 and card_list[0] == 3 and card_list[1] in (4, 7):
    print('AMEX')
elif length == 16 and card_list[0] == 5 and card_list[1] in range(1, 6):
    print('MASTERCARD')
else:
    print('INVALID')
