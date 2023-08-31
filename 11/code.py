with open('input.txt') as f:
    lines = f.readlines()

round = 0

class Monkey:
  def __init__(self, number, items, multiply, opNumber, test, ifYes, ifFalse, activity):
    self.number = number
    self.items = items
    self.multiply = multiply
    self.opNumber = opNumber
    self.test = test
    self.ifYes = ifYes
    self.ifFalse = ifFalse
    self.activity = activity

  def pridat(self, polozka):
    self.items.append(polozka)

  def inspekce(self):
    polozky = []
    for item in self.items:
        self.activity = self.activity + 1
        hodnota = 0
        adresa = 0
        if(self.multiply):
            if(self.opNumber != 'old'):
                hodnota = item * int(self.opNumber)
            else:
                hodnota = item * item
        else:
            if(self.opNumber != 'old'):
                hodnota = item + int(self.opNumber)
            else:
                hodnota = item + item
        #hodnota = hodnota // 3
        ###########################################################
        if hodnota > 100000000000000000000000000000000000000000000000000000000:
            #deleni = [23, 19 , 13, 17]
            deleni = [ 19, 17, 13, 11, 7, 5, 3, 2]

            for i in range(0,10000000):
                ok = 1
                for dele in deleni:
                    if hodnota % dele != i % dele:
                        ok = 0
                        break
                if i == 9999999:
                    print("jsme v loji")
                if ok == 1:
                    hodnota = i
                    break
        ###########################################################

        if(hodnota % self.test == 0):
            adresa = self.ifYes
        else:
            adresa = self.ifFalse

        polozky.append([hodnota, adresa])
    
    self.items = []
    return polozky


MonkeyUnit = []

for i in range(0,len(lines),7):
    MonkeyUnit.append ( Monkey(
        int(lines[i].split(' ')[1][0]),
        [int(i) for i in lines[i+1].split(':')[1].split(',')],
        lines[i+2].split(' ')[-2] == '*' and True or False,
        lines[i+2].split(' ')[-1][0:-1],
        int(lines[i+3].split(' ')[-1]),
        int(lines[i+4].split(' ')[-1]),
        int(lines[i+5].split(' ')[-1]),
        0))


for xxx in range(10000):
    print(xxx)
    for i in range(len(MonkeyUnit)):
        polozky2 = MonkeyUnit[i].inspekce()
        for polozka in polozky2:
            MonkeyUnit[polozka[1]].pridat(polozka[0])


for opice in range(len(MonkeyUnit)):
    print(' ')
    #print(MonkeyUnit[opice].number)
    #print(MonkeyUnit[opice].items)
    #print(MonkeyUnit[opice].multiply)
    #print(MonkeyUnit[opice].opNumber)
    #print(MonkeyUnit[opice].test)
    #print(MonkeyUnit[opice].ifYes)
    #print(MonkeyUnit[opice].ifFalse)
    print(MonkeyUnit[opice].activity)