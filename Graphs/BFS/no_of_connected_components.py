from collections import deque

def count_components(graph, n):

    visited = [False] * n
    count = 0

    for i in range(n):

        if not visited[i]:

            count += 1

            q = deque([i])
            visited[i] = True

            while q:

                u = q.popleft()

                for v in graph[u]:

                    if not visited[v]:
                        visited[v] = True
                        q.append(v)

    return count
