class Solution(object):
    def distance(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        
        n = len(nums)
        
        # Step 1: Group indices by value
        groups = defaultdict(list)
        for i, v in enumerate(nums):
            groups[v].append(i)
        
        # Result array
        res = [0] * n
        
        # Step 2: Process each group separately
        for group in groups.values():
            
            # Total sum of indices in this group
            total = sum(group)
            
            prefix_total = 0  # running sum of previous indices
            sz = len(group)   # size of group
            
            # Step 3: Compute distance for each index
            for i, idx in enumerate(group):
                
                # Formula to calculate sum of distances efficiently
                res[idx] = total - prefix_total * 2 + idx * (2 * i - sz)
                
                # Update prefix sum
                prefix_total += idx
        
        return res