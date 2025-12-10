with open('/home/adrian/Documents/Programming/Advent_of_Code/day_7/test.txt', 'r') as file:
    arr = []
    for line in file:
        arr.append(line.strip())

def traverse(arr, x, y, visited, sum = 0):
    if (x, y) in visited:
        return 0
    visited.add((x, y))

    if arr[x][y] == '^':
        return 1 + traverse(arr, x, y+1, visited) + traverse(arr, x, y-1, visited)
    if x == len(arr) - 1:
        return 0
    if arr[x][y] == '.':
        sum = traverse(arr, x+1, y, visited)
    return sum

visited = set()
print(traverse(arr, 1, len(arr[0])//2, visited))