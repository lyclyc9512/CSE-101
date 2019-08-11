def BubbleSort(A):
    if len(A) == 1:
        return A
    for k in range(len(A)-1):
        for j in range(len(A)-k-1):
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
    return A
