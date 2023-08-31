with open('input.txt') as f:
    lines = f.readlines()

soubory=set()
cesty=set()
cesta =  '/'
x=0

for i in range(len(lines)):
    if '$ cd' in lines[i]  and lines[i] != '$ cd ..\n' and lines[i] != '$ cd /\n':
        cesta=cesta + '/' + lines[i].split(' ')[2]
        cesty.add(cesta)
    if lines[i] == '$ cd /\n':
        cesta = '/'
    if lines[i] == '$ cd ..\n':
        cesta=cesta[0:cesta.rfind('/')]
    if '$ ls' in lines[i]:
        i=i+1
        while('$' not in lines[i]):
            if(lines[i].split(' ')[0] != 'dir'):
                soubory.add(cesta + ' ' + lines[i])
            i=i+1
            if i >= len(lines):
                break
        i=i-1

bonus= 10000000000

for cesta in cesty:
    velikostslozky = 0
    for soubor in soubory:
        if cesta in soubor:
            velikostslozky = velikostslozky + int(soubor.split(' ')[-2])
    if velikostslozky >= 358913 and velikostslozky < bonus:
        bonus = velikostslozky

print(bonus)