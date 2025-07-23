class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """

        # Sort the potions array in ascending order for binary search
        potions.sort()

        # Store the number of potions
        m = len(potions)

        # Initialize the result list to store the count of successful pairs for each spell
        result = []

        # Iterate over each spell in the spells list
        for spell in spells:

            # Initialize binary search boundaries
            low, high = 0, m - 1

            # Initialize idx to m (assume no potion found initially)
            idx = m

            # Perform binary search to find the first potion that forms a successful pair
            while low <= high:

                # Calculate the middle index
                mid = low + (high - low) // 2

                # Check if the current potion forms a successful pair with the spell
                if spell * potions[mid] >= success:
                    # Update idx to current mid because we found a valid pair
                    idx = mid

                    # Try to find an earlier valid potion, so move left
                    high = mid - 1
                else:
                    # Current pair is not successful, search in the right half
                    low = mid + 1

            # Number of successful potions is from idx to end => m - idx
            count = m - idx

            # Append the count to the result list
            result.append(count)

        # Return the list containing number of successful potions for each spell
        return result
