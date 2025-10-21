class Solution(object):
    def maxFrequency(self, nums, k, numOperations):
        # Sort the array to make range checking easier
        nums.sort()
        n = len(nums)  # Length of the array
        ans = 0        # Stores the maximum frequency found
        left = 0       # Left pointer for sliding window
        right = 0      # Right pointer for sliding window
        
        from collections import Counter
        count = Counter(nums)  # Count how many times each number appears

        # ---------- First pass: use an existing number as reference ----------
        for mid in range(n):
            # Move left pointer if range between nums[mid] and nums[left] > k
            while nums[mid] - nums[left] > k:
                left += 1

            # Move right pointer to include numbers within k of nums[mid]
            while right < n - 1 and nums[right + 1] - nums[mid] <= k:
                right += 1

            # Total numbers in the current window
            total = right - left + 1

            # Calculate possible frequency using available operations
            ans = max(ans, min(total - count[nums[mid]], numOperations) + count[nums[mid]])

        # ---------- Second pass: use a non-existent midpoint as reference ----------
        left = 0  # Reset left pointer
        for right in range(n):
            # Find midpoint value between nums[left] and nums[right]
            mid = (nums[left] + nums[right]) // 2

            # Move left pointer until midpoint is within k range from both ends
            while mid - nums[left] > k or nums[right] - mid > k:
                left += 1
                mid = (nums[left] + nums[right]) // 2  # Recalculate midpoint

            # Update max frequency considering non-existent midpoint
            ans = max(ans, min(right - left + 1, numOperations))
        
        # Return the final maximum frequency
        return ans
