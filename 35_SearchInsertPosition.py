class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0                     # start of array
        right = len(nums) - 1        # end of array
        
        # binary search loop
        while left <= right:
            mid = left + (right - left) // 2  # middle index
            
            if nums[mid] == target:           # target found
                return mid
            elif nums[mid] < target:          # target in right half
                left = mid + 1
            else:                             # target in left half
                right = mid - 1
        
        # target not found, left is the insert position
        return left
