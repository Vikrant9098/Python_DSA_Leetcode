class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Step 1: Remove consecutive duplicates
        cleaned = [nums[0]]  # Always include the first element

        for i in range(1, len(nums)):
            # Only add current number if it's different from the previous one
            if nums[i] != nums[i - 1]:
                cleaned.append(nums[i])

        count = 0  # To store number of hills and valleys

        # Step 2: Traverse the cleaned list from second to second-last element
        for i in range(1, len(cleaned) - 1):
            prev = cleaned[i - 1]  # Left neighbor
            curr = cleaned[i]      # Current element
            next = cleaned[i + 1]  # Right neighbor

            # Check for hill: current element is greater than both neighbors
            if curr > prev and curr > next:
                count += 1
            # Check for valley: current element is smaller than both neighbors
            elif curr < prev and curr < next:
                count += 1

        return count  # Return total hills and valleys
