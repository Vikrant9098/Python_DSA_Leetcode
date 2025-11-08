class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MASK = 0xFFFFFFFF        # mask to get last 32 bits
        MAX_INT = 0x7FFFFFFF     # max positive 32-bit integer
        
        while b != 0:            # repeat until there's no carry
            carry = (a & b) << 1  # calculate carry bits
            a = (a ^ b) & MASK    # add without carry (XOR) and apply mask
            b = carry & MASK      # keep carry within 32 bits
        
        # if a > MAX_INT, it's a negative number in 32-bit form
        return a if a <= MAX_INT else ~(a ^ MASK)
