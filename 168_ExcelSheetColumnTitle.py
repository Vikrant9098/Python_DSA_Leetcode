class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = ""

        # Loop until columnNumber becomes 0
        while columnNumber > 0:
            columnNumber -= 1  # Adjust to make it 0-indexed
            remainder = columnNumber % 26  # Find remainder
            letter = chr(ord('A') + remainder)  # Convert remainder to corresponding letter
            result = letter + result  # Prepend letter to result
            columnNumber //= 26  # Move to next position

        return result
