class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # If lengths differ, t cannot be an anagram of s
        if len(s) != len(t):
            return False

        freq = [0] * 26  # Frequency array for letters a-z

        # Count letters in s and subtract letters in t
        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1  # Increment count for s
            freq[ord(t[i]) - ord('a')] -= 1  # Decrement count for t

        # Check if all counts are zero
        for count in freq:
            if count != 0:
                return False  # Not an anagram if any count is non-zero

        return True  # All counts zero → valid anagram