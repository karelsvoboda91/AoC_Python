with open('input.txt') as f:
    lines = f.readlines()

map= []

delkaradku = len(lines[0])-1
cesty= [([10000]*delkaradku) for i in range(len(lines))]

pozice=[]
body=[]
hotoveBody=[]
vzdalenost=0

finx = 0
finy = 0

for i in range(len(lines)):
    map.append(lines[i])
    if "S" in lines[i]:
        pozice.append([i, lines[i].find('S')])
    if "E" in lines[i]:
        finy = i

finx=map[finy].find('E')

map[finy]=map[finy].replace('E', 'z')

cesty[pozice[0][0]][pozice[0][1]] = 0
map[pozice[0][0]] = map[pozice[0][0]].replace('S', 'a')
hotoveBody.append(pozice[0])

print('start=' + str(pozice[0][0]) + ' ' + str(pozice[0][1]) )
print('fin=' + str(finx) + ' ' + str(finy) )

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

f = open("mapa.txt", "w")
for radek in cesty:
    f.write(str(radek) + '\n')
f.close()

for radek in cesty:
    print(radek)

print(cesty[finy][finx])