def AssignmentBB(n, C):
    UB = 0
    listRow = [-1] * n
    listCol = [-1] * n
    for i in range(n):
        min = 0
        for x in range(n):
            for y in range(n):
                if x not in listRow and y not in listCol:
                    if min != 0 and C[x][y] < min:
                        min = C[x][y]
                        j = x
                        k = y
                    elif min == 0:
                        min = C[x][y]
                        j = x
                        k = y
        UB += min
        listRow[i] = j
        listCol[i] = k
    print("UB1 = ", UB, "\n")

    nodeList = [[-1 for x in range(n+1)]]
    nodeList[0][n] = 1
    nodeNum = 1
    upperCount = 1

    while len(nodeList) != 0:
        if nodeList[0][n] == 0:
            nodeList.remove(nodeList[0])
        else:
            LB = tempLB = tempUB = 0
            nodeList[0][n] = 0
            static = []
            for a in range(n):
                if nodeList[0][a] != -1:
                    static.append(nodeList[0][a])
            for b in range(len(static)):
                for c in static:
                    tempLB += C[b][c]

            for i in range(n):
                if i in static:
                    pass
                else:
                    print("Node ", nodeNum, ":")
                    nodeNum += 1
                    LB = tempLB
                    LB += C[len(static)][i]
                    for x in range(len(static)+1, n):
                        min = float("inf")
                        for y in range(n):
                            if y not in static and y != i:
                                if C[x][y] < min:
                                    min = C[x][y]
                        LB += min
                    print("\t- LB: ", LB)
                    if LB >= UB:
                        print("\t- LB(%s) >= UB%s(%s)" % (LB, upperCount, UB))
                    else:
                        tempUB = tempLB + C[len(static)][i]
                        listRow = [-1] * (n-len(static))
                        listCol = [-1] * (n-len(static))
                        for d in range(n-len(static)-1):
                            min = 0
                            for x in range(len(static)+1, n):
                                for y in range(n):
                                    if y not in listCol and y not in static:
                                        if x not in listRow and y != i:
                                            if min != 0 and C[x][y] < min:
                                                min = C[x][y]
                                                j = x
                                                k = y
                                            elif min == 0:
                                                min = C[x][y]
                                                j = x
                                                k = y
                            tempUB += min
                            listRow[d] = j
                            listCol[d] = k
                        print("\t- UB: ", tempUB)
                        if tempUB < UB:
                            UB = tempUB
                            upperCount += 1
                            print("\t- new upper bound UB%s(%s)" % (upperCount, UB))
                            X = [[0 for x in range(n)] for y in range(n)]
                            p = 0
                            for q in static:
                                X[p][q] = 1
                                p += 1
                            X[p][i] = 1
                            for s in range(len(listRow)):
                                if listRow[s] != -1:
                                    p = listRow[s]
                                    q = listCol[s]
                                    X[p][q] = 1
                        if LB < tempUB:
                            newNode = []
                            for z in nodeList[0]:
                                newNode.append(z)
                            newNode[n] = 1
                            newNode[len(static)] = i
                            nodeList.append(newNode)
                        else:
                            print("\t- LB(%s) >= UB%s(%s)" % (LB, upperCount, UB))
            print()
    print("Lowest UpperBound = UB%s(%s)" %(upperCount, UB))
    print("X = ")
    for x in range(n):
        print(X[x])
    return X

