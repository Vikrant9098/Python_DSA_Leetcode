class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Sliding window approach
        left = 0      # Left boundary of the window
        zeros = 0     # Count of zeros in the current window
        max_length = 0  # Maximum length of subarray with at most k zeros flipped

        # Expand window by moving right pointer
        for right in range(len(nums)):
            # If we see a zero, increment zero counter
            if nums[right] == 0:
                zeros += 1
            
            # If zero count exceeds k, shrink window from the left
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1  # Move window forward

            # Calculate max window size so far
            max_length = max(max_length, right - left + 1)
        
        # Return the maximum length found
        return max_length

    # Alternative version: slightly more verbose with step-by-step comments
    def longestOnes_v2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        zero_count = 0
        max_len = 0

        for right in range(len(nums)):
            # Check if current element is zero and increase counter
            if nums[right] == 0:
                zero_count += 1

            # If more than k zeros, shrink from left until valid
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1  # Move the window forward

            # Update max length of the window
            max_len = max(max_len, right - left + 1)
        
        return max_len

# Logic:
# 1. Use a sliding window to include as many 1s and at most k zeros.
# 2. When the window has more than k zeros, shrink it from the left.
# 3. Keep track of the maximum length of such a valid window.

# Example dry run:
# nums = [1,1,1,]()
