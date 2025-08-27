class Solution:
    # 4 diagonal directions (row, col):
    #  ↘ (down-right), ↙ (down-left), ↖ (up-left), ↗ (up-right)
    DIRS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

    def lenOfVDiagonal(self, grid):
        m, n = len(grid), len(grid[0])   # number of rows and columns

        # memo[i][j][mask] = best result starting from (i, j) with a given state
        # mask = (direction << 1) | canTurn
        # - direction (0..3) is stored in higher bits
        # - canTurn (0 or 1) means if turn is still available
        memo = [[[0] * (1 << 3) for _ in range(n)] for _ in range(m)]

        ans = 0  # stores maximum V-shaped length found

        # Try starting from each cell in the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:  # must start with 1
                    continue

                # max possible steps in each direction (used as pruning)
                maxs = [m - i, j + 1, i + 1, n - j]

                # try all 4 diagonal directions from this starting 1
                for k in range(4):
                    if maxs[k] > ans:  # only if possible length can beat current ans
                        # +1 for the starting cell
                        ans = max(ans, self.dfs(i, j, k, 1, 2, grid, memo) + 1)

        return ans

    def dfs(self, i, j, k, canTurn, target, grid, memo):
        m, n = len(grid), len(grid[0])

        # move one step in current direction k
        i += self.DIRS[k][0]
        j += self.DIRS[k][1]

        # if out of bounds OR not matching expected value → stop
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != target:
            return 0

        # create a mask to uniquely identify state = (dir, canTurn)
        mask = (k << 1) | canTurn

        # return cached result if already computed
        if memo[i][j][mask] > 0:
            return memo[i][j][mask]

        # option 1: keep going straight in same direction
        res = self.dfs(i, j, k, canTurn, 2 - target, grid, memo)

        # option 2: if we still have a turn available
        if canTurn == 1:
            # max steps possible in new direction (for pruning)
            maxs = [m - i - 1, j, i, n - j - 1]

            # turn clockwise → new direction
            nk = (k + 1) % 4

            # only explore turn if potentially beneficial
            if maxs[nk] > res:
                res = max(res, self.dfs(i, j, nk, 0, 2 - target, grid, memo))

        # store result (+1 for current cell) in memo
        memo[i][j][mask] = res + 1
        return memo[i][j][mask]
