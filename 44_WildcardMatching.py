class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)             # Lengths of string and pattern

        # dp[i][j] = True if first i chars of s match first j chars of p
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True                   # Empty string matches empty pattern

        # Initialize first row: empty string vs pattern
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]   # '*' can match empty sequence

        # Fill dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                sc = s[i - 1]             # Current char in string
                pc = p[j - 1]             # Current char in pattern

                if pc == sc or pc == '?': # Match character or '?'
                    dp[i][j] = dp[i - 1][j - 1]  # Take diagonal value
                elif pc == '*':           # If pattern is '*'
                    # '*' matches empty (dp[i][j-1]) or one/more chars (dp[i-1][j])
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

        return dp[m][n]                   # Return final result
