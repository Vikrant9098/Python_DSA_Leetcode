class Spreadsheet(object):

    def __init__(self, rows):
        """
        :type rows: int
        Initialize a spreadsheet with given rows and 26 columns (A-Z).
        All cells start with value 0.
        """
        # Dictionary to store cell values
        # Key will be a string like "A1", "B2"
        # Value will be the integer stored in that cell
        self.cells = {}

        # Store number of rows (not used much, but kept for clarity)
        self.rows = rows

    def setCell(self, cell, value):
        """
        :type cell: str  (like "A1", "B10")
        :type value: int
        :rtype: None
        Set the specified cell to a given value.
        """
        # Directly update the dictionary with cell value
        self.cells[cell] = value

    def resetCell(self, cell):
        """
        :type cell: str
        :rtype: None
        Reset the specified cell back to 0.
        """
        # If the cell exists in dictionary, reset its value to 0
        # (If cell doesn’t exist, do nothing because it's already considered 0)
        if cell in self.cells:
            self.cells[cell] = 0

    def getValue(self, formula):
        """
        :type formula: str (like "=A1+B2" or "=5+7")
        :rtype: int
        Evaluate the formula and return the result.
        """
        # Remove '=' at the start of formula string
        expression = formula[1:]

        # Split expression into two parts around '+'
        # Example: "A1+B2" -> part1 = "A1", part2 = "B2"
        part1, part2 = expression.split('+')

        # Get the numeric value of each part and return their sum
        return self._getValueFromToken(part1) + self._getValueFromToken(part2)

    def _getValueFromToken(self, token):
        """
        Helper function to interpret whether the token is:
        - A number (like "5")
        - A cell reference (like "A1")
        """
        # If the token is a number (string of digits), just convert and return it
        if token.isdigit():
            return int(token)

        # Otherwise, it's a cell reference like "A1" or "B2"
        # If cell not set explicitly, return 0 by default
        return self.cells.get(token, 0)
