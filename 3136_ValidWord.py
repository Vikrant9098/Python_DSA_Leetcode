class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # Check if word has at least 3 characters
        if len(word) < 3:
            return False
        
        # Define vowels string for easy checking
        vowels = "aeiouAEIOU"
        
        has_vowel = False
        has_consonant = False
        
        # Check each character in the word
        for char in word:
            # Check if character is valid (only letters and digits allowed)
            if not char.isalnum():
                return False
            
            # Check if character is a letter (not a digit)
            if char.isalpha():
                # Check if it's a vowel or consonant
                if char in vowels:
                    has_vowel = True
                else:
                    has_consonant = True
        
        # Word is valid if it has at least one vowel and one consonant
        return has_vowel and has_consonant