import re
file = open('input.txt', 'r')
array = file.readline().split(',')
sum = 0
for line in array:
    for num in range(int(line.split('-')[0]), int(line.split('-')[1])+1):
        text = str(num)
        if re.match(r'^(\d+)\1+$', text):
            sum += int(text)
print(sum)