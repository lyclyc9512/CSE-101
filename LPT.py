def LPT(P, m):
    pro = [0] * m
    temp = [-1] * len(P)
    P_time = []
    P_index = []
    X = [[] for y in range(m)]
    for i in range(len(P)):
        temp[i] = P[i]
    for i in range(len(temp)):
        max = temp[0]
        maxIndex = 0
        for k in range(1, len(temp)):
            if temp[k] > max:
                max = temp[k]
                maxIndex = k
        P_time.append(max)
        P_index.append(maxIndex)
        temp[maxIndex] = -1

    for i in range(len(P)):
        index = pro.index(min(pro))
        pro[index] += P_time[i]
        X[index].append(P_index[i])

    print("P_{}: ".format(1), end="")
    for y in range(m):
        start = 0
        end = 0
        if y != 0:
            print("\nP_{}: ".format(y + 1), end="")
        for x in range(len(X[y])):
            start = end
            end += P[X[y][x]]
            if x != len(X[y]) - 1:
                print("J_{} ({},{}),".format(X[y][x] + 1, start, end), end=" ")
            else:
                print("J_{} ({},{})".format(X[y][x] + 1, start, end), end=" ")

