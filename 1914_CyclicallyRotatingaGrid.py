class Solution(object):
    def rotateGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])

        # Number of layers in the grid
        nlayer = min(m // 2, n // 2)

        # Process each layer one by one
        for layer in range(nlayer):

            # Store row indices, column indices, and values of the current layer
            r = []
            c = []
            val = []

            # Traverse left side
            for i in range(layer, m - layer - 1):
                r.append(i)
                c.append(layer)
                val.append(grid[i][layer])

            # Traverse bottom side
            for j in range(layer, n - layer - 1):
                r.append(m - layer - 1)
                c.append(j)
                val.append(grid[m - layer - 1][j])

            # Traverse right side
            for i in range(m - layer - 1, layer, -1):
                r.append(i)
                c.append(n - layer - 1)
                val.append(grid[i][n - layer - 1])

            # Traverse top side
            for j in range(n - layer - 1, layer, -1):
                r.append(layer)
                c.append(j)
                val.append(grid[layer][j])

            # Total elements in the current layer
            total = len(val)

            # Effective rotations needed
            kk = k % total

            # Place rotated values back into the grid
            for i in range(total):

                # Find the corresponding rotated index
                idx = (i + total - kk) % total

                grid[r[i]][c[i]] = val[idx]

        return grid