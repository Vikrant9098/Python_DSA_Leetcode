class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Edge case: if either string is empty or s is smaller than t, return empty string
        if not s or not t or len(s) < len(t):
            return ""
        
        from collections import Counter
        
        # Frequency map of characters in t
        t_map = Counter(t)
        # Number of unique characters in t that need to be matched in window
        required = len(t_map)
        
        # Initialize left and right pointers of sliding window
        left, right = 0, 0
        # Number of unique characters in current window that meet required frequency
        formed = 0
        # Frequency map for characters in current window
        window_counts = {}
        
        # Result tuple to store minimum window (window length, left index, right index)
        ans = (float("inf"), None, None)
        
        # Expand the window by moving right pointer
        while right < len(s):
            char = s[right]  # Current character at right pointer
            window_counts[char] = window_counts.get(char, 0) + 1  # Add/update frequency in window
            
            # If current char frequency matches required frequency in t
            if char in t_map and window_counts[char] == t_map[char]:
                formed += 1  # Increment formed count
            
            # Try shrinking the window from left while all required characters are matched
            while left <= right and formed == required:
                char = s[left]  # Character at left pointer
                
                # Update answer if current window is smaller than previous minimum
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                
                # Remove the leftmost character from window
                window_counts[char] -= 1
                # If removed character was required and frequency falls below requirement
                if char in t_map and window_counts[char] < t_map[char]:
                    formed -= 1  # One less unique character fully matched
                
                left += 1  # Move left pointer forward
            
            right += 1  # Expand window by moving right pointer forward
        
        # Return empty string if no valid window found, else return minimum window substring
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]
