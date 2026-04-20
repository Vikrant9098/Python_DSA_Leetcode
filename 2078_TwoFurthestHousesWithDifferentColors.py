class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        
        n = len(colors)  # Length of the array
        
        left, right = 0, n - 1  # Initialize pointers
        
        # Find the first index from the left
        # where value is different from the last element
        for i in range(n):
            if colors[i] ^ colors[-1]:  # XOR checks if values are different
                left = i
                break  # Stop at first occurrence
        
        # Find the first index from the right
        # where value is different from the first element
        for i in range(n - 1, -1, -1):
            if colors[i] ^ colors[0]:  # XOR checks if values are different
                right = i
                break  # Stop at first occurrence
        
        # Return the maximum possible distance
        return max(n - 1 - left, right)