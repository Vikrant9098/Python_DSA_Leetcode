class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # Get the lengths of both strings
        m, n = len(s), len(t)

        # Create a 2D DP array (m+1) x (n+1) filled with 0
        # dp[i][j] means: number of ways to form t[0..j-1] from s[0..i-1]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base case: empty t ("") can always be formed from any prefix of s
        for i in range(m + 1):
            dp[i][0] = 1

        # Fill the DP table
        for i in range(1, m + 1):          # Loop through s
            for j in range(1, n + 1):      # Loop through t
                # If current characters match
                if s[i - 1] == t[j - 1]:
                    # Option 1: use this character  (dp[i-1][j-1])
                    # Option 2: skip this character (dp[i-1][j])
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    # If not match, skip s[i-1]
                    dp[i][j] = dp[i - 1][j]

        # The bottom-right cell has the final count of distinct subsequences
        return dp[m][n]
