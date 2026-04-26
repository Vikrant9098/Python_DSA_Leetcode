class Solution(object):
    def containsCycle(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """

        # Define Union-Find (Disjoint Set) inside the function
        class UnionFind(object):
            def __init__(self, n):
                self.n = n                      # Total number of nodes (cells)
                self.parent = list(range(n))   # Each node is initially its own parent
                self.size = [1] * n            # Size of each set is initially 1

            def findset(self, x):
                # If x is not the parent of itself
                if self.parent[x] != x:
                    # Recursively find root and compress path
                    self.parent[x] = self.findset(self.parent[x])
                return self.parent[x]          # Return root parent

            def unite(self, x, y):
                # If size of x is smaller than size of y
                if self.size[x] < self.size[y]:
                    x, y = y, x               # Swap so that x is always larger

                self.parent[y] = x            # Make x the parent of y
                self.size[x] += self.size[y]  # Increase size of x's component

            def findAndUnite(self, x, y):
                parentX = self.findset(x)     # Find root of x
                parentY = self.findset(y)     # Find root of y

                # If both have same parent → already connected → cycle
                if parentX == parentY:
                    return False              # Cycle detected

                self.unite(parentX, parentY)  # Otherwise, merge the sets
                return True                  # Successfully united (no cycle)

        m, n = len(grid), len(grid[0])        # Get number of rows and columns

        uf = UnionFind(m * n)                 # Create UF for all cells (flattened)

        # Traverse each cell in the grid
        for i in range(m):
            for j in range(n):

                # Check upward neighbor (i-1, j)
                if i > 0 and grid[i][j] == grid[i - 1][j]:
                    # Convert 2D index (i, j) to 1D index → i*n + j
                    # Same for (i-1, j)
                    if not uf.findAndUnite(i * n + j, (i - 1) * n + j):
                        return True          # If already connected → cycle found

                # Check left neighbor (i, j-1)
                if j > 0 and grid[i][j] == grid[i][j - 1]:
                    # Convert both cells to 1D index and try to unite
                    if not uf.findAndUnite(i * n + j, i * n + j - 1):
                        return True          # If already connected → cycle found

        return False                         # No cycle found in entire grid