class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Handle negative powers
        N = n
        if N < 0:
            x = 1 / x   # reciprocal for negative exponent
            N = -N      # make exponent positive

        result = 1.0  # initial result

        # Fast exponentiation loop
        while N > 0:
            if N % 2 == 1:   # if exponent is odd
                result *= x  # multiply result by base
            x *= x           # square the base
            N //= 2          # divide exponent by 2

        # Return final result
        return result
