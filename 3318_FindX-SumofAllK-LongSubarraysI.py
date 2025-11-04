class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n = len(nums)  # Get length of nums array
        ans = []  # List to store the x-sum for each subarray
        
        # Loop over all possible subarrays of length k
        for i in range(n - k + 1):
            sub = nums[i:i + k]  # Get the current subarray
            
            freq = {}  # Dictionary to store frequency of each element
            for num in sub:
                freq[num] = freq.get(num, 0) + 1  # Count occurrences
            
            # Sort by frequency (descending), then by value (descending)
            sorted_items = sorted(freq.items(), key=lambda a: (-a[1], -a[0]))
            
            # Keep only top x elements
            keep = set([num for num, count in sorted_items[:x]])
            
            # Calculate sum of only kept elements
            total = sum(num for num in sub if num in keep)
            
            ans.append(total)  # Store result for this subarray
        
        return ans  # Return final list of x-sums
