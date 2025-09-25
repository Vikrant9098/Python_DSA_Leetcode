class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        # dp array of size equal to the last row
        dp = triangle[-1][:]  # copy last row as base case

        # Bottom-up calculation
        for row in range(n - 2, -1, -1):  # start from second last row
            for col in range(row + 1):   # each element in the row
                # Update dp[col] with the min path sum at this point
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])

        # The top element now has the minimum path sum
        return dp[0]
