class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        count = 0
        
        # Compare each row with each column
        for i in range(n):
            for j in range(n):
                # Get row i
                row = grid[i]
                
                # Get column j
                col = [grid[k][j] for k in range(n)]
                
                # Check if row and column are equal
                if row == col:
                    count += 1
        
        return count