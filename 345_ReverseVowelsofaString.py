class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Define set of vowels (both lowercase and uppercase) for O(1) lookup
        vowels = set('aeiouAEIOU')
        
        # Convert string to list since strings are immutable in Python
        s_list = list(s)
        
        # Initialize two pointers - one at start and one at end
        left = 0
        right = len(s_list) - 1
        
        # Use two-pointer technique to find and swap vowels
        while left < right:
            # Move left pointer until we find a vowel
            while left < right and s_list[left] not in vowels:
                left += 1
            
            # Move right pointer until we find a vowel
            while left < right and s_list[right] not in vowels:
                right -= 1
            
            # If both pointers are at vowels, swap them
            if left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                # Move both pointers towards center
                left += 1
                right -= 1
        
        # Convert list back to string and return
        return ''.join(s_list)