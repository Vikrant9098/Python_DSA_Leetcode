class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0  # index to place next valid element
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # overwrite element
                k += 1
        return k  # number of valid elements
