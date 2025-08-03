class Solution(object):
    def maxTotalFruits(self, fruits, startPos, k):
        """
        :type fruits: List[List[int]]
        :type startPos: int
        :type k: int
        :rtype: int
        """
        n = len(fruits)  # Total number of fruit positions
        max_fruits = 0   # To keep track of the maximum fruits collected
        left = 0         # Left pointer of sliding window
        total = 0        # Sum of fruits in the current window

        # Iterate over all fruit positions using the right pointer
        for right in range(n):
            total += fruits[right][1]  # Add fruits at the right end of the window

            # Check if the current window [left, right] is reachable within k steps
            while left <= right and not self.canReach(fruits, left, right, startPos, k):
                total -= fruits[left][1]  # Remove fruits at the left end
                left += 1                 # Move left pointer to shrink window

            # Update the maximum fruits harvested if current total is more
            max_fruits = max(max_fruits, total)

        return max_fruits  # Return the maximum fruits that can be collected

    def canReach(self, fruits, left, right, startPos, k):
        """
        Helper method to check if you can reach from startPos to both ends of the window
        within at most k steps (walking left first or right first)
        """
        left_pos = fruits[left][0]     # Get the x-position of the left end
        right_pos = fruits[right][0]   # Get the x-position of the right end

        # Option 1: Go to left end first, then walk to right
        steps1 = abs(startPos - left_pos) + (right_pos - left_pos)

        # Option 2: Go to right end first, then walk to left
        steps2 = abs(startPos - right_pos) + (right_pos - left_pos)

        # Return True if either path is reachable within k steps
        return min(steps1, steps2) <= k
