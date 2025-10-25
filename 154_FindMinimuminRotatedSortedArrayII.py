class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize left and right pointers
        left, right = 0, len(nums) - 1
        
        # Binary search loop
        while left < right:
            # Find middle index
            mid = left + (right - left) // 2
            
            # If middle is greater than right, min is in right half
            if nums[mid] > nums[right]:
                left = mid + 1
            # If middle is less than right, min is in left half including mid
            elif nums[mid] < nums[right]:
                right = mid
            # If middle equals right, reduce right by one to handle duplicates
            else:
                right -= 1
        
        # Left points to the minimum element
        return nums[left]
