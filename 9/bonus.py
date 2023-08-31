with open('input.txt') as f:
    lines = f.readlines()

tailPositions = set()

knots = 10
rope = []

#visibility= [([0]*10) for i in range(10)]

for i in range(knots):
    rope.append([0, 0])


for line in lines:
    direction= line.split(' ')[0]
    count = int(line.split(' ')[1])

    for i in range(count):

        if(direction == 'U'):
            rope[0][1] = rope[0][1] + 1
        if(direction == 'D'):
            rope[0][1] = rope[0][1] - 1
        if(direction == 'R'):
            rope[0][0] = rope[0][0] + 1
        if(direction == 'L'):
            rope[0][0] = rope[0][0] - 1

        #visibility= [([0]*10) for i in range(10)]
        for knot in range(knots-1):         
            if(abs(rope[knot][0] - rope[knot+1][0]) > 1  or abs(rope[knot][1] - rope[knot+1][1]) > 1 ):

                if(rope[knot][0] > rope[knot+1][0] ):
                    rope[knot+1][0]=rope[knot+1][0]+1
                elif(rope[knot][0] < rope[knot+1][0]):
                    rope[knot+1][0]=rope[knot+1][0]-1

                if(rope[knot][1] > rope[knot+1][1] ):
                    rope[knot+1][1]=rope[knot+1][1]+1
                elif(rope[knot][1] < rope[knot+1][1]):
                    rope[knot+1][1]=rope[knot+1][1]-1


            if knot == 8:           
                tailPositions.add(str(rope[9]))           
            #visibility[rope[knot][0]][rope[knot][1]]=1

        #for line in visibility:
        #    print(line)

       # print(' ')
        




print(tailPositions)

print(len(tailPositions))