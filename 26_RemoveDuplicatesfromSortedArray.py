class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0  # if array is empty
        
        k = 1  # index to place next unique element (first element always kept)
        
        for i in range(1, len(nums)):
            # if current element is different from previous unique one
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]  # place unique element
                k += 1
        
        return k  # number of unique elements
