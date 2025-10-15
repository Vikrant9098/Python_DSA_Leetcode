class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0  # total number of subarrays with sum = k
        cum_sum = 0  # cumulative sum
        prefix_sums = {0: 1}  # store frequency of prefix sums, base case: sum 0 occurs once

        for num in nums:
            cum_sum += num  # update cumulative sum
            if (cum_sum - k) in prefix_sums:
                count += prefix_sums[cum_sum - k]  # add number of times (cum_sum - k) occurred
            prefix_sums[cum_sum] = prefix_sums.get(cum_sum, 0) + 1  # update frequency of current sum

        return count  # return total count
