class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # Handle cases where k > n

        # Helper function to reverse a portion of the array
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Step 1: Reverse the entire array
        reverse(0, n - 1)
        # Step 2: Reverse the first k elements
        reverse(0, k - 1)
        # Step 3: Reverse the remaining n-k elements
        reverse(k, n - 1)
