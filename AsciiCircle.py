import math

while True:
    rad = int(input('Radius:  '))

    graph = [[' ' for i in range((rad*2) + 1)] for i in range(((rad*2) + 1))]

    for i in range((rad + 1)):
        y = round(math.sqrt((rad**2) - ((i - rad)**2)) + rad)
        graph[i][y] = '*'
        graph[-i][y] = '*'
        graph[i][-y] = '*'
        graph[-i][-y] = '*'
    
    for i in range(((rad*2) + 1)):
        print(' '.join(graph[i]))


                                         

