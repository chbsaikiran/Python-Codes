from collections import deque

def bfs(graph, start):
    visited = set()
    q = deque()

    visited.add(start)
    q.append(start)

    while q:
        node = q.popleft()

        print(node)

        for neigh in graph[node]:
            if neigh not in visited:
                visited.add(neigh)
                q.append(neigh)
