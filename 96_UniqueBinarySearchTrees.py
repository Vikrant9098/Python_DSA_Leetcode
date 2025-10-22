class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)  # dp[i] = number of unique BSTs with i nodes
        dp[0] = 1  # Empty tree has 1 structure
        dp[1] = 1  # One node has 1 structure

        for i in range(2, n + 1):  # Calculate for each number of nodes
            for j in range(1, i + 1):  # Choose each node as root
                dp[i] += dp[j - 1] * dp[i - j]  # Left * Right combinations

        return dp[n]  # Return total number of unique BSTs
