class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = 0  # stores bits seen once
        twos = 0  # stores bits seen twice
        
        # loop through each number in the list
        for num in nums:
            ones = (ones ^ num) & ~twos  # update bits that appeared once
            twos = (twos ^ num) & ~ones  # update bits that appeared twice
        
        return ones  # bits that appeared only once form the unique number
