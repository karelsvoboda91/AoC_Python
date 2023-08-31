with open('input2.txt') as f:
    lines = f.readlines()


def jepole(pole): # je to pole?
    if(pole[0] == '['):
        pole = pole[1:pole.rfind(']')].split(',')
    
    for i in range(len(pole)):
        flag = False
        try:
            int(pole[1])
        except ValueError:
            flag = True # neni číslo
            print('tohle neni cislo')
        if flag:
            pole[1] = jepole(pole[1])
    return pole

    


prvni = lines[0]
druhy = lines[1]


prvni = jepole(prvni)

print(prvni)


