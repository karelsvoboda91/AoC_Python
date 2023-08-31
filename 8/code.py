with open('input2.txt') as f:
    lines = f.readlines()

delkaradku = len(lines[0])-1
visibility= [([0]*delkaradku) for i in range(len(lines))]

for i in range(len(lines)):
    nejvyssi=-1
    for j in range(delkaradku):
        if(int(lines[i][j]) > nejvyssi):
            visibility[i][j]=1
            nejvyssi= int(lines[i][j])

for i in range(len(lines)):
    nejvyssi=-1
    for j in reversed(range(delkaradku)):
        if(int(lines[i][j]) > nejvyssi):
            visibility[i][j]=1
            nejvyssi= int(lines[i][j])


for i in range(delkaradku):
    nejvyssi=-1
    for j in range(len(lines)):
        if(int(lines[j][i]) > nejvyssi):
            visibility[j][i]=1
            nejvyssi= int(lines[j][i])

for i in range(delkaradku):
    nejvyssi=-1
    for j in reversed(range(len(lines))):
        if(int(lines[j][i]) > nejvyssi):
            visibility[j][i]=1
            nejvyssi= int(lines[j][i])


pocet = 0

for row in visibility:
    pocet = pocet + sum(row)
    print(row)


print(pocet)