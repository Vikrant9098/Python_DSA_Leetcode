class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        # count of patches added
        patches = 0
        # index to go through nums
        i = 0
        # smallest number we cannot form yet
        miss = 1

        # loop until we can cover all numbers up to n
        while miss <= n:
            # if the current number can help extend the range
            if i < len(nums) and nums[i] <= miss:
                # add nums[i] to range we can cover
                miss += nums[i]
                # move to next number
                i += 1
            else:
                # patch by adding miss itself
                miss += miss
                # increase patch count
                patches += 1

        # return total patches added
        return patches
