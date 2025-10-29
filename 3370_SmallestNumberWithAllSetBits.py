class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        bits = 1  # start with 1 bit
        num = 1   # number with all bits set for 1 bit (binary "1")
        
        # loop until num becomes greater than or equal to n
        while num < n:
            bits += 1              # increase bit count
            num = (1 << bits) - 1  # make a number with all bits set (like 111 -> 7)
        
        return num  # return the smallest number with all bits set >= n
