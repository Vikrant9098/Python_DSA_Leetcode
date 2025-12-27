class Solution(object):
    # Solution class

    def minDeletionSize(self, strs):
        # Function to find minimum number of columns to delete

        n = len(strs[0])
        # Number of columns in each string

        m = len(strs)
        # Number of strings (rows)

        dp = [1] * n
        # dp[i] = length of longest valid column sequence ending at column i

        for i in range(1, n):
            # Iterate through columns starting from second column

            for j in range(i):
                # Compare current column i with previous column j

                ok = True
                # Flag to check if column j can come before column i

                for r in range(m):
                    # Check all strings

                    if strs[r][j] > strs[r][i]:
                        # If lexicographical order breaks
                        ok = False
                        # Mark as invalid
                        break
                        # Stop checking further rows

                if ok:
                    # If column j can come before column i
                    dp[i] = max(dp[i], dp[j] + 1)
                    # Update longest valid sequence

        mx = 0
        # Variable to store maximum value in dp

        for v in dp:
            # Loop through dp array
            mx = max(mx, v)
            # Find the maximum valid column sequence

        return n - mx
        # Minimum deletions = total columns - longest valid sequence
