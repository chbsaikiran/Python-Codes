from collections import deque

def bfs_shortest(graph, src, n):

    dist = [-1] * n
    parent = [-1] * n

    q = deque()

    dist[src] = 0
    q.append(src)

    while q:

        u = q.popleft()

        for v in graph[u]:

            if dist[v] == -1:

                dist[v] = dist[u] + 1
                parent[v] = u

                q.append(v)

    return dist, parent
    

def get_path(parent, target):

    path = []

    while target != -1:
        path.append(target)
        target = parent[target]

    path.reverse()

    return path
