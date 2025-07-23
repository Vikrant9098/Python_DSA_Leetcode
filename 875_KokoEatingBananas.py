class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        # Define the search space: minimum speed is 1, maximum is the largest pile
        low = 1
        high = max(piles)

        # Binary search to find the minimum speed that allows Koko to finish in h hours
        while low < high:
            # Calculate mid speed
            mid = low + (high - low) // 2

            # Calculate total hours required at this speed
            hours = self.totalHours(piles, mid)

            # If she can finish within h hours, try a smaller speed
            if hours <= h:
                high = mid
            else:
                # Otherwise, increase the speed
                low = mid + 1

        # When low == high, we found the minimum valid eating speed
        return low

    def totalHours(self, piles, speed):
        """
        Helper function to calculate total hours needed to eat all bananas
        at a given speed.
        :type piles: List[int]
        :type speed: int
        :rtype: int
        """
        total = 0

        # For each pile, calculate hours needed and add to total
        for pile in piles:
            # Use ceiling division: (pile + speed - 1) // speed
            total += (pile + speed - 1) // speed

        return total
