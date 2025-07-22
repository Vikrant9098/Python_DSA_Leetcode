from collections import deque  # Importing deque for efficient queue operations (used in BFS)

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]  → 2D grid representing the box of oranges
        :rtype: int                  → Minimum number of minutes until all oranges are rotten
        """

        rows, cols = len(grid), len(grid[0])  # Get the number of rows and columns in the grid

        queue = deque()  # Initialize a queue for BFS to keep track of rotten oranges
        fresh = 0        # Counter to keep track of how many fresh oranges are there

        # Step 1: Traverse the grid to find initial rotten oranges and count fresh ones
        for r in range(rows):                # Iterate through each row
            for c in range(cols):            # Iterate through each column
                if grid[r][c] == 2:          # Rotten orange found
                    queue.append((r, c, 0))  # Add to queue with time 0 (initial minute)
                elif grid[r][c] == 1:        # Fresh orange found
                    fresh += 1               # Increment the count of fresh oranges

        # These are the 4 possible directions (up, down, left, right) for BFS traversal
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        time = 0  # Variable to store the time taken to rot all reachable oranges

        # Step 2: Start BFS from all initially rotten oranges
        while queue:
            row, col, t = queue.popleft()  # Get the current orange's position and time
            time = max(time, t)           # Track the maximum time so far during BFS

            # Try to rot neighboring fresh oranges in all four directions
            for dr, dc in directions:
                newRow, newCol = row + dr, col + dc  # Calculate new cell coordinates

                # Check if new cell is inside grid and contains a fresh orange
                if (0 <= newRow < rows and 0 <= newCol < cols and grid[newRow][newCol] == 1):
                    grid[newRow][newCol] = 2         # Mark the orange as rotten
                    fresh -= 1                       # Decrease fresh orange count
                    queue.append((newRow, newCol, t + 1))  # Enqueue it with increased time

        # Step 3: After BFS, check if any fresh orange is left unrotted
        if fresh > 0:
            return -1  # Impossible to rot all oranges → return -1

        return time    # Return the time it took to rot all oranges
