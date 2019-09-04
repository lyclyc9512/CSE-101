def Floyd(V, E):
    n = len(V)
    d = [[float('inf') for x in range(n)] for y in range(n)]
    print("Initialization:")
    for v in V:
        d[v][v] = 0
    for e in range(len(E)):
        d[E[e][0]][E[e][1]] = E[e][2]
    for x in range(n):
        print(d[x])
    print()
    for k in range(n):
        print("Phase {} (use Vertex {}):".format(k + 1, k))
        for i in range(n):
            print("[", end="")
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    if j != n - 1:
                        print("*{}*".format(d[i][j]), end=", ")
                    else:
                        print("*{}*".format(d[i][j]), end="")
                else:
                    if j != n - 1:
                        print(d[i][j], end=", ")
                    else:
                        print(d[i][j], end="")
            print("]")
        print()

    print("Final distance:")
    for x in range(n):
        print(d[x])
