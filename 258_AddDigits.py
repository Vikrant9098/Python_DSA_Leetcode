class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # If the number is 0, return 0
        if num == 0:
            return 0
        
        # Use the digital root formula for O(1) solution
        return 1 + (num - 1) % 9
