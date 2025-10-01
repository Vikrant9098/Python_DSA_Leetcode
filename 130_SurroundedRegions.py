class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        rows = len(board)
        cols = len(board[0])
        
        # DFS function to mark safe 'O's
        def dfs(i, j):
            # base case: out of bounds or not 'O'
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != 'O':
                return
            # mark current 'O' as safe
            board[i][j] = 'S'
            # explore all 4 directions
            dfs(i + 1, j)  # down
            dfs(i - 1, j)  # up
            dfs(i, j + 1)  # right
            dfs(i, j - 1)  # left
        
        # mark all border 'O's and connected regions as safe
        for i in range(rows):
            dfs(i, 0)        # left border
            dfs(i, cols - 1) # right border
        
        for j in range(cols):
            dfs(0, j)        # top border
            dfs(rows - 1, j) # bottom border
        
        # flip captured 'O's to 'X' and safe 'S's back to 'O'
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'  # captured
                elif board[i][j] == 'S':
                    board[i][j] = 'O'  # safe
