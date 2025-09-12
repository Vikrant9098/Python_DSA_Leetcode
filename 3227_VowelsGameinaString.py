class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = set("aeiou")
        
        # Count total vowels in the string
        vowel_count = sum(1 for ch in s if ch in vowels)
        
        # If there are no vowels, Alice cannot make any move, so she loses
        if vowel_count == 0:
            return False
        
        # If there's at least one vowel, Alice can always start
        # by removing a substring with an odd number of vowels
        # and eventually force Bob into a losing position.
        return True
