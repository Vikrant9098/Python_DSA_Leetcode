class Solution(object):
    def zigZagArrays(self, n, l, r):
        """
        :type n: int
        :type l: int
        :type r: int
        :rtype: int
        """

        MOD = 1000000007

        # Total number of distinct values available in the range [l, r]
        m = r - l + 1

        # Base case:
        # For an array of length 1, every value in the range can be chosen.
        # dp[j] represents the number of valid ways ending with the j-th value.
        # Initially, every value contributes exactly 1 way.
        dp = [1] * m

        # Build DP for lengths 2 to n
        for i in range(2, n + 1):

            # Reverse the DP array.
            # This transformation allows the prefix-sum trick below
            # to efficiently compute transitions for zig-zag relationships.
            dp.reverse()

            # Running prefix sum of previous DP values
            s = 0

            for j in range(m):

                # Store the current prefix sum into dp[j].
                # This becomes the new DP value for position j.
                #
                # At the same time:
                # - Add the old dp[j] value into the running sum.
                # - Take modulo to avoid overflow.
                #
                # Tuple assignment ensures the old dp[j] is used
                # before it gets overwritten.
                dp[j], s = s, (s + dp[j]) % MOD

        # Sum all valid arrays ending with any value.
        total = sum(dp) % MOD

        # Multiply by 2 because the DP above counts only one zig-zag direction
        # (e.g., starting with increasing then decreasing).
        # The opposite direction contributes the same count.
        return (total << 1) % MOD