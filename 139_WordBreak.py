class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set(wordDict)  # convert list to set for fast lookup
        n = len(s)
        dp = [False] * (n + 1)    # dp[i] = True if s[0:i] can be segmented
        dp[0] = True  # empty string can always be segmented

        # Check all prefixes
        for i in range(1, n + 1):
            for j in range(i):
                # If s[0:j] can be segmented and s[j:i] is in dictionary
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # no need to check further for this i

        return dp[n]  # return if the entire string can be segmented
