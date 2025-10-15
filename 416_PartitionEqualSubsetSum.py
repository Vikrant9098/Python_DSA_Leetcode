class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)  # calculate total sum of array
        if total % 2 != 0:  # if sum is odd, cannot split equally
            return False

        target = total // 2  # sum each subset must reach
        dp = [False] * (target + 1)  # dp[i] = whether sum i is possible
        dp[0] = True  # sum 0 is always possible

        for num in nums:  # iterate through numbers
            for i in range(target, num - 1, -1):  # iterate backwards
                dp[i] = dp[i] or dp[i - num]  # include num or not

        return dp[target]  # return whether sum/2 is achievable
