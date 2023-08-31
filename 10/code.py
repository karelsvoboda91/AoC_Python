with open('input.txt') as f:
    lines = f.readlines()

cycle = 0
x=1

sum=0


for line in lines:
    if(line == 'noop\n'):
        cycle = cycle +1
        if(cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220):
            sum = sum + (cycle * x)
    elif line.split(' ')[0] == 'addx':
        cycle =cycle +1 
        if(cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220):
            sum = sum + (cycle * x)
        cycle =cycle +1 


        if(cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220):
            sum = sum + (cycle * x)
        x=x + int(line.split(' ')[1])
        

        


print(sum)
