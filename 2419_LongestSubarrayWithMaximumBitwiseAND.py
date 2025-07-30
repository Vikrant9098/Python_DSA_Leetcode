class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        max_val = 0  # Initialize variable to store the maximum value in the array

        # Step 1: Find the maximum value in the array
        for num in nums:
            max_val = max(max_val, num)  # Update max_val if current num is greater

        max_length = 0       # Stores the maximum length of subarray with AND = max_val
        current_length = 0   # Temporary counter to track the current streak of max_val

        # Step 2: Traverse the array to find longest contiguous subarray with value == max_val
        for num in nums:
            if num == max_val:
                current_length += 1  # If current number equals max_val, extend the streak
                max_length = max(max_length, current_length)  # Update max_length if needed
            else:
                current_length = 0  # Reset current_length if number is not max_val

        return max_length  # Return the longest length of subarray with AND = max_val

# Time complexity: O(n)
# Space complexity: O(1)