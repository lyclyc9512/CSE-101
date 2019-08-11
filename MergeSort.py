
def MergeSort(A):
    if len(A) == 1:
        return A
    else:
        mid = int(len(A)/2)
        B = A[:mid]
        C = A[mid:]
        MergeSort(B)
        MergeSort(C)

        i = j = k = 0
        while k < len(B) and j < len(C):
            if B[k] <= C[j]:
                A[i] = B[k]
                k += 1
            else:
                A[i] = C[j]
                j += 1
            i += 1

        while k < len(B) or j < len(C):
            if k < len(B):
                A[i] = B[k]
                k += 1
            else:
                A[i] = C[j]
                j += 1
            i += 1
        return A
