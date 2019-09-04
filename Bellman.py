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

