with open('input.txt') as f:
    lines = f.readlines()

score=0
i=0

print(lines[1][0:1])
print(lines[1][2:3])
    
while(i < len(lines)):
    if(lines[i][2:3] == 'X'):
        if(lines[i][0:1] == 'A'):
            score=score+4
        if(lines[i][0:1] == 'B'):
            score=score+1
        if(lines[i][0:1] == 'C'):
            score=score+7
    if(lines[i][2:3] == 'Y'):
        if(lines[i][0:1] == 'A'):
            score=score+8
        if(lines[i][0:1] == 'B'):
            score=score+5
        if(lines[i][0:1] == 'C'):
            score=score+2
    if(lines[i][2:3] == 'Z'):
        if(lines[i][0:1] == 'A'):
            score=score+3
        if(lines[i][0:1] == 'B'):
            score=score+9
        if(lines[i][0:1] == 'C'):
            score=score+6   
    i=i+1

print(score)

