import re
with open('/home/adrian/Documents/Programming/Advent_of_Code/day_6/input.txt', 'r') as file:
    operators = {'*', '+'}
    numbers = []
    for line in file:
        line = line.replace('\n', '')
        numbers.append(line)

sum = 0
string = ""
for i in reversed(range(len(numbers[0]))):
    for j in range(len(numbers)):
        if numbers[j][i] in operators:
            string = re.sub(r'\s+', numbers[j][i], string.strip())
            sum += eval(string)
            string = ""
        else:
            string += numbers[j][i]
print(sum)