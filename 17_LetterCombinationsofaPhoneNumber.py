class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # Handle empty input case
        if not digits:
            return []
        
        # Map digits to their corresponding letters (like phone keypad)
        digit_to_letters = {
            '2': 'abc',
            '3': 'def', 
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        # Initialize result with empty string to start combinations
        result = ['']
        
        # For each digit in input, build combinations iteratively
        for digit in digits:
            # Get letters for current digit
            letters = digit_to_letters[digit]
            # Create new combinations by appending each letter to existing combinations
            result = [combo + letter for combo in result for letter in letters]
        
        return result