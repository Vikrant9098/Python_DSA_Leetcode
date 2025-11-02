class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        # get number of rows and columns
        m, n = len(matrix), len(matrix[0])

        # create prefix matrix with one extra row and column
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]

        # fill prefix sum matrix
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # sum = current value + top + left - overlap
                self.prefix[i][j] = (
                    matrix[i - 1][j - 1]          # current cell value
                    + self.prefix[i - 1][j]       # add top cell
                    + self.prefix[i][j - 1]       # add left cell
                    - self.prefix[i - 1][j - 1]   # subtract overlap area
                )

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
d sum of give/*************  ✨ Windsurf Command ⭐  *************/
    """
    Compute the sum of all elements in the rectangle defined by (row1,col1) and (row2,col2)
    using the prefix sum matrix computed in __init__.
    """
/*******  57347b48-f90a-484c-a85e-ebd728802214  *******/n rectangle using prefix sums
        return (
            self.prefix[row2 + 1][col2 + 1]   # total area sum
            - self.prefix[row1][col2 + 1]     # remove top part
            - self.prefix[row2 + 1][col1]     # remove left part
            + self.prefix[row1][col1]         # add overlap back
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
