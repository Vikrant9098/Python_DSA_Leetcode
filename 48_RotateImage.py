class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)  # Size of the square matrix
        
        # Step 1: Transpose the matrix
        # Swap elements matrix[i][j] with matrix[j][i] for all i < j
        for i in range(n):            # Iterate over each row
            for j in range(i + 1, n): # Iterate over each column starting from i+1 to avoid double swap
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]  # Swap elements
        
        # Step 2: Reverse each row to complete the 90° clockwise rotation
        for i in range(n):           # Iterate over each row
            matrix[i].reverse()      # Reverse the row in-place
