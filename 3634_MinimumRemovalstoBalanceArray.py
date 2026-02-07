class Solution(object):                 # Define the Solution class
    def minRemoval(self, nums, k):       # Function to find minimum removals
        """
        :type nums: List[int]            # nums is a list of integers
        :type k: int                     # k is an integer multiplier
        :rtype: int                      # return type is integer
        """
        nums.sort()                      # Sort the array
        i = 0                            # Left pointer of window
        max_len = 0                     # Stores largest valid window size
        
        for j in range(len(nums)):       # Right pointer moves through array
            while nums[j] > nums[i] * k: # If condition breaks
                i += 1                   # Move left pointer
            max_len = max(max_len, j - i + 1)  # Update max window size
            
        return len(nums) - max_len       # Remove elements outside window
