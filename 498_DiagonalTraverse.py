class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(mat), len(mat[0])   # number of rows (m), number of cols (n)
        result = []                   # list to store diagonal order
        
        row, col = 0, 0               # starting position
        dir = 1                       # direction: 1 = up-right, -1 = down-left

        while len(result) < m * n:    # loop until we collect all elements
            result.append(mat[row][col])  # add current element
            
            if dir == 1:              # moving up-right
                if col == n - 1:      # if at last column
                    row += 1          # move down
                    dir = -1          # change direction to down-left
                elif row == 0:        # if at top row
                    col += 1          # move right
                    dir = -1          # change direction to down-left
                else:                 # otherwise, move up-right
                    row -= 1
                    col += 1
            else:                     # moving down-left
                if row == m - 1:      # if at last row
                    col += 1          # move right
                    dir = 1           # change direction to up-right
                elif col == 0:        # if at first column
                    row += 1          # move down
                    dir = 1           # change direction to up-right
                else:                 # otherwise, move down-left
                    row += 1
                    col -= 1
        
        return result                 # return final diagonal order
