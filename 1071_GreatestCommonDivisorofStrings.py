class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # Quick check: if str1 + str2 != str2 + str1, no common divisor exists
        if str1 + str2 != str2 + str1:
            return ""
        
        # Helper function to calculate GCD of two numbers
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        # The length of the GCD string must be GCD of the lengths
        gcd_length = gcd(len(str1), len(str2))
        
        # Return the substring of that length
        return str1[:gcd_length]