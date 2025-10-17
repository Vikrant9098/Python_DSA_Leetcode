class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)  # length of the array
        i = n - 2  # start from second last element

        # step 1: find first decreasing element from the end
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1  # move left until nums[i] < nums[i+1]

        if i >= 0:
            j = n - 1  # start from the last element
            # step 2: find element just larger than nums[i] from the end
            while nums[j] <= nums[i]:
                j -= 1  # move left to find the element larger than nums[i]
            nums[i], nums[j] = nums[j], nums[i]  # step 3: swap nums[i] and nums[j]

        # step 4: reverse the elements after index i
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]  # swap to reverse
            left += 1  # move left pointer
            right -= 1  # move right pointer
