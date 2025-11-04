class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # get number of rows
        m = len(matrix)
        # get number of columns
        n = len(matrix[0])

        # create memo table to store longest path from each cell
        memo = [[0] * n for _ in range(m)]

        # directions for up, down, left, and right
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # define dfs function to find path length from cell (i, j)
        def dfs(i, j):
            # if result already stored, return it
            if memo[i][j] != 0:
                return memo[i][j]

            # start with path length 1 (current cell)
            max_len = 1

            # explore all 4 directions
            for dx, dy in dirs:
                # new cell coordinates
                x, y = i + dx, j + dy
                # check if inside matrix and increasing
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    # get length from next cell and update max
                    max_len = max(max_len, 1 + dfs(x, y))

            # store longest path for this cell
            memo[i][j] = max_len
            # return path length from this cell
            return max_len

        # variable to keep track of overall longest path
        result = 0

        # loop through each cell in matrix
        for i in range(m):
            for j in range(n):
                # compute longest path from this cell
                result = max(result, dfs(i, j))

        # return longest path found
        return result
