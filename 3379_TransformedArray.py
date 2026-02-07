class Solution(object):                  # Define the Solution class
    def constructTransformedArray(self, nums):   # Function that transforms the array
        """
        :type nums: List[int]             # nums is a list of integers
        :rtype: List[int]                 # function returns a list of integers
        """
        # Create a new list using list comprehension
        return [
            nums[(i + v) % len(nums)]     # Pick element at shifted index (with wrap-around)
            for i, v in enumerate(nums)   # Loop through index i and value v in nums
        ]
