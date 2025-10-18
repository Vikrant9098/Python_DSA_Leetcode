class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        low = 0               # Pointer for next position of 0
        mid = 0               # Pointer for current element
        high = len(nums) - 1  # Pointer for next position of 2

        # Loop until mid crosses high
        while mid <= high:
            if nums[mid] == 0:            # If current element is 0
                nums[low], nums[mid] = nums[mid], nums[low]  # Swap 0 to the front
                low += 1                  # Move low pointer forward
                mid += 1                  # Move mid pointer forward
            elif nums[mid] == 1:          # If current element is 1
                mid += 1                  # Keep it in place, just move mid
            else:                         # If current element is 2
                nums[mid], nums[high] = nums[high], nums[mid]  # Swap 2 to the back
                high -= 1                 # Move high pointer backward
