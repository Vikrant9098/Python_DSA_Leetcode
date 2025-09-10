class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        h_len, n_len = len(haystack), len(needle)

        # If needle is longer than haystack, impossible to find
        if n_len > h_len:
            return -1

        # Loop through haystack until there's enough room for needle
        for i in range(h_len - n_len + 1):
            # Compare substring with needle
            if haystack[i:i + n_len] == needle:
                return i  # Found at index i

        # If not found
        return -1
