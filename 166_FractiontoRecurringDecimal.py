class Solution:
    def fractionToDecimal(self, numerator, denominator):
        # If numerator is 0, the result is always "0"
        if numerator == 0:
            return "0"
        
        # Use a list to build the result string step by step
        result = []
        
        # Check if result should be negative (XOR → true if only one is negative)
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")
        
        # Convert numerator and denominator to positive (absolute values)
        num = abs(numerator)
        den = abs(denominator)
        
        # Add the integer part of the division to result
        result.append(str(num // den))
        
        # Get the remainder after dividing
        remainder = num % den
        
        # If remainder is 0 → it's a whole number, return directly
        if remainder == 0:
            return "".join(result)
        
        # Otherwise, add a decimal point for fractional part
        result.append(".")
        
        # Dictionary to map remainder → position in result
        remainder_map = {}
        
        # Loop until remainder becomes 0 or repeats
        while remainder != 0:
            # If remainder already seen → repeating fraction found
            if remainder in remainder_map:
                # Get index where this remainder first appeared
                index = remainder_map[remainder]
                # Insert "(" at that index
                result.insert(index, "(")
                # Add ")" at the end
                result.append(")")
                # Stop, since we found the cycle
                break
            
            # Store current remainder with current result length
            remainder_map[remainder] = len(result)
            
            # Multiply remainder by 10 to get next digit
            remainder *= 10
            
            # Append next quotient digit
            result.append(str(remainder // den))
            
            # Update remainder
            remainder %= den
        
        # Join list into final string and return
        return "".join(result)
