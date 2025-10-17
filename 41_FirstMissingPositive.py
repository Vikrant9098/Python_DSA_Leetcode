class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)  # length of the array

        # place each number in its correct position (nums[i] -> nums[nums[i]-1])
        for i in range(n):
            while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]  # swap to correct position

        # find the first index where the number is incorrect
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1  # first missing positive

        # if all numbers are in place, the missing number is n+1
        return n + 1
