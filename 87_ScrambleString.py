class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:           # If both strings are same, return True
            return True
        if len(s1) != len(s2): # If lengths differ, return False
            return False
        memo = {}               # Dictionary to store already checked pairs
        return self.helper(s1, s2, memo)  # Call helper with memo

    def helper(self, s1, s2, memo):
        key = s1 + "," + s2    # Create unique key for pair
        if key in memo:        # If already computed, return stored value
            return memo[key]
        if s1 == s2:           # If strings equal, store True and return
            memo[key] = True
            return True
        if sorted(s1) != sorted(s2):  # If letters differ, store False and return
            memo[key] = False
            return False
        n = len(s1)            # Get length of strings

        for i in range(1, n):  # Try all split positions
            if (self.helper(s1[:i], s2[:i], memo) and    # Case 1: No swap
                self.helper(s1[i:], s2[i:], memo)):
                memo[key] = True    # Store result as True
                return True
            if (self.helper(s1[:i], s2[n - i:], memo) and # Case 2: Swap
                self.helper(s1[i:], s2[:n - i], memo)):
                memo[key] = True    # Store result as True
                return True

        memo[key] = False   # No valid split, store False
        return False        # Return False
