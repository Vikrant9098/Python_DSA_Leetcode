class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """

        # Initialize both minimum and maximum cost with the largest cost value
        xMin = xMax = max(costs)

        # Frequency array where freq[i] stores
        # how many ice creams have cost = i
        freq = [0] * (xMax + 1)

        # Count frequency of each cost and find the minimum cost
        for x in costs:
            freq[x] += 1
            xMin = min(xMin, x)

        # Stores the total number of ice creams purchased
        cnt = 0

        # Traverse costs from the minimum cost to the maximum cost
        # using the frequency array (counting sort approach)
        for x, f in enumerate(freq[xMin:], start=xMin):

            # Skip costs that do not exist
            if f == 0:
                continue

            # Maximum ice creams of cost x that can be bought
            # Limited by:
            # 1. Available coins
            # 2. Available ice creams with this cost
            buy = min(coins // x, f)

            # If we cannot buy even one ice cream at this cost,
            # we cannot afford any higher cost either
            if buy == 0:
                break

            # Add purchased ice creams to the answer
            cnt += buy

            # Deduct the spent coins
            coins -= buy * x

        # Return the maximum number of ice creams purchased
        return cnt