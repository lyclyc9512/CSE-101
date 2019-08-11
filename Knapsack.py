def Knapsack(n, c, V, W):
    maxV = totalW = totalV = 0
    R = [0] * n
    for b in range(pow(2, n)):
        X = [int(d) for d in bin(b)[2:].zfill(n)]
        for i in range(n):
            if X[i] == 1:
                totalV += V[i]
                totalW += W[i]
        if totalW <= c and maxV <= totalV:
            maxV = totalV
            for j in range(n):
                R[j] = X[j]
        totalW = totalV = 0
    return R
