class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        c = 0
        
        # XOR ASCII values of all characters in s
        for cs in s:
            c ^= ord(cs)   # ord() gives ASCII value
        
        # XOR ASCII values of all characters in t
        for ct in t:
            c ^= ord(ct)
        
        # Convert ASCII value back to character
        return chr(c)   # chr() converts ASCII to character