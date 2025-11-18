class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0  # pointer to scan bits
        
        # iterate until the second last bit
        while i < len(bits) - 1:
            if bits[i] == 1:
                i += 2   # two-bit character (10 or 11)
            else:
                i += 1   # one-bit character (0)
        
        # if we stop exactly at last index -> last char is one-bit
        return i == len(bits) - 1
