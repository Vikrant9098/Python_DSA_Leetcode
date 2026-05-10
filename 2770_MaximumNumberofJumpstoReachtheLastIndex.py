class Solution(object):
    def maximumJumps(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        memo = {}

        def dfs(i):

            # Return already computed result
            if i in memo:
                return memo[i]

            # If we reach the last index, no more jumps are needed
            if i == len(nums) - 1:
                return 0

            # Initialize result with a very small value
            res = float('-inf')

            # Try jumping to every next index
            for j in range(i + 1, len(nums)):

                # Check if the jump condition is satisfied
                if abs(nums[i] - nums[j]) <= target:

                    # Take the maximum jumps possible
                    res = max(res, dfs(j) + 1)

            # Store result in memoization dictionary
            memo[i] = res
            return res

        ans = dfs(0)

        # If no valid path exists, return -1
        return -1 if ans < 0 else ans