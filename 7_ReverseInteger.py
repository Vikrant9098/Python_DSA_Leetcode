class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        """
        Reverse the digits of a 32-bit signed integer.
        Return 0 if the reversed integer overflows.
        """
        # Define the 32-bit signed integer range limits
        INT_MIN = -2**31      # -2147483648
        INT_MAX = 2**31 - 1   # 2147483647
        
        # Handle the sign separately - store if number is negative
        sign = -1 if x < 0 else 1
        
        # Work with absolute value to make digit extraction easier
        x = abs(x)
        
        # Initialize result to store the reversed number
        result = 0
        
        # Process each digit from right to left
        while x != 0:
            # Extract the last digit using modulo operation
            digit = x % 10
            
            # Remove the last digit from x using integer division
            x = x // 10
            
            # Check for overflow BEFORE actually updating result
            # If result > (INT_MAX - digit) / 10, then result * 10 + digit > INT_MAX
            if result > (INT_MAX - digit) // 10:
                return 0  # Overflow detected, return 0
            
            # Build the reversed number by shifting left and adding new digit
            # This is equivalent to: result = result * 10 + digit
            result = result * 10 + digit
        
        # Apply the original sign to the result
        result = result * sign
        
        # Final check: ensure the result is within 32-bit signed integer range
        if result < INT_MIN or result > INT_MAX:
            return 0
        
        return result




            