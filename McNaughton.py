import math

def McNaughton(P, m):
    p_sum = 0
    for p in P:
        p_sum += p
    c_max = max(math.ceil(p_sum/m), max(P))

    start = 0
    end = 0
    processor = 1
    print("P_{}: ".format(processor), end="")
    for i in range(len(P)):
        start = end
        end += P[i]
        while end > c_max:
            print("J_{} ({},{}) ".format(i+1, start, c_max), end="")
            start = 0
            end = end - c_max
            processor += 1
            print("\nP_{}: ".format(processor), end="")
        if end < c_max:
            if i == len(P) - 1:
                print("J_{} ({},{}) ".format(i+1, start, end), end="")
            else:
                print("J_{} ({},{}), ".format(i + 1, start, end), end="")
        if end == c_max:
            print("J_{} ({},{}) ".format(i+1, start, c_max), end="")
            end = 0
            processor += 1
            print("\nP_{}: ".format(processor), end="")

