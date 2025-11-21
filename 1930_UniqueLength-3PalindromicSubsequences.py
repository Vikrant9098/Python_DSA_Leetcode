class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)               # length of the string
        result = 0               # final count of palindromes

        # check for every character from 'a' to 'z'
        for ch in map(chr, range(ord('a'), ord('z') + 1)):
            left = -1            # first index of ch
            right = -1           # last index of ch

            # find first and last occurrence of ch
            for i in range(n):
                if s[i] == ch:   # if current character equals ch
                    if left == -1:
                        left = i # set first occurrence
                    right = i    # always update last occurrence

            # ensure at least two same ends and middle space exists
            if left != -1 and right != -1 and right - left > 1:
                visited = set()  # set to store unique middle characters

                # collect all characters between left and right
                for j in range(left + 1, right):
                    visited.add(s[j])   # add char to set (unique)

                result += len(visited)  # add unique middle characters count

        return result            # return the final result
