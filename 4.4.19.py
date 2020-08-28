dimension = input('Enter dimension: ')
height, width = dimension.split('x')

num = [0,1,2,3,4,5,6,7,8,9]
track = 0
line = []
for i in range(int(height)):
    line = []
    for i in range(int(width)):
        line.append(str(num[track]))
        track += 1
        if track == len(num):
            track = 0
    print(' '.join(line))
