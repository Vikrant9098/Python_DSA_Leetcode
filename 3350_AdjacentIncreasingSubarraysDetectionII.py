class Solution(object):
    def maxIncreasingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)  # get length of list
        up = 1  # current increasing length
        pre_max_up = 0  # previous increasing length
        res = 0  # result (max k)

        for i in range(1, n):  # loop from 2nd element
            if nums[i] > nums[i - 1]:  # if strictly increasing
                up += 1  # extend current increasing length
            else:  # if sequence breaks
                pre_max_up = up  # store previous increasing length
                up = 1  # reset current length

            # find possible k using both sequences
            res = max(res, max(up // 2, min(pre_max_up, up)))

        return res  # return the max k found
