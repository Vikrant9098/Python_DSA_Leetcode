class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Start from top-right corner
        row = 0
        col = len(matrix[0]) - 1

        # Loop while inside matrix bounds
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True  # found the target
            elif matrix[row][col] > target:
                col -= 1  # move left if current value is too big
            else:
                row += 1  # move down if current value is too small

        # Target not found
        return False
