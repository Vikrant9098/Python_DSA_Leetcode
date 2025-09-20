class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        # Step 1: Find dimensions of the matrix
        m, n = len(matrix), len(matrix[0])   # 'm' = number of rows, 'n' = number of columns

        # Step 2: Check if the first row already has any zero
        # This is important because we will use the first row as markers later,
        # so we need to remember its original state separately.
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))

        # Step 3: Check if the first column already has any zero
        # Similarly, we will use the first column as markers, so track its original state.
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))

        # Step 4: Traverse the matrix (except the first row and column)
        # If we encounter a zero at (i, j), we mark its row and column
        # by setting matrix[i][0] and matrix[0][j] to zero.
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:          # Found a zero inside the matrix
                    matrix[i][0] = 0           # Mark this row for zeroing
                    matrix[0][j] = 0           # Mark this column for zeroing

        # Step 5: Traverse again (except first row/column)
        # If either its row OR its column is marked zero,
        # then make this cell zero.
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0           # Overwrite with zero

        # Step 6: Now handle the first row separately
        # If the first row originally had a zero, make the entire row zero.
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Step 7: Handle the first column separately
        # If the first column originally had a zero, make the entire column zero.
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0
