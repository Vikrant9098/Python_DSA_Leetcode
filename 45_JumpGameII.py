class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0          # number of jumps made
        currentEnd = 0     # end of the current jump range
        farthest = 0       # farthest index we can reach

        for i in range(len(nums) - 1):  # no need to jump from last index
            farthest = max(farthest, i + nums[i])

            # If we reach the end of the current range, we must jump
            if i == currentEnd:
                jumps += 1
                currentEnd = farthest

        return jumps
