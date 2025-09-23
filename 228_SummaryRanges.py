class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # List to store the result ranges
        result = []

        # If the array is empty, return empty result
        if not nums:
            return result

        # Mark the start of the current range
        start = nums[0]

        # Loop through all numbers + one extra step to handle the last range
        for i in range(1, len(nums) + 1):
            # Case 1: reached the end of array
            # Case 2: current number is not consecutive to previous one
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                # If start and end are the same, add single value
                if start == nums[i - 1]:
                    result.append(str(start))
                else:
                    # Otherwise, add range "start->end"
                    result.append(str(start) + "->" + str(nums[i - 1]))
                # Update start for the next range (if not at the end)
                if i < len(nums):
                    start = nums[i]

        # Return the final list of ranges
        return result
