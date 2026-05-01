class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Step 1: Initialize variables
        n = len(nums)              # Length of the array
        numSum = sum(nums)         # Total sum of all elements
        f = 0                      # Initial rotation function value

        # Step 2: Calculate F(0)
        # F(0) = 0*nums[0] + 1*nums[1] + ... + (n-1)*nums[n-1]
        for i, num in enumerate(nums):
            f += i * num

        # Store the maximum result
        res = f

        # Step 3: Use the relation:
        # F(k) = F(k-1) + sum(nums) - n * nums[n-k]
        # Iterate from last index to 1
        for i in range(n - 1, 0, -1):
            f = f + numSum - n * nums[i]   # Update rotation value
            res = max(res, f)              # Update maximum

        # Step 4: Return the maximum rotation function value
        return res