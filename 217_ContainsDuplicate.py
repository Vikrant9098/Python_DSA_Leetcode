class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()                     # to store unique numbers

        for num in nums:                 # loop through each number
            if num in seen:              # if already seen, it's duplicate
                return True              # return True immediately
            seen.add(num)                # otherwise add number to set

        return False                     # if no duplicates found
