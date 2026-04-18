class Solution(object):
    def reverse(self, n):
        res = 0  # Initialize result to store reversed number
        
        while n > 0:  # Loop until all digits are processed
            res = res * 10 + n % 10  # Append last digit of n to res
            n //= 10  # Remove last digit from n
        
        return res  # Return reversed number

    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Call reverse function and compute absolute difference
        return abs(n - self.reverse(n))