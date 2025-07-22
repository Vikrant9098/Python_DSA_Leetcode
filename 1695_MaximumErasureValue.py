class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Initialize a set to store the unique elements in the current subarray
        seen = set()

        # Pointer to track the start of the current window
        start = 0

        # To store the sum of current window elements
        current_sum = 0

        # To keep track of the maximum sum of any valid subarray found
        max_sum = 0

        # Loop through each element using 'end' as the right boundary of the window
        for end in range(len(nums)):

            # If the current element is already in the window (duplicate)
            # move the start pointer forward until the duplicate is removed
            while nums[end] in seen:
                # Remove the element at 'start' from the set
                seen.remove(nums[start])
                # Subtract the value from current sum
                current_sum -= nums[start]
                # Move the start of the window forward
                start += 1

            # Now, the current element is unique within the window
            # Add it to the set
            seen.add(nums[end])

            # Add its value to the current sum
            current_sum += nums[end]

            # Update the max_sum if the current sum is greater
            max_sum = max(max_sum, current_sum)

        # Return the maximum sum found
        return max_sum
