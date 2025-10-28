class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # if string is empty or has one char, it's already a palindrome
        if not s or len(s) == 1:
            return s

        # reverse the string
        rev = s[::-1]

        # join original and reversed with a separator
        combined = s + "#" + rev

        # get the LPS array for combined string
        lps = self.buildLPS(combined)

        # longest palindrome prefix length
        longest_pal_prefix = lps[-1]

        # find part to add in front from reversed string
        add = rev[:len(s) - longest_pal_prefix]

        # return the final shortest palindrome
        return add + s

    def buildLPS(self, pattern):
        """
        Helper function to build LPS (Longest Prefix Suffix) array
        """
        n = len(pattern)           # length of string
        lps = [0] * n              # create LPS array
        length = 0                 # track prefix length
        i = 1                      # start from second char

        # loop to fill LPS array
        while i < n:
            if pattern[i] == pattern[length]:  # if chars match
                length += 1                    # increase length
                lps[i] = length                # store in LPS
                i += 1                         # move forward
            else:
                if length > 0:                 # if mismatch, try shorter prefix
                    length = lps[length - 1]
                else:                          # if no match
                    lps[i] = 0                 # set 0
                    i += 1                     # move forward
        return lps                             # return final LPS array
