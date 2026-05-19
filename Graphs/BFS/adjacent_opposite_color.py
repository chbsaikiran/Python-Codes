from collections import deque

def is_bipartite(graph, n):

    color = [-1] * n

    for start in range(n):

        if color[start] == -1:

            q = deque([start])
            color[start] = 0

            while q:

                u = q.popleft()

                for v in graph[u]:

                    if color[v] == -1:

                        color[v] = 1 - color[u]
                        q.append(v)

                    elif color[v] == color[u]:
                        return False

    return True
