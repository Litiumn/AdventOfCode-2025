with open('input.txt', 'r') as file:
    ranges = []
    ids = []
    count = 0
    for line in file:
        line = line.strip()
        if(line == ''):
            break
        if("-" in line):
            ranges.append(list(map(int, line.split('-'))))
    ranges.sort()

adjustedRange = []
for lower, upper in ranges:
    if not adjustedRange:
        adjustedRange.append([lower, upper])
        
    prevUp = adjustedRange[-1][1]
    if lower <= prevUp:
        if upper < prevUp:
            continue
        adjustedRange[-1][1] = upper
    else:
        adjustedRange.append([lower, upper])

for lower, upper in adjustedRange:
    count += (upper-lower)+1

print(count)