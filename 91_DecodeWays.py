class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)  # Get length of string
        if n == 0 or s[0] == '0':  # If empty or starts with 0, invalid
            return 0

        dp = [0] * (n + 1)  # DP array to store ways
        dp[0] = 1  # Base case: empty string has 1 way
        dp[1] = 1  # First char (not '0') has 1 way

        for i in range(2, n + 1):  # Loop through string
            one = int(s[i - 1])  # Take single digit
            two = int(s[i - 2:i])  # Take two digits

            if one >= 1:  # Valid single digit (1–9)
                dp[i] += dp[i - 1]
            if 10 <= two <= 26:  # Valid two digits (10–26)
                dp[i] += dp[i - 2]

        return dp[n]  # Return total number of ways
