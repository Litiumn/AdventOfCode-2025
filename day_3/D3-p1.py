# Optimized using Monotonic Stack
file = open('input.txt', 'r')
banks = []
sum = 0
string = ""
for line in file:
    banks.append(list(line.strip()))
    
for bank in banks:
    stack = []
    for index in range(len(bank)):
        while(stack and stack[-1] < bank[index] and len(stack) + (len(bank)-index) > 2):
            stack.pop()
        if(len(stack) < 2):
            stack.append(bank[index])
    sum += int(''.join(str(num) for num in stack))
print(sum)



'''

# Old Code

file = open('input.txt', 'r')
banks = []
sum = 0
for line in file:
    banks.append(list(line.strip()))

for bank in banks:
    start = 0
    found = 0
    size = len(bank)-1
    jolt = ""
    for _ in bank:
        if(len(jolt) == 2):
            break
        sub = bank[start:size-found]
        num = max(sub)
        start += sub.index(num)+1
        found += sub.index(num)
        size = start+(len(bank)-1)
        jolt += num
    sum += int(jolt)
print(sum)
'''