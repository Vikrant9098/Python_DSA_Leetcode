class Solution(object):                 # Defines the Solution class
    def numOfWays(self, n):             # Function to calculate number of ways for n rows
        MOD = 10**9 + 7                 # Large number to avoid overflow
        A = B = 6                       # A → 2-color patterns, B → 3-color patterns (for first row)

        for _ in range(2, n + 1):       # Loop from second row to nth row
               # Update A: ways with 2 colors
            A, B = (2*A + 2*B) % MOD, (2*A + 3*B) % MOD   # Update B: ways with 3 colors

        return (A + B) % MOD            # Return total number of ways
