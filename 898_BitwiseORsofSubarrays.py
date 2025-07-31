class Solution(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # Set to store all unique OR results
        result = set()
        
        # Set to store OR results of subarrays ending at previous element
        prev = set()
        
        for num in arr:
            # Set to store OR results of subarrays ending at current element
            curr = set()
            
            # Add current number as a single-element subarray
            curr.add(num)
            
            # Extend previous subarrays by ORing with current number
            for val in prev:
                curr.add(val | num)
            
            # Add current results to the global result set
            result.update(curr)
            
            # Update prev for next iteration
            prev = curr
        
        return len(result)
