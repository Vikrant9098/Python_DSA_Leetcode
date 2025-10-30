class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        operations = target[0]  # Start with first element as initial operations
        
        # Loop through the array from second element
        for i in range(1, len(target)):
            # If current value is greater than previous value
            if target[i] > target[i - 1]:
                # Add the difference to operations
                operations += target[i] - target[i - 1]
        
        return operations  # Return total minimum operations
