class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:               # Step 1: Negative numbers and 0 are not ugly
            return False

        for p in [2, 3, 5]:      # Step 2: Check prime factors 2, 3, and 5
            while n % p == 0:    # Divide n by p as long as possible
                n //= p

        return n == 1            # Step 3: If n becomes 1, it’s an ugly number
