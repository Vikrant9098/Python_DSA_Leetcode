class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)                  # Number of children
        candies = [1] * n                 # Step 1: Give each child at least 1 candy

        # Step 2: Left to right pass
        # Ensure children with higher rating than left neighbor get more candies
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1   # Give one more candy than left neighbor

        # Step 3: Right to left pass
        # Ensure children with higher rating than right neighbor get more candies
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)  # Max of current or 1 more than right neighbor

        # Step 4: Sum up all candies to get the minimum total
        total = sum(candies)              # Total minimum candies needed

        return total                       # Return the total
