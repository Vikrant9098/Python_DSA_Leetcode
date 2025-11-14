class Solution(object):                     # define class
    def rangeAddQueries(self, n, queries):  # define function
        mat = [[0] * n for _ in range(n)]   # create n x n matrix of zeros

        for top, left, bottom, right in queries:  # loop through each query
            mat[top][left] += 1                   # add +1 at start point

            if right + 1 < n:                     # check right boundary
                mat[top][right + 1] -= 1          # subtract to stop effect on right

            if bottom + 1 < n:                    # check bottom boundary
                mat[bottom + 1][left] -= 1        # subtract to stop effect below

            if bottom + 1 < n and right + 1 < n:  # check bottom-right boundary
                mat[bottom + 1][right + 1] += 1   # fix double subtract

        for i in range(n):                        # loop rows
            for j in range(1, n):                 # loop columns (start from 1)
                mat[i][j] += mat[i][j - 1]        # add previous left value

        for j in range(n):                        # loop columns
            for i in range(1, n):                 # loop rows (start from 1)
                mat[i][j] += mat[i - 1][j]        # add previous top value

        return mat                                # return final matrix
