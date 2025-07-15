class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Initialize pointer for string s - tracks which character we're looking for
        s_pointer = 0
        
        # If s is empty, it's always a subsequence of any string
        if len(s) == 0:
            return True
        
        # Traverse through string t with t_pointer
        for t_pointer in range(len(t)):
            # If current character in t matches the character we're looking for in s
            if t[t_pointer] == s[s_pointer]:
                # Move to next character in s that we need to find
                s_pointer += 1
                
                # If we've found all characters of s in order, return True
                if s_pointer == len(s):
                    return True
        
        # If we've gone through all of t but haven't found all characters of s
        # then s is not a subsequence of t
        return False