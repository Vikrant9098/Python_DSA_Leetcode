class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers are not palindromes
        # Numbers ending with 0 (except 0 itself) can't be palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0  # to store the reversed half of the number
        
        # Reverse only half of the digits
        while x > reversed_half:
            digit = x % 10                      # get the last digit
            reversed_half = reversed_half * 10 + digit  # add digit to reversed half
            x //= 10                            # remove the last digit from x
        
        # For even digits: x == reversed_half
        # For odd digits: ignore middle digit by dividing reversed_half by 10
        return x == reversed_half or x == reversed_half // 10
