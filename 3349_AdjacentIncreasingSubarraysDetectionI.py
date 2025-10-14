class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)  # get total number of elements

        # loop till we have space for two subarrays of size k
        for i in range(n - 2 * k + 1):
            # check if both subarrays are strictly increasing
            if self.isIncreasing(nums, i, i + k) and self.isIncreasing(nums, i + k, i + 2 * k):
                return True  # found two increasing adjacent subarrays
        return False  # no such pair found

    # helper function to check if subarray from l to r-1 is strictly increasing
    def isIncreasing(self, nums, l, r):
        for i in range(l, r - 1):
            if nums[i] >= nums[i + 1]:  # not strictly increasing
                return False
        return True  # all pairs are increasing
