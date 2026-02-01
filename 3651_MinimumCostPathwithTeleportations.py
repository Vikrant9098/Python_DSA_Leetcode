import heapq  # Used for priority queue (min-heap)

class Solution(object):
    def minCost(self, grid, k):
        """
        grid : 2D matrix of costs
        k    : maximum number of teleports allowed
        """

        # Number of rows and columns
        m, n = len(grid), len(grid[0])

        # Store grid in a named variable (as required)
        lurnavrethy = grid  

        # --------------------------------------------------
        # Collect all cells as (value, row, col)
        # This helps process teleports in sorted order
        # --------------------------------------------------
        cells = []
        for r in range(m):              # Loop through rows
            for c in range(n):          # Loop through columns
                cells.append((lurnavrethy[r][c], r, c))

        # Sort cells by their value (ascending)
        cells.sort()

        # --------------------------------------------------
        # Min-heap for Dijkstra
        # (currentCost, row, col, teleportsUsed)
        # --------------------------------------------------
        pq = [(0, 0, 0, 0)]

        # --------------------------------------------------
        # dist[r][c][t] = minimum cost to reach (r,c)
        # using exactly t teleports
        # --------------------------------------------------
        dist = [[[float('inf')] * (k + 1) for _ in range(n)] for _ in range(m)]

        # Starting point cost is 0 with 0 teleports used
        dist[0][0][0] = 0

        # Allowed normal moves: down and right
        directions = [(1, 0), (0, 1)]

        # --------------------------------------------------
        # teleport_ptr[t] tells how many cells have already
        # been processed for teleport count = t
        # --------------------------------------------------
        teleport_ptr = [0] * (k + 1)

        # --------------------------------------------------
        # Dijkstra's algorithm loop
        # --------------------------------------------------
        while pq:
            # Get state with minimum cost
            cost, r, c, used = heapq.heappop(pq)

            # If destination is reached, return answer
            if r == m - 1 and c == n - 1:
                return cost

            # Ignore outdated states
            if cost > dist[r][c][used]:
                continue

            # ==================================================
            # 1. NORMAL MOVES (Right / Down)
            # ==================================================
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check grid boundaries
                if 0 <= nr < m and 0 <= nc < n:
                    # Cost to enter next cell
                    new_cost = cost + lurnavrethy[nr][nc]

                    # Relax edge if cheaper path is found
                    if new_cost < dist[nr][nc][used]:
                        dist[nr][nc][used] = new_cost
                        heapq.heappush(pq, (new_cost, nr, nc, used))

            # ==================================================
            # 2. TELEPORT MOVES
            # ==================================================
            if used < k:  # Only if teleports are still available

                # Process all cells whose value
                # is <= current cell value
                while (teleport_ptr[used] < len(cells) and
                       cells[teleport_ptr[used]][0] <= lurnavrethy[r][c]):

                    _, tr, tc = cells[teleport_ptr[used]]

                    # Teleport does NOT add cell cost
                    if cost < dist[tr][tc][used + 1]:
                        dist[tr][tc][used + 1] = cost
                        heapq.heappush(pq, (cost, tr, tc, used + 1))

                    # Move pointer so cell is not reused
                    teleport_ptr[used] += 1

        # If destination cannot be reached
        return -1
