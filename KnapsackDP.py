def KnapsackDP(n, c, V, W):
    f = [[0 for x in range(c+1)] for y in range(n)]

    for k in range(n):
        f[k][0] = 0

    for i in range(n):
        for k in range(1, c+1):
            if k >= W[i]:
                f[i][k] = max(f[i-1][k-W[i]]+V[i], f[i-1][k])
            else:
                f[i][k] = f[i-1][k]

    X = [0 for x in range(n)]
    l = c
    for i in range(n-1, -1, -1):
        if f[i][l] == f[i-1][l]:
            pass
        elif f[i][l] > f[i-1][l]:
            X[i] = 1
            l = l - W[i]

    print("Optimal Value is: ", f[n-1][c])
    return X

