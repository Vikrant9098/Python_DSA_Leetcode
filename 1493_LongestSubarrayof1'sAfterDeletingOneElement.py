class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sliding window approach
        left = 0        # Left boundary of the window
        zeros = 0       # Count of zeros in the current window
        max_len = 0     # Maximum length of subarray after deleting one element

        # Expand window using right pointer
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1  # Count the zeros in the window

            # If more than one zero, move the left pointer to shrink the window
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1  # Shrink the window from the left

            # Update max length (we delete one element, so the length is (right - left))
            max_len = max(max_len, right - left)
        
        return max_len

    # Alternative version with more detailed explanation
    def longestSubarray_v2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        zero_count = 0
        result = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            # Allow only one zero to be removed
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # Subarray length is right - left (since we must delete 1 element)
            result = max(result, right - left)
        
        return result

# Logic:
# 1. Maintain a window that can contain at most one zero.
# 2. Delete one element (a zero) by allowing at most one in the window.
# 3. When zero count exceeds one, move left to shrink the window.
# 4. Track the maximum length of such valid windows.

# Example:
# nums = [1,1,0,1]
# Window = [1,1,0] → delete '0' → [1,1] → next element '1' → [1,1,1]
# Length = 3
