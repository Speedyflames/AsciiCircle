import math

while True:
    rad = int(input('Radius:  '))

    graph = [['`' for i in range((rad + 1) * 2)] for i in range(((rad + 1) * 2))]

    for i in range((rad + 1)):
        y = round(math.sqrt((rad**2) - ((i - rad)**2)) + rad)
        graph[i][y] = '*'
        graph[-i][y] = '*'

    for i in range((rad + 1)):
        y = round(-(math.sqrt((rad**2) - ((i - rad)**2)) + rad))
        graph[i][y] = '*'
        graph[-i][y] = '*'


    graph.append([' ' for i in range((rad + 1) * 2)])
    
    graph[0][rad], graph[0][-rad] = ' ',' '
    graph[0][rad + 2], graph[0][-rad - 2] = '*','*'
    graph[-1][rad + 2], graph[-1][-rad - 2] = '*','*'
    graph[rad + 1][1], graph[rad + 1][-1] = '*','*'

    
    for i in range(((rad + 1) * 2) + 1):
        print('`'.join(graph[i]))


                                         
