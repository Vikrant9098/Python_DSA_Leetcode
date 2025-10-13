class Solution(object):  # Define the class Solution
    def isInterleave(self, s1, s2, s3):  # Define the function with three string inputs
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # If total length doesn't match, return False
        if len(s1) + len(s2) != len(s3):
            return False

        # Create a 2D DP table filled with False
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True  # Empty s1 and s2 make empty s3

        # Fill first row (only using s2)
        for j in range(1, len(s2) + 1):  # Loop over s2
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]  # Check if s2 builds s3

        # Fill first column (only using s1)
        for i in range(1, len(s1) + 1):  # Loop over s1
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]  # Check if s1 builds s3

        # Fill the rest of the DP table
        for i in range(1, len(s1) + 1):  # Loop over each char in s1
            for j in range(1, len(s2) + 1):  # Loop over each char in s2
                # Check if current char of s3 matches from s1 or s2
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                           (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])

        # Return the final result from bottom-right of DP table
        return dp[len(s1)][len(s2)]
