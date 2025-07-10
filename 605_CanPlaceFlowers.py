class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # Track how many flowers we can plant
        count = 0
        
        # Iterate through each position in the flowerbed
        for i in range(len(flowerbed)):
            # Check if current position is empty (0)
            if flowerbed[i] == 0:
                # Check if left neighbor is empty or doesn't exist (i.e., we're at start)
                left_empty = (i == 0) or (flowerbed[i-1] == 0)
                
                # Check if right neighbor is empty or doesn't exist (i.e., we're at end)
                right_empty = (i == len(flowerbed) - 1) or (flowerbed[i+1] == 0)
                
                # If both neighbors are empty/don't exist, we can plant here
                if left_empty and right_empty:
                    # Plant flower by marking position as 1
                    flowerbed[i] = 1
                    # Increment count of planted flowers
                    count += 1
                    
                    # Early termination: if we've planted enough flowers, return True
                    if count >= n:
                        return True
        
        # Return True if we managed to plant at least n flowers
        return count >= n