class Solution:
    def countCoveredBuildings(self, n, buildings):
        from bisect import bisect_left   # used for binary search on sorted lists

        rowToCol = {}   # map: row to list of columns
        colToRow = {}   # map: column to list of rows

        # Fill rowToCol and colToRow with building positions
        for x, y in buildings:
            rowToCol.setdefault(x, []).append(y)   # add column y to row x
            colToRow.setdefault(y, []).append(x)   # add row x to column y

        # Sort all column lists for each row
        for v in rowToCol.values():
            v.sort()

        # Sort all row lists for each column
        for v in colToRow.values():
            v.sort()

        cnt = 0   # count covered buildings

        # Check each building
        for x, y in buildings:
            cols = rowToCol[x]  # list of columns in same row
            rows = colToRow[y]  # list of rows in same column

            i = bisect_left(cols, y)   # index of y in sorted cols
            left = cols[i-1] if i > 0 else None      # building to the left
            right = cols[i+1] if i+1 < len(cols) else None   # building to the right

            j = bisect_left(rows, x)   # index of x in sorted rows
            up = rows[j-1] if j > 0 else None        # building above
            down = rows[j+1] if j+1 < len(rows) else None    # building below

            # Check if building has all four neighbors
            if left is not None and right is not None and up is not None and down is not None:
                cnt += 1   # count it as covered

        return cnt   # return total covered buildings
