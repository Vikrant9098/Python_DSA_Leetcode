class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()  # Split the string into words
        if len(pattern) != len(words):  # Length mismatch → cannot follow pattern
            return False

        char_to_word = {}  # Map from pattern char to word
        word_to_char = {}  # Map from word to pattern char

        for c, w in zip(pattern, words):
            # If character already mapped, check if it matches the current word
            if c in char_to_word:
                if char_to_word[c] != w:
                    return False
            else:
                char_to_word[c] = w  # Add new mapping

            # If word already mapped, check if it matches the current character
            if w in word_to_char:
                if word_to_char[w] != c:
                    return False
            else:
                word_to_char[w] = c  # Add new mapping

        return True  # All mappings consistent → pattern matches
