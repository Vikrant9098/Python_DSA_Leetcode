class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0  # variable to store the reversed bits

        # iterate over all 32 bits
        for i in range(32):
            result <<= 1          # shift result left to make space for next bit
            result |= n & 1       # add the least significant bit of n to result
            n >>= 1               # shift n right to process the next bit

        return result  # return the integer with reversed bits
