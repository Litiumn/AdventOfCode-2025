file = open('input.txt', 'r')
num = 50
password = 0
for line in file:
    letter = line.strip()
    previousNum = num
    rotations = 0

    if(letter[0] == 'L'):
        num -= int(letter.split('L')[1])
    else:
        num += int(letter.split('R')[1])

    rotations += abs(num)//100

    if((num < 0 and previousNum != 0) or num == 0):
        rotations +=1

    password += rotations
    num %= 100

print(password)


