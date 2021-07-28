text = input('TEXT:')
word = 1
sentence = 0
letters = 0

# For loop to cound letters. words & sentences.
for i in range(len(text)):

    if text[i].isalpha():
        letters += 1

    if text[i] == ' ':
        word += 1
# checking for sentences
    if text[i] in ('.', '!', '?'):
        sentence += 1

L = (letters / word) * 100
S = (sentence / word) * 100

index = 0.0588 * L - 0.296 * S - 15.8

if index < 1:
    print('Before Grade 1')
elif index > 16:
    print("Grade 16+")
else:
    print(f'Grade {round(index)}')
