file = open('input.txt', 'r')
num = 50
password = 0
for line in file:
    letter = line.strip()
    if(letter[0] == 'L'):
        num -= int(letter.split('L')[1])
    else:
        num += int(letter.split('R')[1])

    if(num % 100 == 0):
        password += 1
    num %= 100

print(password)


