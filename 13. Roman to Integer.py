class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Step 1: Create a mapping of Roman numerals to integers
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Step 2: Initialize result variable
        total = 0

        # Step 3: Loop through each character in the string
        for i in range(len(s)):
            # If current value is smaller than the next value → subtract
            if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            else:
                # Otherwise just add the value
                total += roman_map[s[i]]

        # Step 4: Return final integer value
        return total
