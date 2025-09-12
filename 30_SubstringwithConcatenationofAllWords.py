class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # List to store the starting indices of valid substrings
        result = []
        
        # Edge case: if input string or words list is empty, return empty result
        if not s or not words:
            return result
        
        # Length of each word (all words are the same length)
        word_length = len(words[0])
        # Number of words
        word_count = len(words)
        # Total length of substring we are looking for
        substring_length = word_length * word_count
        
        # If s is smaller than required substring length, no possible match
        if len(s) < substring_length:
            return result
        
        # Build frequency map of words (word → count)
        from collections import Counter
        word_map = Counter(words)
        
        # Try starting from every offset within word_length
        # Example: if word_length = 3, we try indices 0, 1, 2
        for i in range(word_length):
            left = i          # Left pointer of the sliding window
            count = 0         # Number of valid words matched so far
            window_map = {}   # Current window word frequency
            
            # Move right pointer in steps of word_length
            for right in range(i, len(s) - word_length + 1, word_length):
                # Extract the word of size word_length
                word = s[right:right + word_length]
                
                # If the word exists in the required word_map
                if word in word_map:
                    # Add/update the count of this word in current window
                    window_map[word] = window_map.get(word, 0) + 1
                    count += 1
                    
                    # If word occurs more times than required, shrink window from the left
                    while window_map[word] > word_map[word]:
                        left_word = s[left:left + word_length]
                        window_map[left_word] -= 1
                        left += word_length
                        count -= 1
                    
                    # If current window contains exactly all words → add starting index
                    if count == word_count:
                        result.append(left)
                else:
                    # If word not in word_map, reset window
                    window_map.clear()
                    count = 0
                    left = right + word_length  # move left pointer after this invalid word
        
        # Return all valid starting indices
        return result
