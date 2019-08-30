def ListScheduling(P, m):
    pro = [0] * m
    X = [[] for y in range(m)]
    for i in range(len(P)):
        index = pro.index(min(pro))
        pro[index] += P[i]
        X[index].append(i)

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

