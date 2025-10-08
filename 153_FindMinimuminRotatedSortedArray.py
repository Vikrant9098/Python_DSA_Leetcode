class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Left pointer
        left = 0
        # Right pointer
        right = len(nums) - 1

        # Binary search to find the minimum element
        while left < right:
            # Find middle index
            mid = (left + right) // 2

            # If middle element is greater than right element,
            # minimum is in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            # Otherwise, minimum is in the left half (including mid)
            else:
                right = mid

        # Left now points to the smallest element
        return nums[left]
