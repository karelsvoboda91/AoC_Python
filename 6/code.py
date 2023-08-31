with open('input.txt') as f:
    lines = f.readlines()
delka =14
i=0
while(i < len(lines[0])-delka):
    ok = 1
    prvek=delka
    while(prvek > 1):
        j=1
        while(j < prvek ):
            if(lines[0][i + delka-prvek] == lines[0][i+ delka-prvek+j]):
                ok =0
            j=j+1
        prvek= prvek-1
    if(ok == 1):
        print(i + delka)
        break
    i+=1