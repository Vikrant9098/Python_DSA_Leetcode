class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Left pointer
        left = 0
        # Right pointer
        right = len(nums) - 1

        # Binary search loop
        while left <= right:
            # Find middle index
            mid = (left + right) // 2

            # If middle element is the target
            if nums[mid] == target:
                return mid

            # Check if left half is sorted
            if nums[left] <= nums[mid]:
                # Check if target lies in the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Move to left half
                else:
                    left = mid + 1   # Move to right half
            # Otherwise, right half is sorted
            else:
                # Check if target lies in the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Move to right half
                else:
                    right = mid - 1  # Move to left half

        # Target not found
        return -1
