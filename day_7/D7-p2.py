with open('/home/adrian/Documents/Programming/Advent_of_Code/day_7/test.txt', 'r') as file:
    arr = []
    for line in file:
        arr.append(line.strip())

def traverse(arr, x, y, memo):
    if (x,y) in memo:
        return memo[(x,y)]
    
    if arr[x][y] == '^':
        memo[(x,y)] = traverse(arr, x, y-1, memo) + traverse(arr, x, y+1, memo)
        return memo[(x,y)]
    if x == len(arr) - 1:
        return 1
    if arr[x][y] == '.':
        memo[(x,y)] = traverse(arr, x+1, y, memo)
    return memo[(x,y)]

memo = dict()
print(traverse(arr, 1, len(arr[0])//2, memo))