file = open('/home/adrian/Documents/Programming/Advent_of_Code/day_4/input.txt', 'r')
walls = []
remove = []
col = 0
for line in file:
    walls.append(list(line.strip()))

while True:
    for line in range(0, len(walls)):
        for column in range(0, len(walls[line])):
            string = []
            if(walls[line][column] == "."):
                continue

            for row in [line-1, line, line+1]:
                if(row == -1 or row == len(walls)):
                    continue
                start = column-1
                end = 3
                if(column-1 == -1):
                    start += 1
                    end -= 1
                if(column+1 == len(walls)):
                    end -= 1
                string += walls[row][start:start+end]
                
            while "." in string:
                string.remove('.')

            if(len(string)-1 < 4):
                col += 1
                remove.append((line,column))
    
    if len(remove) == 0:
        break
    
    for left, right in remove:
        walls[left][right] = '.'
    remove = []
print(col)