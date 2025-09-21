class Solution(object):  # Define a class Solution
    def gameOfLife(self, board):  # Main method to update the board in-place
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])  # Get number of rows and columns in board

        # All 8 possible neighbor directions (up, down, left, right, diagonals)
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        # Step 1: Traverse each cell
        for r in range(rows):  # Loop over all rows
            for c in range(cols):  # Loop over all columns
                live_neighbors = 0  # Counter for live neighbors

                # Step 2: Count live neighbors
                for dr, dc in directions:  # For each direction
                    nr, nc = r + dr, c + dc  # Neighbor row and column
                    # Check if neighbor is inside grid and if it is alive (1 or -1)
                    if 0 <= nr < rows and 0 <= nc < cols and abs(board[nr][nc]) == 1:
                        live_neighbors += 1  # Increase live neighbor count

                # Step 3: Apply Game of Life rules
                # Rule 1 or Rule 3 → live cell dies (mark as -1 for now)
                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = -1
                # Rule 4 → dead cell becomes alive (mark as 2 for now)
                if board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 2

        # Step 4: Final update of the board
        for r in range(rows):  # Loop again over rows
            for c in range(cols):  # Loop again over columns
                # Any positive value (1 or 2) becomes alive (1)
                if board[r][c] > 0:
                    board[r][c] = 1
                # Any non-positive value (0 or -1) becomes dead (0)
                else:
                    board[r][c] = 0
