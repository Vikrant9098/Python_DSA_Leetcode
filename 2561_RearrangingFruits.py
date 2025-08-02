class Solution(object):
    def minCost(self, basket1, basket2):
        """
        :type basket1: List[int]
        :type basket2: List[int]
        :rtype: int
        """
        from collections import Counter

        # Count frequency of each fruit in both baskets
        count = Counter()
        for fruit in basket1:
            count[fruit] += 1
        for fruit in basket2:
            count[fruit] -= 1

        to_swap = []

        # Prepare the list of fruits that need to be swapped
        for fruit, diff in count.items():
            # If any fruit has an odd frequency difference, return -1 (not swappable evenly)
            if diff % 2 != 0:
                return -1
            # Add abs(diff) // 2 occurrences of this fruit to the to_swap list
            for _ in range(abs(diff) // 2):
                to_swap.append(fruit)

        # If nothing to swap, both baskets are already equal
        if not to_swap:
            return 0

        # Sort the list of fruits to be swapped for greedy approach
        to_swap.sort()

        # Find the minimum fruit cost in both baskets (used for potential double-swap)
        min_fruit = min(min(basket1), min(basket2))

        total_cost = 0

        # Only need to perform n // 2 swaps (rest are the pairings)
        for i in range(len(to_swap) // 2):
            # The cost is the minimum between:
            # - Direct swap (to_swap[i])
            # - Double-swap through the cheapest fruit (2 * min_fruit)
            total_cost += min(to_swap[i], 2 * min_fruit)

        # Return the total minimum cost
        return total_cost
