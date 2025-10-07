"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        # start building the quad tree from the full grid
        return self.build(grid, 0, 0, len(grid))

    # helper function to build the Quad Tree
    def build(self, grid, row, col, size):
        # check if the current sub-grid has all same values
        if self.isUniform(grid, row, col, size):
            # create and return a leaf node with that value
            return Node(grid[row][col] == 1, True)

        # divide the grid into 4 smaller equal parts
        newSize = size // 2

        # build top-left part recursively
        topLeft = self.build(grid, row, col, newSize)

        # build top-right part recursively
        topRight = self.build(grid, row, col + newSize, newSize)

        # build bottom-left part recursively
        bottomLeft = self.build(grid, row + newSize, col, newSize)

        # build bottom-right part recursively
        bottomRight = self.build(grid, row + newSize, col + newSize, newSize)

        # create a non-leaf node with four children
        return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)

    # helper function to check if sub-grid has same values
    def isUniform(self, grid, row, col, size):
        # store the first cell value
        val = grid[row][col]

        # loop through all cells in the sub-grid
        for i in range(row, row + size):
            for j in range(col, col + size):
                # if any value is different, not uniform
                if grid[i][j] != val:
                    return False
        
        # all cells are same → uniform grid
        return True
