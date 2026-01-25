class Solution(object):                      # Define Solution class
    def minimumDifference(self, nums, k):    # Function to find minimum difference
        """
        :type nums: List[int]                # nums is a list of integers
        :type k: int                         # k is the group size
        :rtype: int                          # return type is integer
        """
        if len(nums) <= 1:                   # If array has 0 or 1 element
            return 0                         # Difference is 0

        nums.sort()                          # Sort the array
        res = nums[k - 1] - nums[0]          # Initial difference of first k elements

        for i in range(k, len(nums)):        # Loop from k to end
            res = min(                       # Update minimum difference
                res,                         # Previous minimum
                nums[i] - nums[i - k + 1]    # Current window difference
            )

        return res                           # Return final minimum difference
