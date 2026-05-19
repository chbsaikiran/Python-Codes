from collections import deque

def shortest_grid(grid, sr, sc):

    rows = len(grid)
    cols = len(grid[0])

    dist = [[-1]*cols for _ in range(rows)]

    dirs = [
        (-1,0),
        (1,0),
        (0,-1),
        (0,1)
    ]

    q = deque()

    q.append((sr, sc))
    dist[sr][sc] = 0

    while q:

        r, c = q.popleft()

        for dr, dc in dirs:

            nr = r + dr
            nc = c + dc

            if 0 <= nr < rows and 0 <= nc < cols:

                if grid[nr][nc] == 0 and dist[nr][nc] == -1:

                    dist[nr][nc] = dist[r][c] + 1

                    q.append((nr, nc))
