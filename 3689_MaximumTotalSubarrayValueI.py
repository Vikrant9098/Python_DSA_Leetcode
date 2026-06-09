class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # Find the minimum element in the array
        minimum_value = min(nums)

        # Find the maximum element in the array
        maximum_value = max(nums)

        # Difference between maximum and minimum value
        difference = maximum_value - minimum_value

        # Multiply the difference by k and return the result
        return difference * k