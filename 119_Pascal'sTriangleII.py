class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # Create a list to store the current row
        row = []

        # Loop from 0 to rowIndex to build each row
        for i in range(rowIndex + 1):
            # Add 1 at the end of the list for every new row
            row.append(1)

            # Update elements from right to left to avoid overwriting needed values
            for j in range(i - 1, 0, -1):
                # Each element is the sum of the two elements above it
                row[j] = row[j] + row[j - 1]

        # Return the final row (the rowIndex-th row)
        return row
