class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary to store the last index of each character
        char_index = {}
        
        # Start pointer of the sliding window
        left = 0
        
        # Variable to store maximum length
        max_len = 0
        
        # Iterate over the string with right pointer
        for right in range(len(s)):
            # If character is already in the dictionary and inside current window
            if s[right] in char_index and char_index[s[right]] >= left:
                # Move the left pointer to one position right of the duplicate character
                left = char_index[s[right]] + 1
            
            # Update the latest index of the character
            char_index[s[right]] = right
            
            # Update max_len with current window size
            max_len = max(max_len, right - left + 1)
        
        return max_len
