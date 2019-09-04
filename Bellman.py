def Bellman(V, E, s):
    dist = [float('inf')] * len(V)
    dist[s] = 0
    print("Initialization: ", dist)

    topSort = [0] * len(V)
    topOrder = []
    temp = []
    for i in range(len(E)):
        topSort[E[i][1]] += 1
    while len(topOrder) < len(V):
        for i in range(len(V)):
            if topSort[i] == 0:
                topSort[i] = -1
                topOrder.append(i)
                temp.append(i)
        for j in temp:
            for k in range(len(E)):
                if j == E[k][0]:
                    topSort[E[k][1]] -= 1
            temp.remove(j)
    print("Order from TopSort: ", topOrder)

    count = 1
    for i in topOrder:
        print("Phase: ", count)
        for j in range(len(E)):
            if i == E[j][0]:
                if dist[E[j][1]] > dist[E[j][0]] + E[j][2]:
                    print("\tRelaxed edge ({}, {})".format(i, E[j][1]))
                    dist[E[j][1]] = dist[E[j][0]] + E[j][2]
        print("\tDistance: ", dist)
        count += 1

    print("Final distance = ", dist)


V = [0, 1, 2, 3, 4, 5, 6]
E = [[1, 0, 9], [1, 2, -3], [1, 3, -2], [2, 0 ,2], [3, 0, 9], [3,5, 4], [3,6,5], [4,1,5], [4,2,-8],[4,3,8],[5,6,12],[6,2,-8]]
s = 4
Bellman(V, E, s)
print("=========================")
V = [0, 1, 2, 3, 4, 5, 6,7,8]
E = [[0,1,1], [1, 2, 1], [2, 3, 1], [0, 4 ,8], [3,7,1], [4,5,2], [5,6,4], [6,7,1], [4,8,3],[8,7,5]]
s = 0
Bellman(V, E, s)
print("=========================")
V = [0,1,2,3,4,5,6]
E = [[0,1,1],[0,5,6],[0,6,9],[1,2,1],[1,3,3],[1,4,9],[1,5,8],[3,2,1],[3,4,-6],[4,5,6],[5,6,-10]]
s = 0
Bellman(V, E, s)
print("=========================")
