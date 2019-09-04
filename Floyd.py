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



V = [0, 1, 2, 3, 4]
E = [[0,1,3],[0,3,6],[1,3,2],[1,4,4],[2,0,3],[3,2,1],[3,4,1]]
Floyd(V, E)

V = [0,1,2,3]
E = [[0,1,5],[0,3,11],[1,2,3],[2,1,2],[2,3,2]]
Floyd(V, E)
