class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Implement regular expression matching with support for '.' and '*'
        # '.' matches any single character
        # '*' matches zero or more of the preceding element
        # Get lengths of string and pattern for easier indexing
        s_len = len(s)
        p_len = len(p)
        
        # Create a 2D DP table where dp[i][j] represents if s[0:i] matches p[0:j]
        # dp[i][j] = True if first i characters of s match first j characters of p
        dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]
        
        # Base case: empty string matches empty pattern
        dp[0][0] = True
        
        # Handle patterns like "a*", "a*b*", "a*b*c*" that can match empty string
        # When pattern has '*', it can match zero occurrences of preceding character
        for j in range(2, p_len + 1):
            # If current character is '*' and we can match empty string up to j-2
            if p[j-1] == '*' and dp[0][j-2]:
                dp[0][j] = True
        
        # Fill the DP table using bottom-up approach
        for i in range(1, s_len + 1):
            for j in range(1, p_len + 1):
                # Current characters being compared
                s_char = s[i-1]  # Current character in string
                p_char = p[j-1]  # Current character in pattern
                
                # Case 1: Current pattern character is NOT '*'
                if p_char != '*':
                    # Check if current characters match (exact match or '.' wildcard)
                    if s_char == p_char or p_char == '.':
                        # Current characters match, so result depends on previous state
                        dp[i][j] = dp[i-1][j-1]
                    # If characters don't match, dp[i][j] remains False
                
                # Case 2: Current pattern character IS '*'
                else:
                    # '*' matches zero or more of the preceding element
                    # We need to look at the character before '*' in pattern
                    prev_p_char = p[j-2]  # Character before '*'
                    
                    # Option 1: Use '*' to match zero occurrences of preceding character
                    # This means we ignore the "char*" pattern and check if s[0:i] matches p[0:j-2]
                    dp[i][j] = dp[i][j-2]
                    
                    # Option 2: Use '*' to match one or more occurrences
                    # This is only possible if current string character matches the character before '*'
                    if s_char == prev_p_char or prev_p_char == '.':
                        # If they match, we can use '*' to match current character
                        # Result depends on whether s[0:i-1] matches p[0:j] (match one more occurrence)
                        dp[i][j] = dp[i][j] or dp[i-1][j]
        
        # Return whether the entire string matches the entire pattern
        return dp[s_len][p_len]