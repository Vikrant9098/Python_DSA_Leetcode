class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)                      # get total number of houses
        if n == 1:                         # if only one house
            return nums[0]                 # rob that house
        if n == 2:                         # if two houses
            return max(nums[0], nums[1])   # rob the one with more money

        # case 1: rob from house 0 to n-2 (skip last)
        case1 = self.robLinear(nums, 0, n - 2)
        # case 2: rob from house 1 to n-1 (skip first)
        case2 = self.robLinear(nums, 1, n - 1)

        return max(case1, case2)           # take the better result

    def robLinear(self, nums, start, end):
        prev2 = 0      # stores dp[i-2] → max money till two houses before
        prev1 = 0      # stores dp[i-1] → max money till previous house

        # loop through given range of houses
        for i in range(start, end + 1):
            pick = nums[i] + prev2          # if we rob current house
            skip = prev1                    # if we skip current house
            curr = max(pick, skip)          # choose the better option
            prev2 = prev1                   # move prev2 forward
            prev1 = curr                    # update prev1 to current best

        return prev1                        # return final max money
