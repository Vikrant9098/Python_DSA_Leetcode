class Solution(object):  # Define solution class

    def cal(self, a, b):  # Function to calculate movement cost between two letters
        return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)  # Manhattan distance on 6-column grid

    def minimumDistance(self, word):  # Main function
        n = len(word)  # Length of the word
        
        # 3D DP: dp[i][j][k] = min cost after i chars, left at j, right at k
        dp = [[[0] * 26 for _ in range(26)] for _ in range(n + 1)]

        for i in range(n):  # Iterate over each character
            t = ord(word[i]) - ord('A')  # Convert current char to index (0–25)

            for j in range(26):  # Loop over all left finger positions
                for k in range(26):  # Loop over all right finger positions
                    dp[i + 1][j][k] = 1000000  # Initialize next state with large value

            for j in range(26):  # Previous left finger positions
                for k in range(26):  # Previous right finger positions

                    # Move right finger to current character
                    dp[i + 1][j][t] = min(  # Update state keeping left same, right at t
                        dp[i + 1][j][t],  # Current stored cost
                        dp[i][j][k] + self.cal(k, t)  # Add cost from right finger move
                    )

                    # Move left finger to current character
                    dp[i + 1][t][k] = min(  # Update state keeping right same, left at t
                        dp[i + 1][t][k],  # Current stored cost
                        dp[i][j][k] + self.cal(j, t)  # Add cost from left finger move
                    )

        ans = 100000  # Initialize answer with large value

        for j in range(26):  # Final left finger positions
            for k in range(26):  # Final right finger positions
                ans = min(ans, dp[n][j][k])  # Take minimum cost

        return ans  # Return minimum total distance