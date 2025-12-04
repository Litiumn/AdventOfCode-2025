file = open('/home/adrian/Documents/Programming/Advent_of_Code/day_3/input.txt', 'r')
banks = []
sum = 0
string = ""
for line in file:
    banks.append(list(line.strip()))
    
for bank in banks:
    stack = []
    for index in range(len(bank)):
        while(stack and stack[-1] < bank[index] and len(stack) + (len(bank)-index) > 12):
            stack.pop()
        if(len(stack) < 12):
            stack.append(bank[index])
    sum += int(''.join(str(num) for num in stack))
print(sum)