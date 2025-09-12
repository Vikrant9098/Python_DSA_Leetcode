class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        
        if not matrix or not matrix[0]:
            return result
        
        top, bottom = 0, len(matrix) - 1   # Top and bottom boundaries
        left, right = 0, len(matrix[0]) - 1 # Left and right boundaries
        
        # Traverse layer by layer
        while top <= bottom and left <= right:
            # Traverse top row from left to right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1  # Move top boundary down
            
            # Traverse right column from top to bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1  # Move right boundary left
            
            # Traverse bottom row from right to left, if still valid
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1  # Move bottom boundary up
            
            # Traverse left column from bottom to top, if still valid
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1  # Move left boundary right
        
        return result
