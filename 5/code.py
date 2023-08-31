with open('input.txt') as f:
    lines = f.readlines()

sklad=[]


pocetStani=len(lines[0])//4

skladIndex=0
i=0
while(skladIndex == 0):
    if('move' in lines[i]):
        skladIndex=i-3
    i=i+1

i=0
while(i < pocetStani):
    j=skladIndex
    while(j >= 0):
        sklad.append([])
        if(lines[j][i*4:i*4+3] != '   '):
            sklad[i].append(lines[j][i*4:i*4+3])
        j+=1
    i=i+1



prvnimove = skladIndex +3

jjj=0
while(prvnimove+jjj < len(lines)):
    ukol = lines[prvnimove+jjj].split(' ')
    kolik = int(ukol[1])
    z = int(ukol[3])
    do = int(ukol[5])
    while(kolik > 0):
        sklad[do-1].append(sklad[z-1][len(sklad[z-1])-1])
        sklad[z-1].pop()
        kolik = kolik -1
    jjj=jjj+1



ppp =0
while(ppp < len(sklad)):
    print(sklad[ppp])
    ppp=ppp+1