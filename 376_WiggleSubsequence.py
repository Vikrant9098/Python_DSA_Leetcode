class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if list has 0 or 1 element, it's already a wiggle
        if len(nums) < 2:
            return len(nums)

        up = 1    # longest wiggle subsequence ending with an increase
        down = 1  # longest wiggle subsequence ending with a decrease

        # loop through array from second element
        for i in range(1, len(nums)):
            # if current number is greater than previous → up movement
            if nums[i] > nums[i - 1]:
                up = down + 1  # extend previous down sequence
            # if current number is smaller than previous → down movement
            elif nums[i] < nums[i - 1]:
                down = up + 1  # extend previous up sequence
            # if equal → no change in direction, so skip

        # return the longer of up or down sequences
        return max(up, down)
