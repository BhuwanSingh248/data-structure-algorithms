from collections import deque
graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
def bsf(graph=graph, root = 0):
    visited, queue = {root,}, deque([root])

    while queue:
        vertex = queue.popleft()
        print( vertex ,end = '-->' )
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

bsf()
print()

