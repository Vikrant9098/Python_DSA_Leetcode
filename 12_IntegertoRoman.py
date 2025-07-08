class Solution(object):
    def intToRoman(self, num):
        # Create a list of (value, symbol) pairs sorted from largest to smallest
        # This includes all basic symbols and subtractive forms (like 900='CM', 400='CD')
        val_to_roman = [
            (1000, 'M'), (900, 'CM'),  # 1000 and 900 (subtractive form)
            (500, 'D'),  (400, 'CD'),  # 500 and 400 (subtractive form)
            (100, 'C'),  (90, 'XC'),   # 100 and 90 (subtractive form)
            (50, 'L'),   (40, 'XL'),   # 50 and 40 (subtractive form)
            (10, 'X'),   (9, 'IX'),    # 10 and 9 (subtractive form)
            (5, 'V'),    (4, 'IV'),    # 5 and 4 (subtractive form)
            (1, 'I')                   # 1
        ]

        roman = ""  # Start with empty result string

        # Go through each value-symbol pair from largest to smallest
        for value, symbol in val_to_roman:
            # Keep using this symbol while the number is >= its value
            while num >= value:
                roman += symbol  # Add the symbol to result
                num -= value     # Subtract the value from number
        
        # Return the final Roman numeral string
        return roman