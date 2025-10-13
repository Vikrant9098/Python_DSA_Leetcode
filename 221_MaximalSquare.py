class Solution(object):  # Define the class Solution
    def maximalSquare(self, matrix):  # Define the function with input matrix
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:  # Check if matrix is empty
            return 0  # Return 0 if matrix is empty

        m, n = len(matrix), len(matrix[0])  # Number of rows and columns
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # Create DP table with extra row/column
        max_side = 0  # Initialize max side length of square

        for i in range(1, m + 1):  # Loop through each row starting from 1
            for j in range(1, n + 1):  # Loop through each column starting from 1
                if matrix[i - 1][j - 1] == '1':  # If current cell is '1'
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1  # Update DP value
                    max_side = max(max_side, dp[i][j])  # Update maximum square side

        return max_side * max_side  # Return area of largest square
