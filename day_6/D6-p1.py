with open('/home/adrian/Documents/Programming/Advent_of_Code/day_6/input.txt', 'r') as file:
    operators = {'*', '+'}
    numbers = []
    operations = []
    for line in file:
        line = line.strip().split()
        if operators.issubset(line):
            operations += line
        else:
            numbers.append(list(map(int, line)))

length = [len(num) for num in numbers] 
rearranged = dict()

for num in numbers:
    for index, value in enumerate(num):
        if index not in rearranged:
            rearranged[index] = value
        else:
            operation = operations[index]
            if operation == '+':
                rearranged[index] += value
            elif operation == '*':
                rearranged[index] *= value
print(sum(rearranged.values()))


'''
    # Old Code

    index = 0
    while index < num:
        check = rearranged.get(index, False)
        if check:
            rearranged[index] += operations[index] + (numbers[line][index])
        else:
            rearranged[index] = numbers[line][index]
        index += 1
    line += 1
'''