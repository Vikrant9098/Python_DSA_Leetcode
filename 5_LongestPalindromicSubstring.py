class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) < 1:  # if string is empty or length < 1
            return ""             # return empty string

        start, end = 0, 0        # store start and end indices of longest palindrome

        def expand(left, right):  # helper function to expand around center
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1         # move left pointer outward
                right += 1        # move right pointer outward
            return right - left - 1  # length of palindrome

        for i in range(len(s)):   # loop through each character as center
            len1 = expand(i, i)       # check odd length palindrome
            len2 = expand(i, i + 1)   # check even length palindrome
            max_len = max(len1, len2) # take the longer palindrome
            if max_len > end - start: # update longest palindrome if needed
                start = i - (max_len - 1) // 2  # new start index
                end = i + max_len // 2          # new end index

        return s[start:end + 1]   # return longest palindromic substring
