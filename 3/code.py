with open('input.txt') as f:
    lines = f.readlines()

vobou=[]
i=0
radek=0

while(i < len(lines)):
    j=0
    while(j < len(lines[i])/2):
        l=0
        while(l < len(lines[i])/2):
            if(lines[i][j] == lines[i][(len(lines[i])//2)+l]):
                if(radek == 0):
                    vobou.append(lines[i][j])
                radek=1
            l=l+1
        j=j+1
    i=i+1
    radek=0

print(vobou)

sum=0
o=0
while(o < len(vobou)):

    if(ord(vobou[o])> 64 and ord(vobou[o]) < 91 ):
        sum=sum+ord(vobou[o])-38
    else:
        sum=sum+ord(vobou[o])-96

    o=o+1

print(sum)