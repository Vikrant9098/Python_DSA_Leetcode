class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0

        # Iterate through each character in the column title
        for c in columnTitle:
            # Convert character to number
            value = ord(c) - ord('A') + 1
            # Multiply previous result by 26 and add current value
            result = result * 26 + value

        return result
