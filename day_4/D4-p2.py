file = open('input.txt', 'r')
walls = []
col = 0
checker = True
for line in file:
    walls.append(list(line.strip()))

while checker:
    checker = False
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
                walls[line][column] = "."
                checker = True
print(col)