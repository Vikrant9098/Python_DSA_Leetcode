class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        # Create 9 sets for rows (to track used numbers in each row)
        rows = [set() for _ in range(9)]

        # Create 9 sets for columns (to track used numbers in each column)
        cols = [set() for _ in range(9)]

        # Create 9 sets for 3x3 boxes (to track used numbers in each sub-box)
        boxes = [set() for _ in range(9)]

        # Loop through each row of the Sudoku board
        for i in range(9):                       # i = row index (0 to 8)

            # Loop through each column of the Sudoku board
            for j in range(9):                   # j = column index (0 to 8)

                # Get the current cell value
                c = board[i][j]

                # If the cell is empty '.', skip it (no need to check)
                if c == '.':
                    continue

                # Calculate 3x3 box index
                # (i // 3) gives the box row (0,1,2)
                # (j // 3) gives the box column (0,1,2)
                # Multiply box row by 3 and add box column → unique index (0–8)
                boxIndex = (i // 3) * 3 + (j // 3)

                # If the current number already exists in the row → invalid Sudoku
                if c in rows[i]:
                    return False

                # If the current number already exists in the column → invalid Sudoku
                if c in cols[j]:
                    return False

                # If the current number already exists in the 3x3 box → invalid Sudoku
                if c in boxes[boxIndex]:
                    return False

                # Otherwise, mark this number as seen in the row
                rows[i].add(c)

                # Mark this number as seen in the column
                cols[j].add(c)

                # Mark this number as seen in the 3x3 box
                boxes[boxIndex].add(c)

        # If we checked all cells without conflicts, the Sudoku is valid
        return True
