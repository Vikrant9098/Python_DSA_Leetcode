from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """

        # Get number of rows and columns in the maze
        rows, cols = len(maze), len(maze[0])

        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Queue for BFS, storing (row, col, steps)
        queue = deque()
        start_row, start_col = entrance
        queue.append((start_row, start_col, 0))

        # Mark entrance as visited so we don't consider it again
        maze[start_row][start_col] = '+'

        # Start BFS
        while queue:
            r, c, steps = queue.popleft()

            # Check all four directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc  # New row and column after moving

                # Check if new cell is within bounds and is an empty cell
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '.':
                    # If the new cell is on the border and not the entrance, it's an exit
                    if nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1:
                        return steps + 1  # Found the nearest exit

                    # Mark the cell as visited and add to queue for further BFS
                    maze[nr][nc] = '+'
                    queue.append((nr, nc, steps + 1))

        # If no exit is found
        return -1
