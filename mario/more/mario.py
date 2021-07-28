while True:
    try:
        height = int(input('Height: '))
    except ValueError:
        continue
    if height > 0 and height < 9:
        break

i = height-1
j = 1

while (True):
    print(' ' * i, end='')
    print('#'*j, end='')
    print('  ', end='')
    print('#'*j)
    i -= 1
    j += 1
    if j > height:
        break
