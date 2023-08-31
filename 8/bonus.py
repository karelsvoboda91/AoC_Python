with open('input.txt') as f:
    lines = f.readlines()

delkaradku = len(lines[0])-1
max = 0

for i in range(len(lines)):
    for j in range(delkaradku):

        top=0
        down=0
        left=0
        right=0

        for strom in reversed(range(j)): # left
            if((int(lines[i][strom]) < int(lines[i][j])) ):
                left = left + 1
            else:
                left = left + 1
                break

        for strom in range(delkaradku - j - 1): # right
            if((int(lines[i][j+strom + 1]) < int(lines[i][j])) ):
                right = right + 1
            else:
                right = right + 1
                break

        for strom in reversed(range(i)): # top
            if((int(lines[strom][j]) < int(lines[i][j])) ):
                top = top + 1
            else:
                top = top + 1
                break

        for strom in range(len(lines) - i - 1): # down
            if((int(lines[i+strom + 1][j]) < int(lines[i][j])) ):
                down = down + 1
            else:
                down = down + 1
                break

        if max < left*right*top*down:
            max=left*right*top*down

print(max)