class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf')] * (n + 1)  # dp[i] = minimum number of perfect squares to get sum i
        dp[0] = 0  # base case: 0 needs 0 squares

        for i in range(1, n + 1):  # loop through all numbers from 1 to n
            j = 1
            while j * j <= i:  # try all perfect squares less than or equal to i
                dp[i] = min(dp[i], dp[i - j * j] + 1)  # take min between current and using square j*j
                j += 1

        return dp[n]  # return the minimum number of squares to sum to n
