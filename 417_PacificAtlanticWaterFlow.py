class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        # If matrix is empty, return nothing
        if not heights or not heights[0]:
            return []

        # Get number of rows and columns
        rows, cols = len(heights), len(heights[0])

        # Sets to store cells reachable by Pacific and Atlantic oceans
        pacific = set()
        atlantic = set()

        # DFS function to explore reachable cells
        def dfs(r, c, visit, prevHeight):
            # Stop if cell is out of bounds, already visited, or height is lower
            if ((r, c) in visit or
                r < 0 or c < 0 or r >= rows or c >= cols or
                heights[r][c] < prevHeight):
                return

            # Mark current cell as visited
            visit.add((r, c))

            # Move in all four directions
            dfs(r + 1, c, visit, heights[r][c])  # down
            dfs(r - 1, c, visit, heights[r][c])  # up
            dfs(r, c + 1, visit, heights[r][c])  # right
            dfs(r, c - 1, visit, heights[r][c])  # left

        # Start DFS for Pacific Ocean (top row and left column)
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])              # top edge
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])  # bottom edge

        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])              # left edge
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])  # right edge

        # Find cells reachable by both oceans
        result = list(pacific & atlantic)

        # Return list of coordinates
        return result
