class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1  # Two pointers at start and end

        while left < right:
            # Move left pointer until it's alphanumeric
            while left < right and not s[left].isalnum():
                left += 1
            # Move right pointer until it's alphanumeric
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare lowercase characters
            if s[left].lower() != s[right].lower():
                return False  # Not a palindrome

            left += 1
            right -= 1

        return True  # Passed all checks, it's a palindrome
