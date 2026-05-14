class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # Sort the array so numbers come in order
        nums.sort()

        # Expected maximum number
        n = len(nums) - 1

        # Check if numbers from 1 to n-1 are present correctly
        for i in range(n):
            if nums[i] != i + 1:
                return False

        # Last element should be equal to n
        return nums[n] == n