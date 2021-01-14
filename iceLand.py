# find the number of iceland in the given set of data the iceland ar defined as the continuos 1 in the 2d array we cannot move digonally 



def bfs(a:list, i:int, j:int):
    if i >= len(a) or j >= len(a[i]) or i<0 or j<0 or a[i][j] == "0": return
    a[i][j] = "0"
    bfs(a, i+1, j)
    bfs(a, i, j+1)
    bfs(a, i-1, j)
    bfs(a, i, j-1)

a = ["11000",
"11000",
"00100",
"00011"
]
count = 0
a = list(map(lambda  x: list(x),a))

for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] == "1":
            count += 1
            bfs(a, i, j)
print(count) 

        
