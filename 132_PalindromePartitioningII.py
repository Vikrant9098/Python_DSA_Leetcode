class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # DP table to check if s[i..j] is palindrome
        isPalindrome = [[False]*n for _ in range(n)]
        # cuts[i] = minimum cuts for substring s[0..i]
        cuts = [0]*n

        for i in range(n):
            minCut = i  # maximum cuts = cut before every character
            for j in range(i+1):
                # Check if s[j..i] is palindrome
                if s[i] == s[j] and (i - j <= 1 or isPalindrome[j+1][i-1]):
                    isPalindrome[j][i] = True
                    if j == 0:
                        minCut = 0  # whole substring s[0..i] is palindrome
                    else:
                        minCut = min(minCut, cuts[j-1] + 1)  # cut before j
            cuts[i] = minCut  # store minimum cuts for s[0..i]

        return cuts[n-1]  # minimum cuts for the whole string
