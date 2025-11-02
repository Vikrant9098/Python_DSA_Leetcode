class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        # create grid of m x n
        grid = [[0] * n for _ in range(m)]

        # mark guards as 1
        for r, c in guards:
            grid[r][c] = 1

        # mark walls as 2
        for r, c in walls:
            grid[r][c] = 2

        # directions: up, down, left, right
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        # for each guard
        for r, c in guards:
            # move in all directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # move until wall or guard found
                while 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 1 and grid[nr][nc] != 2:
                    # mark as guarded if empty
                    if grid[nr][nc] == 0:
                        grid[nr][nc] = 3
                    # move further in same direction
                    nr += dr
                    nc += dc

        # count unguarded cells
        count = 0
        for i in range(m):
            for j in range(n):
                # if cell is empty (0), count it
                if grid[i][j] == 0:
                    count += 1

        # return total unguarded cells
        return count
