class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.count = 0  # To keep track of total valid solutions
        cols = [False] * n         # Track attacked columns
        diag1 = [False] * (2 * n)  # Track attacked main diagonals (r + c)
        diag2 = [False] * (2 * n)  # Track attacked anti-diagonals (r - c + n)
        
        # Start backtracking from the first row
        def backtrack(row):
            # Base case: all queens are successfully placed
            if row == n:
                self.count += 1
                return
            
            # Try placing a queen in each column of current row
            for col in range(n):
                d1 = row + col        # Main diagonal index
                d2 = row - col + n    # Anti-diagonal index
                
                # Skip if the column or diagonals are already attacked
                if cols[col] or diag1[d1] or diag2[d2]:
                    continue
                
                # Place the queen (mark the attacks)
                cols[col] = diag1[d1] = diag2[d2] = True
                
                # Recurse for the next row
                backtrack(row + 1)
                
                # Backtrack: remove the queen (unmark attacks)
                cols[col] = diag1[d1] = diag2[d2] = False
        
        backtrack(0)  # Start recursion from row 0
        return self.count  # Return the total number of distinct solutions
