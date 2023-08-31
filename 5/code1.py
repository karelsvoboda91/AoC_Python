;with open('input.txt') as f:
    lines = f.readlines()

max=0
i=0
elfici=[]

while(i < len(lines)):
    elf=0
    while(lines[i] != '\n'):
        elf=elf+int(lines[i])
        i=i+1
        if(i >= len(lines)):
            break
    if(elf > max):
        max=elf
    i=i+1
    elfici.append(elf)

elfici.sort()

print((elfici[len(elfici)-1]+elfici[len(elfici)-2]+elfici[len(elfici)-3] ))

print(elfici)
print(max)