class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Edge case: if numRows is 1 or greater than string length
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create arrays to store characters for each row
        rows = [''] * numRows
        
        # Track current row and direction
        current_row = 0
        going_down = False
        
        # Process each character
        for char in s:
            # Add character to current row
            rows[current_row] += char
            
            # Change direction at top or bottom
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Move to next row
            current_row += 1 if going_down else -1
        
        # Concatenate all rows
        return ''.join(rows)