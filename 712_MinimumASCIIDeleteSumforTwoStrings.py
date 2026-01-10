class Solution(object):                       # Define the Solution class
    def minimumDeleteSum(self, s1, s2):       # Function to calculate minimum delete ASCII sum
        """
        :type s1: str                         # First input string
        :type s2: str                         # Second input string
        :rtype: int                           # Return type is integer
        """
        m, n = len(s1), len(s2)               # Get lengths of both strings
        dp = [0] * (n + 1)                    # Create DP array for second string

        for j in range(1, n + 1):             # Loop through second string
            dp[j] = dp[j - 1] + ord(s2[j - 1])# Add ASCII value of s2 character
        
        for i in range(1, m + 1):             # Loop through first string
            prev = dp[0]                      # Store previous diagonal value
            dp[0] += ord(s1[i - 1])           # Add ASCII value of s1 character

            for j in range(1, n + 1):         # Loop through second string
                temp = dp[j]                  # Save current dp value

                if s1[i - 1] == s2[j - 1]:    # If characters are equal
                    dp[j] = prev              # No deletion needed
                else:                         # If characters are different
                    dp[j] = min(              # Choose minimum delete cost
                        dp[j] + ord(s1[i - 1]),   # Delete character from s1
                        dp[j - 1] + ord(s2[j - 1])# Delete character from s2
                    )
                
                prev = temp                   # Update prev for next iteration
        
        return dp[n]                          # Return final minimum delete sum
