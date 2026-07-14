class Solution:
    def subsequencePairCount(self, nums: list[int]) -> int:
        MOD = 1000000007

        # Find the maximum value in the array
        m = max(nums)

        # dp[g1][g2] = Number of ways where:
        # g1 = GCD of first subsequence
        # g2 = GCD of second subsequence
        dp = [[0] * (m + 1) for _ in range(m + 1)]

        # Initially both subsequences are empty, so their GCD is 0
        dp[0][0] = 1

        # Process each number one by one
        for num in nums:

            # Create a new DP table for the current iteration
            ndp = [[0] * (m + 1) for _ in range(m + 1)]

            # Try every possible GCD of the first subsequence
            for j in range(m + 1):

                # New GCD if current number is added to first subsequence
                divisor1 = math.gcd(j, num)

                # Try every possible GCD of the second subsequence
                for k in range(m + 1):

                    # Number of ways to reach current state
                    val = dp[j][k]

                    # Skip states that are never reached
                    if val == 0:
                        continue

                    # New GCD if current number is added to second subsequence
                    divisor2 = math.gcd(k, num)

                    # Option 1: Ignore the current number
                    ndp[j][k] = (ndp[j][k] + val) % MOD

                    # Option 2: Put current number into the first subsequence
                    ndp[divisor1][k] = (ndp[divisor1][k] + val) % MOD

                    # Option 3: Put current number into the second subsequence
                    ndp[j][divisor2] = (ndp[j][divisor2] + val) % MOD

            # Move to the next iteration
            dp = ndp

        # Count states where both subsequences have the same non-zero GCD
        ans = 0
        for j in range(1, m + 1):
            ans = (ans + dp[j][j]) % MOD

        return ans