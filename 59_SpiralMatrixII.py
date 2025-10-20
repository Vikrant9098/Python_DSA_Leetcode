class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for _ in range(n)]  # Create an n x n matrix filled with 0
        left, right = 0, n - 1  # Set left and right boundaries
        top, bottom = 0, n - 1  # Set top and bottom boundaries
        num = 1  # Start filling numbers from 1

        # Keep filling until all numbers are placed
        while left <= right and top <= bottom:
            # Fill the top row from left to right
            for i in range(left, right + 1):
                matrix[top][i] = num  # Place number in current cell
                num += 1
            top += 1  # Move top boundary down

            # Fill the right column from top to bottom
            for i in range(top, bottom + 1):
                matrix[i][right] = num  # Place number in current cell
                num += 1
            right -= 1  # Move right boundary left

            # Fill the bottom row from right to left
            if top <= bottom:  # Check if bottom row still exists
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = num  # Place number in current cell
                    num += 1
                bottom -= 1  # Move bottom boundary up

            # Fill the left column from bottom to top
            if left <= right:  # Check if left column still exists
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num  # Place number in current cell
                    num += 1
                left += 1  # Move left boundary right

        return matrix  # Return the filled spiral matrix
