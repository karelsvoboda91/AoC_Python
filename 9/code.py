with open('input.txt') as f:
    lines = f.readlines()

tailPositions = set()


head = [0,0]
tail = [0,0]


for line in lines:
    direction= line.split(' ')[0]
    count = int(line.split(' ')[1])

    for i in range(count):

        lastHeadX = head[0]
        lastHeadY = head[1]

        if(direction == 'U'):
            head[1] = head[1] + 1
        if(direction == 'D'):
            head[1] = head[1] - 1
        if(direction == 'R'):
            head[0] = head[0] + 1
        if(direction == 'L'):
            head[0] = head[0] - 1
        
        if(abs(head[0] - tail[0]) > 1  or abs(head[1] - tail[1]) > 1 ):
            tail[0]=lastHeadX
            tail[1]=lastHeadY
        tailPositions.add(str(tail))
        



print(len(tailPositions))