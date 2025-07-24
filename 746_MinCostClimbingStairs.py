class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        # Get the number of steps in the cost array
        n = len(cost)

        # Initialize the minimum cost to reach step 0 and step 1
        dp0 = cost[0]  # Cost to reach step 0
        dp1 = cost[1]  # Cost to reach step 1

        # Iterate from step 2 to the top of the staircase
        for i in range(2, n):
            # Calculate cost to reach current step:
            # It can be reached from (i - 1) or (i - 2)
            curr = cost[i] + min(dp0, dp1)

            # Move the window forward:
            # dp0 becomes dp1, and dp1 becomes curr (new result)
            dp0, dp1 = dp1, curr

        # To reach the top (beyond last index), you can come from last or second-last step
        return min(dp0, dp1)
