class Solution:
    def minimumTotalDistance(self, robot, factory):
        # Sort robots and factories by position
        robot.sort()
        factory.sort()

        n = len(robot)      # number of robots
        m = len(factory)    # number of factories

        INF = 10**18        # large value to represent impossible cases

        # dp[i][j] = minimum distance to fix first i robots using first j factories
        dp = [[INF] * (m + 1) for _ in range(n + 1)]

        # Base case: 0 robots → 0 distance regardless of factories
        for j in range(m + 1):
            dp[0][j] = 0

        # Iterate over factories
        for j in range(1, m + 1):
            pos, limit = factory[j - 1]  # current factory position & capacity

            # Iterate over number of robots
            for i in range(n + 1):

                # Option 1: skip this factory
                dp[i][j] = dp[i][j - 1]

                # Try assigning k robots to this factory (1 to limit)
                dist = 0  # cumulative distance for k robots

                for k in range(1, limit + 1):
                    if i - k < 0:
                        break  # not enough robots to assign

                    # Add distance of assigning (i-k)th robot to current factory
                    dist += abs(robot[i - k] - pos)

                    # Option 2: assign k robots to this factory
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i - k][j - 1] + dist  # previous + current assignment cost
                    )

        # Final answer: all robots using all factories
        return dp[n][m]