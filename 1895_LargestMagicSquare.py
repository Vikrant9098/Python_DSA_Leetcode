class Solution(object):                          # Define the Solution class
    def largestMagicSquare(self, grid):           # Function to find largest magic square
        m, n = len(grid), len(grid[0])            # Get number of rows (m) and columns (n)
        res = 1                                   # Minimum magic square size is 1

        def isValid(i, j, k):                     # Helper function to check k×k square
            s = None                              # Stores the required magic sum

            for x in range(i, i + k):             # Loop through each row in the square
                row = sum(grid[x][j:j + k])       # Calculate sum of current row
                if s is None:                     # If sum not set yet
                    s = row                       # Set magic sum
                elif s != row:                    # If row sum doesn’t match
                    return False                  # Not a magic square

            for y in range(j, j + k):             # Loop through each column in the square
                if sum(grid[x][y] for x in range(i, i + k)) != s:
                    return False                  # Column sum mismatch

            if sum(grid[i + d][j + d] for d in range(k)) != s:
                return False                      # Main diagonal sum mismatch

            if sum(grid[i + d][j + k - 1 - d] for d in range(k)) != s:
                return False                      # Anti-diagonal sum mismatch

            return True                           # All checks passed → magic square

        for k in range(2, min(m, n) + 1):         # Try square sizes from 2 to max possible
            for i in range(m - k + 1):            # Move square vertically
                for j in range(n - k + 1):        # Move square horizontally
                    if isValid(i, j, k):          # Check if current square is magic
                        res = k                   # Update largest magic square size

        return res                                # Return the largest size found
