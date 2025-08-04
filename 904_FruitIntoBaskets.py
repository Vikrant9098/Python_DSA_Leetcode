class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        from collections import defaultdict

        basket = defaultdict(int)  # Dictionary to count fruit types in the window
        left = 0  # Left pointer of the sliding window
        max_fruits = 0  # Max number of fruits we can collect

        # Right pointer iterates over each fruit
        for right in range(len(fruits)):
            basket[fruits[right]] += 1  # Add current fruit to the basket

            # If we have more than 2 types of fruits, shrink window from the left
            while len(basket) > 2:
                basket[fruits[left]] -= 1  # Remove one fruit from the left
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]  # Remove fruit type if count is 0
                left += 1  # Move the left pointer right

            # Update the maximum fruits collected so far
            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits
