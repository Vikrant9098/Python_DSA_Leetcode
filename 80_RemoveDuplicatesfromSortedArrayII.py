class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)  # if size ≤ 2, no need to remove
        
        k = 2  # index to place the next allowed element (first two are always valid)
        
        for i in range(2, len(nums)):
            # if current num is not equal to element two positions before,
            # it means it appeared <= 2 times
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]  # keep this element
                k += 1
        
        return k  # new length after removing extra duplicates
