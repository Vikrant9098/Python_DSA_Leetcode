class Solution(object):                     # Define a class named Solution
    def minBitwiseArray(self, nums):         # Define function that takes a list nums
        ans = [-1]*len(nums)                 # Create result list filled with -1
        for i in range(len(nums)):           # Loop through each index of nums
            n = nums[i]                      # Store current number
            cnt = 0                          # Initialize bit count
            while n != 0:                    # Loop until n becomes 0
                cnt += 1                     # Increase bit count
                n = n >> 1                   # Right shift n by 1 bit
            n = 2**(cnt-1)-2                 # Set starting value based on bit count
            while n < nums[i]:               # Loop until n reaches nums[i]
                if n | n+1 == nums[i]:       # Check if n OR (n+1) equals nums[i]
                    ans[i] = n               # Store valid n in answer
                    break                   # Exit loop if found
                n += 1                       # Increment n
        return ans                           # Return the final result list
