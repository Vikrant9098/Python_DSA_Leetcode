class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        ans, prev, cur = 0, 0, 1   # ans = result, prev = previous group length, cur = current group length
        
        for i in range(1, len(s)):   # Start from second character
            
            if s[i] != s[i - 1]:   # If character changes (new group starts)
                
                ans += min(prev, cur)   # Add valid substrings from previous and current groups
                prev = cur              # Update previous group length
                cur = 1                 # Reset current group length
            
            else:   # If same character continues
                cur += 1   # Increase current group length
        
        ans += min(prev, cur)   # Add contribution of the last group
        
        return ans   # Return total count
