class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        # First two elements must be increasing
        if nums[0] >= nums[1]:
            return False

        count = 1  # Count direction changes

        # Start checking from the third element
        for i in range(2, n):
            # Equal adjacent values are not allowed
            if nums[i - 1] == nums[i]:
                return False

            # Check if the direction changes
            if (nums[i - 2] - nums[i - 1]) * (nums[i - 1] - nums[i]) < 0:
                count += 1

        # Trionic array must have exactly 3 segments
        return count == 3
