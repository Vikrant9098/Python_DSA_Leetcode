class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        result = 0

        # loop through all numbers
        for num in nums:
            # XOR cancels out duplicates
            result ^= num

        # the remaining number is the one that appears only once
        return result
