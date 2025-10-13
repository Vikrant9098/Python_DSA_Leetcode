class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        m = len(word1)  # length of first word
        n = len(word2)  # length of second word

        # dp[i][j] = min operations to convert word1[0..i-1] to word2[0..j-1]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # base cases: empty string conversions
        for i in range(m + 1):
            dp[i][0] = i  # delete all characters
        for j in range(n + 1):
            dp[0][j] = j  # insert all characters

        # fill dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # if characters match, no new operation needed
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # take min of insert, delete, replace
                    dp[i][j] = 1 + min(
                        dp[i - 1][j - 1],  # replace
                        dp[i - 1][j],      # delete
                        dp[i][j - 1]       # insert
                    )

        # final answer at bottom-right
        return dp[m][n]
