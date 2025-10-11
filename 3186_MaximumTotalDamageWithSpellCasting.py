class Solution(object):
    def maximumTotalDamage(self, power):
        """
        :type power: List[int]
        :rtype: int
        """
        # Import Counter to count occurrences easily
        from collections import Counter
        # Count how many times each damage value appears
        freq = Counter(power)

        # Get all unique damage values
        unique = sorted(freq.keys())
        # Store the total number of unique damages
        n = len(unique)

        # Create a DP list to store max total damage up to each index
        dp = [0] * n
        # Initialize DP with the first damage’s total damage
        dp[0] = unique[0] * freq[unique[0]]

        # Loop through each unique damage value starting from index 1
        for i in range(1, n):
            # Current damage value
            curr_val = unique[i]
            # Total damage for all spells with this value
            curr_total = curr_val * freq[curr_val]
            # Start by not taking this damage (same as previous best)
            dp[i] = dp[i - 1]

            # Check previous damages to find a non-conflicting one (difference > 2)
            j = i - 1
            while j >= 0 and abs(unique[j] - curr_val) <= 2:
                # Move left until we find a damage that is far enough
                j -= 1

            # If a valid non-conflicting damage exists
            if j >= 0:
                # Take the better of skipping or including current damage
                dp[i] = max(dp[i], dp[j] + curr_total)
            else:
                # If no valid previous found, compare with current total only
                dp[i] = max(dp[i], curr_total)

        # Return the maximum total damage possible
        return dp[-1]
