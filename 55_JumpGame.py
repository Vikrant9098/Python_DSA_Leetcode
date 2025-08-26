class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxReach = 0  # farthest index we can reach so far

        for i in range(len(nums)):
            if i > maxReach:
                return False  # stuck, can't move further
            maxReach = max(maxReach, i + nums[i])
            if maxReach >= len(nums) - 1:
                return True  # we can reach the last index

        return True
