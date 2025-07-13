class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        # Initialize result array to store final products
        result = [1] * n
        
        # First pass: calculate left products (product of all elements to the left)
        # result[i] will contain product of all elements before index i
        for i in range(1, n):
            result[i] = result[i-1] * nums[i-1]
        
        # Second pass: calculate right products and multiply with left products
        # Use a variable to track running product from right side
        right_product = 1
        for i in range(n-1, -1, -1):
            # Multiply current left product with right product
            result[i] *= right_product
            # Update right product for next iteration
            right_product *= nums[i]
        
        return result