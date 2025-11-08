class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:  
            return []  # if list is empty, return empty list

        nums.sort()  # sort numbers in ascending order
        n = len(nums)  # get total count of numbers

        dp = [1] * n  # dp[i] stores size of largest subset ending at nums[i]
        prev = [-1] * n  # prev[i] stores previous index in the subset chain

        max_index = 0  # index of last element in the largest subset

        # check each number with previous ones
        for i in range(1, n):
            for j in range(i):
                # if nums[i] is divisible by nums[j]
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1  # increase subset length
                    prev[i] = j  # store previous element index
            # update the index of the largest subset found so far
            if dp[i] > dp[max_index]:
                max_index = i

        result = []  # to store final subset
        k = max_index  # start from last index of subset
        while k >= 0:
            result.append(nums[k])  # add current number to result
            k = prev[k]  # move to previous element in subset

        return result[::-1]  # reverse result to get correct order
