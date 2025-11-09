class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # create dp array to store number of ways for each sum
        dp = [0] * (target + 1)
        
        # base case: only 1 way to make sum 0 (choose nothing)
        dp[0] = 1

        # loop through all sums from 1 to target
        for i in range(1, target + 1):
            # for each number in nums
            for num in nums:
                # if number can be used to form current sum i
                if i - num >= 0:
                    # add ways to make (i - num) to dp[i]
                    dp[i] += dp[i - num]

        # dp[target] holds total number of combinations
        return dp[target]
