with open('input.txt') as f:
    lines = f.readlines()

cycle = 0
x=1

crt=[]

crt.append([])
crt.append([])
crt.append([])
crt.append([])
crt.append([])
crt.append([])
crt.append([])

def kontrola():
    if (((cycle%40) >= x-1 ) and ((cycle%40) <= x+1)):
        print('#')
        crt[cycle//40].append('#')
    else:
        print('.')
        crt[cycle//40].append('.')


kontrola()

for line in lines:
    if(line == 'noop\n'):
        cycle = cycle +1
        kontrola()
    elif line.split(' ')[0] == 'addx':
        cycle =cycle +1 
        kontrola()
        cycle =cycle +1 

        x=x + int(line.split(' ')[1])
        kontrola()
        

for line in crt:
    print(line)