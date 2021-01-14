def cost(B):
    c0, c1 = 0, 0
    for i in range(1, len(B)):
        c0, c1 = max(c0, c1+B[i-1]-1), max(c0+B[i]-1, c1+abs(B[i]-B[i-1]))
    return max(c0, c1)


B = [10, 1, 10, 1, 10]
print(cost(B))

