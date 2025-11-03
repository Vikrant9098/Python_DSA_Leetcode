class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # add 1 at both ends to handle edge balloons easily
        nums = [1] + nums + [1]
        n = len(nums)

        # create dp table to store max coins for each range
        dp = [[0] * n for _ in range(n)]

        # l is the length of the current range
        for l in range(2, n):
            # i is the start of the range
            for i in range(0, n - l):
                j = i + l  # end of the range
                # try bursting each balloon k between i and j
                for k in range(i + 1, j):
                    # coins gained = left + burst k + right
                    coins = nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j]
                    dp[i][j] = max(dp[i][j], coins)  # store the best result

        # result is stored between first and last balloon
        return dp[0][n - 1]
