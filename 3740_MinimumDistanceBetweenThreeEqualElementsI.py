class Solution:
    def minimumDistance(self, nums):
        from collections import defaultdict  # To store indices of each number
        
        mp = defaultdict(list)  # Dictionary: value -> list of indices
        
        # Store indices of each number in the array
        for i, val in enumerate(nums):
            mp[val].append(i)

        ans = float('inf')  # Initialize answer with infinity
        
        # Iterate over all values' index lists
        for v in mp.values():
            
            # We need at least 3 occurrences to form a triplet
            if len(v) >= 3:
                
                # Check all consecutive triplets of indices
                for i in range(len(v) - 2):
                    
                    # Distance = 2 * (last index - first index)
                    d = 2 * (v[i + 2] - v[i])
                    
                    # Update minimum distance
                    ans = min(ans, d)

        # If no valid triplet found, return -1
        return -1 if ans == float('inf') else ans