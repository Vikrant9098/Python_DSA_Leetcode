class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """

        # Disjoint Set (Union-Find) to connect valid cells
        class DisjointSet:
            def __init__(self, n):
                # Initially each node is its own parent
                self.parent = list(range(n))

            def find(self, x):
                # Path compression optimization
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def merge(self, x, y):
                # Connect two components
                self.parent[self.find(x)] = self.find(y)

        m, n = len(grid), len(grid[0])
        ds = DisjointSet(m * n)

        # Convert 2D index → 1D index
        def getId(x, y):
            return x * n + y

        # Check LEFT connection
        def detectL(x, y):
            if y - 1 >= 0 and grid[x][y - 1] in [1, 4, 6]:
                ds.merge(getId(x, y), getId(x, y - 1))

        # Check RIGHT connection
        def detectR(x, y):
            if y + 1 < n and grid[x][y + 1] in [1, 3, 5]:
                ds.merge(getId(x, y), getId(x, y + 1))

        # Check UP connection
        def detectU(x, y):
            if x - 1 >= 0 and grid[x - 1][y] in [2, 3, 4]:
                ds.merge(getId(x, y), getId(x - 1, y))

        # Check DOWN connection
        def detectD(x, y):
            if x + 1 < m and grid[x + 1][y] in [2, 5, 6]:
                ds.merge(getId(x, y), getId(x + 1, y))

        # Based on street type, try valid directions
        def handler(x, y):
            if grid[x][y] == 1:       # left ↔ right
                detectL(x, y)
                detectR(x, y)
            elif grid[x][y] == 2:     # up ↕ down
                detectU(x, y)
                detectD(x, y)
            elif grid[x][y] == 3:     # left + down
                detectL(x, y)
                detectD(x, y)
            elif grid[x][y] == 4:     # right + down
                detectR(x, y)
                detectD(x, y)
            elif grid[x][y] == 5:     # left + up
                detectL(x, y)
                detectU(x, y)
            else:                    # type 6 → right + up
                detectR(x, y)
                detectU(x, y)

        # Process every cell
        for i in range(m):
            for j in range(n):
                handler(i, j)

        # Check if start and end are connected
        return ds.find(getId(0, 0)) == ds.find(getId(m - 1, n - 1))