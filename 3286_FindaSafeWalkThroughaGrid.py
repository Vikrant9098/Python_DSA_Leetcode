class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        INF = float('inf')
        dist = [[INF] * n for _ in range(m)]  # Minimum health cost to reach each cell

        dq = deque()
        dist[0][0] = grid[0][0]  # Starting cost includes the first cell
        dq.appendleft((0, 0))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Four possible movement directions

        while dq:
            x, y = dq.popleft()  # Process the next cell with the smallest known cost

            # If destination is reached, check if remaining health is positive
            if x == m - 1 and y == n - 1:
                return dist[x][y] < health

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                # Skip cells outside the grid
                if 0 <= nx < m and 0 <= ny < n:
                    w = grid[nx][ny]  # Cost of entering the neighboring cell

                    # Relax the edge if a lower-cost path is found
                    if dist[x][y] + w < dist[nx][ny]:
                        dist[nx][ny] = dist[x][y] + w

                        # Cost 0 edges are processed first (0-1 BFS optimization)
                        if w == 0:
                            dq.appendleft((nx, ny))
                        else:
                            dq.append((nx, ny))

        # Check whether the destination can be reached within the available health
        return dist[m - 1][n - 1] < health