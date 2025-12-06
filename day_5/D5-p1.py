with open('input.txt', 'r') as file:
    lower, upper, ids = [], [], []
    count = 0
    for line in file:
        line = line.strip()
        if(line == ''):
            continue
        if("-" in line):
            lower.append(list(map(int, line.split('-'))))
        else:
            ids.append(int(line))

    for i, j in lower:
        upper.append([j, i])
    lower.sort()
    upper.sort()

found = False
for id in ids:
    low = 0
    high = len(lower) -1
    while low <= high:    
        mid = low + (high - low)//2
        if(lower[mid][0] <= id <= lower[mid][1]):
            count += 1
            found = True
            break
        if(lower[mid][0] > id):
            high = mid - 1
        else:
            low = mid + 1
    
    if found:
        found = False
        continue
    
    low = 0
    high = len(lower) -1
    while low <= high:    
        mid = low + (high - low)//2
        if(upper[mid][1] <= id <= upper[mid][0]):
            count += 1
            break
        if(upper[mid][0] > id):
            high = mid - 1
        else:
            low = mid + 1
print(count)