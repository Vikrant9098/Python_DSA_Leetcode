import math


class Solution(object):

    def minOperations(self, s, k):
        
        zero = 0                      # Variable to count number of '0's in the string
        len_s = len(s)                # Store length of string
        
        # Count number of zeros in the string
        for i in range(len_s):
            zero += ~ord(s[i]) & 1    # Clever trick:
                                      # For '0' -> adds 1
                                      # For '1' -> adds 0
        
        # If no zeros exist, no operation is needed
        if zero == 0:
            return 0
        
        # Special case: if string length equals k
        if len_s == k:
            # If all characters are zero -> return 1
            # Otherwise return -1
            return ((1 if zero == len_s else 0) << 1) - 1
        
        base = len_s - k              # Remaining part after selecting k
        
        # Calculate minimum operations assuming result must be odd
        odd = max(
            int(math.ceil(float(zero) / k)),              # Minimum groups needed to fix zeros
            int(math.ceil(float(len_s - zero) / base))    # Minimum groups needed to fix ones
        )
        
        odd += ~odd & 1               # Ensure odd is actually odd (if even, add 1)
        
        # Calculate minimum operations assuming result must be even
        even = max(
            int(math.ceil(float(zero) / k)),              # Fix zeros
            int(math.ceil(float(zero) / base))            # Fix zeros in remaining part
        )
        
        even += even & 1              # Ensure even is actually even (if odd, add 1)
        
        res = float('inf')            # Initialize result with infinity
        
        # If parity of k matches parity of zero count
        if (k & 1) == (zero & 1):
            res = min(res, odd)       # Consider odd case
        
        # If zero count is even
        if (~zero & 1) == 1:
            res = min(res, even)      # Consider even case
        
        # If result never updated, return -1
        # Otherwise return minimum operations found
        return -1 if res == float('inf') else res