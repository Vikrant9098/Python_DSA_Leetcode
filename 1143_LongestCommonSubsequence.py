class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        m = len(text1)  # length of first string
        n = len(text2)  # length of second string

        # create dp table of size (m+1) x (n+1) filled with 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # loop over each character of both strings
        for i in range(1, m + 1):
            for j in range(1, n + 1):

                # if characters match, add 1 to diagonal value
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    # else take max from top or left cell
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # return the final answer from bottom-right cell
        return dp[m][n]
