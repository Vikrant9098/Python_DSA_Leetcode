class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        
        # We need to find the minimum number of deci-binary numbers
        # required to sum up to the given number.
        # The key observation is:
        # The answer is simply the largest digit in the string.
        
        # Convert each character (digit) in the string into an integer,
        # then find the maximum digit among them.
        return max(int(digit) for digit in n)