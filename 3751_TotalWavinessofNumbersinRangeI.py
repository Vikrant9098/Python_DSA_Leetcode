class Solution(object):
    # Maximum limit for precomputation
    MAX = 100001

    # dp[i] stores the waviness count for number i
    dp = [0] * MAX

    # pref[i] stores the prefix sum of waviness values up to i
    pref = [0] * MAX

    # Precompute waviness values and prefix sums
    for i in range(100, MAX):

        # Extract the rightmost digit
        right_digit = i % 10

        # Extract the middle digit
        middle_digit = (i // 10) % 10

        # Extract the left digit (hundreds place)
        left_digit = (i // 100) % 10

        # Check if the middle digit forms a wave
        # A wave exists if the middle digit is either
        # strictly greater than both neighbors or
        # strictly smaller than both neighbors
        is_wave = (
            middle_digit > max(left_digit, right_digit)
            or middle_digit < min(left_digit, right_digit)
        )

        # Add current wave contribution to the value of i // 10
        dp[i] = dp[i // 10] + int(is_wave)

        # Build prefix sum array for fast range queries
        pref[i] = pref[i - 1] + dp[i]

    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """

        # Return the sum of waviness values in the range [num1, num2]
        return self.pref[num2] - self.pref[num1 - 1]