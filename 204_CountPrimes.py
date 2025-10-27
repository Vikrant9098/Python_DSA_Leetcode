class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # If n is less than or equal to 2, there are no primes
        if n <= 2:
            return 0

        # Create a list marking all numbers as prime initially
        is_prime = [True] * n

        # 0 and 1 are not prime numbers
        is_prime[0] = is_prime[1] = False

        # Start checking from 2
        i = 2
        while i * i < n:
            # If i is still marked as prime
            if is_prime[i]:
                # Mark all multiples of i as not prime
                for j in range(i * i, n, i):
                    is_prime[j] = False
            # Move to next number
            i += 1

        # Count all numbers that are still prime
        return sum(is_prime)
