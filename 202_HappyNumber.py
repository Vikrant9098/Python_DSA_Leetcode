class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()  # To keep track of numbers we already saw (detect cycles)

        while n != 1 and n not in seen:
            seen.add(n)  # Mark current number as seen
            n = self.getSumOfSquares(n)  # Replace n with sum of squares of its digits

        return n == 1  # True if reached 1, False if cycle detected

    def getSumOfSquares(self, num):
        total = 0
        while num > 0:
            digit = num % 10  # Get last digit
            total += digit * digit  # Add square of digit
            num //= 10  # Remove last digit
        return total
