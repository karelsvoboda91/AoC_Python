with open('input.txt') as f:
    lines = f.readlines()

finx = 0
finy = 0


for i in range(len(lines)):
    if "E" in lines[i]:
        finy = i

finx=lines[finy].find('E')

print('fin=' + str(finx) + ' ' + str(finy) )

min = 10000


starts= []

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == 'a':
            starts.append([i,j])

print(starts)
for start in starts:

    map= []
    delkaradku = len(lines[0])-1
    cesty= [([10000]*delkaradku) for i in range(len(lines))]
    pozice=[]
    pozice.append(start)
    body=[]
    hotoveBody=[]
    vzdalenost=0

    for i in range(len(lines)):
        map.append(lines[i])
        if "E" in lines[i]:
            finy = i

    finx=map[finy].find('E')

    map[finy]=map[finy].replace('E', 'z')

    cesty[pozice[0][0]][pozice[0][1]] = 0

    hotoveBody.append(pozice[0])




    for pozi in pozice:
        vzdalenost = cesty[pozi[0]][pozi[1]] +1

        if(pozi[0] - 1 >= 0 ):
            if [pozi[0] - 1, pozi[1]] not in hotoveBody:
                body.insert(0, [pozi[0] - 1, pozi[1]])
        if(pozi[0] + 1 < len(lines)):
            if [pozi[0] + 1, pozi[1]] not in hotoveBody:
                body.insert(0, [pozi[0] + 1, pozi[1]])
        if(pozi[1] - 1 >= 0):
            if [pozi[0], pozi[1] - 1] not in hotoveBody:
                body.insert(0, [pozi[0], pozi[1] - 1])
        if(pozi[1] + 1 < delkaradku):
            if [pozi[0], pozi[1] +1] not in hotoveBody:
                body.insert(0, [pozi[0], pozi[1] + 1])

        for bod in body:
            if (ord(map[bod[0]][bod[1]]) -1) <=  (ord(map[pozi[0]][pozi[1]])):
                #přidá se pozice
                pozice.append([bod[0], bod[1]])
                cesty[bod[0]][bod[1]] = vzdalenost
                hotoveBody.append(bod)
        body = []
    if cesty[finy][finx] < min:
        min = cesty[finy][finx]


print(min)