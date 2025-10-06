class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])  # Get number of rows and columns

        # DFS helper function to check from (row, col) if we can form word[index:]
        def dfs(row, col, index):
            if index == len(word):  # All characters matched
                return True
            # Check boundaries and current character match
            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != word[index]:
                return False

            temp = board[row][col]  # Store original character
            board[row][col] = '#'   # Mark cell as visited

            # Explore all 4 directions: down, up, right, left
            found = (dfs(row + 1, col, index + 1) or
                     dfs(row - 1, col, index + 1) or
                     dfs(row, col + 1, index + 1) or
                     dfs(row, col - 1, index + 1))

            board[row][col] = temp  # Restore original character (backtrack)
            return found  # Return True if word found in any direction

        # Start DFS from every cell in the board
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):  # If word found starting from this cell
                    return True
        return False  # Word not found in the entire board
