class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]      # Amount of each fruit type
        :type baskets: List[int]     # Capacity of each basket
        :rtype: int                  # Number of unplaced fruit types
        """
        
        n = len(fruits)  # Total number of fruits (and baskets, since both are same length)
        
        used = [False] * n  # Track whether a basket has already been used
        
        unplaced = 0  # Count how many fruits couldn't be placed
        
        for i in range(n):  # Loop through each fruit type
            placed = False  # Assume the fruit is not placed yet
            
            for j in range(n):  # Try to find a suitable basket
                if not used[j] and baskets[j] >= fruits[i]:
                    # If basket is unused and has enough capacity
                    used[j] = True  # Mark this basket as used
                    placed = True   # Mark fruit as placed
                    break           # No need to check more baskets for this fruit
            
            if not placed:
                # If no basket could hold this fruit
                unplaced += 1  # Increment count of unplaced fruits
        
        return unplaced  # Return total number of unplaced fruit types
