class Solution(object):   # Define a class named Solution (inherits from object in Python 2 style)
    def getNoZeroIntegers(self, n):   # Define a function that takes an integer n
        """
        :type n: int                  # Tells that n is an integer (for documentation, not functional)
        :rtype: List[int]             # Tells that the function will return a list of integers
        """
        # Try all possible values of a from 1 to n-1
        for a in range(1, n):         # Loop from 1 up to n-1
            b = n - a                 # b is chosen so that a + b = n
            if self.isNoZero(a) and self.isNoZero(b):  # Check if both a and b are no-zero integers
                return [a, b]         # If yes, return them as a list

    # Helper function to check if a number has no zero
    def isNoZero(self, num):          # Define a helper function that checks a number
        while num > 0:                # Loop through each digit of num
            if num % 10 == 0:         # If the last digit is zero
                return False          # Number is not valid (contains zero)
            num //= 10                # Remove the last digit and continue
        return True                   # If no digit was zero, return True
