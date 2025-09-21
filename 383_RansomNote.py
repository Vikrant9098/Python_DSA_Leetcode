class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Array to count frequency of letters (26 lowercase letters)
        count = [0] * 26

        # Count letters in magazine
        for c in magazine:
            count[ord(c) - ord('a')] += 1

        # Check if ransomNote can be formed
        for c in ransomNote:
            if count[ord(c) - ord('a')] == 0:  # Letter not available
                return False
            count[ord(c) - ord('a')] -= 1      # Use one occurrence

        return True  # All letters available
