class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)  # Length of array
        left = 0       # Left pointer of sliding window
        total = 0      # Current window sum
        min_len = float("inf")  # Initialize minimum length as infinity

        # Expand the window by moving the right pointer
        for right in range(n):
            total += nums[right]  # Add current element to window sum

            # Shrink the window while total >= target
            while total >= target:
                min_len = min(min_len, right - left + 1)  # Update min length
                total -= nums[left]  # Remove leftmost element
                left += 1            # Move left pointer forward

        # If no valid subarray found, return 0; otherwise return min_len
        return 0 if min_len == float("inf") else min_len
