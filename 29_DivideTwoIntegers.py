class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # If overflow case: -2147483648 / -1 = 2147483648 (out of range)
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1  # Return max 32-bit value

        # Check if the result should be negative
        negative = (dividend < 0) ^ (divisor < 0)

        # Take absolute values of both numbers
        a = abs(dividend)
        b = abs(divisor)

        # Store the final answer
        result = 0

        # Repeat until dividend becomes smaller than divisor
        while a >= b:
            temp = b        # Current divisor value
            multiple = 1    # How many times divisor fits

            # Keep doubling temp and multiple while it fits in a
            while a >= (temp << 1):
                temp <<= 1       # Multiply temp by 2 using left shift
                multiple <<= 1   # Multiply multiple by 2 using left shift

            a -= temp            # Subtract largest possible temp from dividend
            result += multiple   # Add corresponding multiple to result

        # Apply the sign to result
        if negative:
            result = -result

        # Clamp result between -2^31 and 2^31 - 1
        result = max(min(result, 2**31 - 1), -2**31)

        # Return the final result
        return result
