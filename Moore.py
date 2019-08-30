def Moore(P, D):
    n = len(D)
    X = [-1] * n
    Y = [-1] * n
    Z = []
    for i in range(n):
        X[i] = D[i]
    for i in range(n):
        Y[i] = X.index(min(X))
        X[X.index(min(X))] = float('inf')

    L = 0
    C = 0
    LJ = []
    for i in range(n):
        C = C + P[Y[i]]
        L = C - D[Y[i]]
        Z.append(Y[i])
        if L > 0:
            A = [0] * len(Z)
            for j in range(len(Z)):
                A[j] = P[Z[j]]
            max = A[0]
            maxIndex = 0
            for k in range(1, len(A)):
                if A[k] > max:
                    max = A[k]
                    maxIndex = k
            LJ.append(Z[maxIndex])
            Z.remove(Z[maxIndex])
            C = 0
            for x in Z:
                C = C + P[x]
    print("P: ", end="")
    S = 0
    E = 0
    count = 0
    for i in Z:
        j = i + 1
        S = E
        E = E + P[i]
        count += 1
        if count != len(Z):
            print("J_{} ({},{}), ".format(j, S, E), end="")
        else:
            print("J_{} ({},{}) ".format(j, S, E), end="")
    print("| ", end="")
    count = 0
    for i in LJ:
        j = i + 1
        S = E
        E = E + P[i]
        count += 1
        if count != len(LJ):
            print("J_{} ({},{}), ".format(j, S, E), end="")
        else:
            print("J_{} ({},{}) ".format(j, S, E), end="")

