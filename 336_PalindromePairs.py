class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # Create a map of reversed word → its index
        word_map = {w[::-1]: i for i, w in enumerate(words)}

        # List to store all palindrome pairs
        res = []

        # Function to check if a string is palindrome
        def is_palindrome(s):
            # Return True if string equals its reverse
            return s == s[::-1]

        # Loop through each word and its index
        for i, word in enumerate(words):
            # Try every possible split of the word
            for j in range(len(word) + 1):
                # Left part of the split
                left = word[:j]
                # Right part of the split
                right = word[j:]

                # Case 1: If left is palindrome
                if is_palindrome(left):
                    # Check if reversed right part exists in map
                    if right in word_map and word_map[right] != i:
                        # Add pair (reversed right index, current word index)
                        res.append([word_map[right], i])

                # Case 2: If right is palindrome
                # Avoid duplicate checking when j == len(word)
                if j < len(word) and is_palindrome(right):
                    # Check if reversed left part exists in map
                    if left in word_map and word_map[left] != i:
                        # Add pair (current word index, reversed left index)
                        res.append([i, word_map[left]])

        # Return all found palindrome pairs
        return res
