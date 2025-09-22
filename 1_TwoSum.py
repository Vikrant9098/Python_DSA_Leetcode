class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store number -> index
        seen = {}
        
        # Loop through array
        for i, num in enumerate(nums):
            # Calculate the number we need to find
            complement = target - num
            
            # If complement already exists in dictionary, return indices
            if complement in seen:
                return [seen[complement], i]
            
            # Otherwise, store current number with its index
            seen[num] = i
