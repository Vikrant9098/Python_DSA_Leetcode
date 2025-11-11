class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # Create DP array where dp[i][j] = max strings using i zeros and j ones
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Loop through each binary string
        for s in strs:
            # Count zeros and ones in the string
            zeros = s.count('0')
            ones = s.count('1')
            
            # Update dp from bottom-right to avoid using same string twice
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    # Take max of including or excluding this string
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        
        # Return max subset size possible with m zeros and n ones
        return dp[m][n]
