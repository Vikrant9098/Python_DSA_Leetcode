class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Get number of rows
        m = len(matrix)
        # Get number of columns
        n = len(matrix[0])

        # Left pointer at start of flattened matrix
        left = 0
        # Right pointer at end of flattened matrix
        right = m * n - 1

        # Binary search loop
        while left <= right:
            # Find the middle index
            mid = (left + right) // 2

            # Convert mid index to row and column
            row = mid // n
            col = mid % n

            # Check if the middle element is the target
            if matrix[row][col] == target:
                return True
            # If middle element is smaller, search right half
            elif matrix[row][col] < target:
                left = mid + 1
            # If middle element is larger, search left half
            else:
                right = mid - 1

        # Target not found
        return False
