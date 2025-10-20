class Solution(object):  # Define the Solution class
    def search(self, nums, target):  # Define the search method
        """
        :type nums: List[int]  # Input type: list of integers
        :type target: int      # Input type: integer
        :rtype: bool           # Return type: boolean
        """
        left, right = 0, len(nums) - 1  # Initialize left and right pointers for binary search

        while left <= right:  # Continue searching while left pointer is less than or equal to right pointer
            mid = left + (right - left) // 2  # Calculate the middle index to avoid overflow

            if nums[mid] == target:  # If middle element is the target
                return True  # Target found, return True

            if nums[left] == nums[mid] == nums[right]:  # If left, mid, and right elements are equal
                left += 1   # Move left pointer one step right
                right -= 1  # Move right pointer one step left
            elif nums[left] <= nums[mid]:  # If left side is sorted
                if nums[left] <= target < nums[mid]:  # If target lies within left sorted side
                    right = mid - 1  # Move right pointer to mid-1 to search left side
                else:  # If target is not in left sorted side
                    left = mid + 1  # Move left pointer to mid+1 to search right side
            else:  # If right side is sorted
                if nums[mid] < target <= nums[right]:  # If target lies within right sorted side
                    left = mid + 1  # Move left pointer to mid+1 to search right side
                else:  # If target is not in right sorted side
                    right = mid - 1  # Move right pointer to mid-1 to search left side

        return False  # If while loop ends, target is not found, return False
