class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Step 1: Define a set containing both lowercase and uppercase vowels
        vowels = set("aeiouAEIOU")  
        
        # Step 2: Convert the input string into a list of characters (mutable)
        chars = list(s)             
        
        # Step 3: Extract only the vowels from the string into a list
        vowel_list = [c for c in chars if c in vowels]
        
        # Step 4: Sort the vowels by their ASCII values (e.g., 'A' < 'E' < 'a')
        vowel_list.sort()
        
        # Step 5: Initialize an index to track which sorted vowel to insert next
        idx = 0  
        
        # Step 6: Traverse the string, replacing vowels with sorted ones
        for i in range(len(chars)):
            # If the current character is a vowel
            if chars[i] in vowels:
                # Replace it with the next sorted vowel
                chars[i] = vowel_list[idx]
                # Move to the next vowel in the sorted list
                idx += 1
        
        # Step 7: Join the modified list back into a string and return
        return "".join(chars)
