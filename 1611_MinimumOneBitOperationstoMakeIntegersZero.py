class Solution(object):
    def minimumOneBitOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = n                  # start with the given number
        while n > 0:             # continue until all bits are processed
            n >>= 1              # right shift n by 1 bit
            res ^= n             # XOR res with shifted n to update result
        return res               # final result = minimum number of operations
