hodnota = 310

deleni = [23, 19 , 13, 17]
#deleni = [ 19, 17, 13, 11, 7, 5, 3, 2]
zbytky = []

for dele in deleni:
    zbytky.append(hodnota % dele)

print(zbytky)


x = 1
done = 0
for i in range(1,100):
    for j in range(1,100):
        for k in range(1,100):
            for l in range(1,100):
                if (i*deleni[0])+zbytky[0] == (j*deleni[1])+zbytky[1] and (j*deleni[1])+zbytky[1]  == (k*deleni[2])+zbytky[2] and  (j*deleni[1])+zbytky[1]  == (l*deleni[2])+zbytky[2]:
                    x= (i*deleni[0])+zbytky[0]
                    done = 1
                    break
            if(done == 1):
                break
        if(done == 1):
            break
    if(done == 1):
        break



zbytky =[]

for dele in deleni:
    zbytky.append(x % dele)

print(zbytky)