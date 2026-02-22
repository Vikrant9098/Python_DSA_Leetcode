class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        x = 1   # Start with binary 1
        
        while x <= n:   # Keep generating alternating numbers until x exceeds n
            
            if x == n:   # If generated number equals n
                return True   # n has alternating bits
            
            elif x % 2 == 0:   # If x is even (ends with 0 in binary)
                x = 2 * x + 1   # Append 1 → make pattern alternate
            
            else:   # If x is odd (ends with 1 in binary)
                x = 2 * x   # Append 0 → make pattern alternate
        
        return False   # If we exit loop, n is not alternating
