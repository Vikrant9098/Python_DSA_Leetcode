class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []  # store all valid board setups
        board = [["."] * n for _ in range(n)]  # make n x n board filled with '.'

        # check if a queen can be placed safely
        def isSafe(row, col):
            for i in range(row):  # check all rows above
                if board[i][col] == "Q":  # same column has a queen
                    return False

            i, j = row - 1, col - 1  # start from upper-left diagonal
            while i >= 0 and j >= 0:  # move up-left
                if board[i][j] == "Q":  # queen found on upper-left diagonal
                    return False
                i -= 1  # move one row up
                j -= 1  # move one column left

            i, j = row - 1, col + 1  # start from upper-right diagonal
            while i >= 0 and j < n:  # move up-right
                if board[i][j] == "Q":  # queen found on upper-right diagonal
                    return False
                i -= 1  # move one row up
                j += 1  # move one column right

            return True  # safe to place queen

        # try to place queens row by row
        def backtrack(row):
            if row == n:  # all queens are placed
                res.append(["".join(r) for r in board])  # save current board
                return  # go back to try other options

            for col in range(n):  # loop through all columns
                if isSafe(row, col):  # check if current spot is safe
                    board[row][col] = "Q"  # place queen
                    backtrack(row + 1)  # move to next row
                    board[row][col] = "."  # remove queen (backtrack)

        backtrack(0)  # start placing queens from first row
        return res  # return all possible valid boards
