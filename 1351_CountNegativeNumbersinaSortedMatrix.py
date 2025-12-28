class Solution(object):                     # Define the Solution class
    def countNegatives(self, grid):          # Method to count negative numbers
        count = 0                            # Store count of negative elements

        for i in range(len(grid)-1, -1, -1): # Loop rows from last to first
            for j in range(len(grid[0])-1, -1, -1): # Loop columns from last to first
                if grid[i][j] < 0:           # Check if the element is negative
                    count += 1               # Increase count if negative

        return(count)                        # Return total negative count
