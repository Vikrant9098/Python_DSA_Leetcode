
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Initialize left pointer - tracks the next position for non-zero elements
        left = 0
        
        # Traverse the array with right pointer
        for right in range(len(nums)):
            # If current element is non-zero, we need to move it to the front
            if nums[right] != 0:
                # Only swap if positions are different to minimize operations
                if left != right:
                    # Swap non-zero element to the left position
                    nums[left], nums[right] = nums[right], nums[left]
                
                # Move left pointer to next position for next non-zero element
                left += 1
        
        # At this point, all non-zero elements are at the front
        # and left pointer is at the first position that should contain zero
        # All positions from left to end are automatically zeros due to swapping
