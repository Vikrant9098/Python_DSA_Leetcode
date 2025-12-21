class Solution(object):
    # Solution class

    def minDeletionSize(self, strs):
        # Function to find minimum columns to delete

        n = len(strs)
        # Number of strings (rows)

        m = len(strs[0])
        # Length of each string (columns)

        resolved = [False] * (n - 1)
        # resolved[i] = True means
        # strs[i] is already smaller than strs[i+1]

        unresolved = n - 1
        # Count of row pairs whose order is not fixed

        deletions = 0
        # Count of deleted columns

        for col in range(m):
            # Traverse columns left to right

            if unresolved == 0:
                # Stop if all row orders are fixed
                break

            need_delete = False
            # Flag to decide whether to delete this column

            for row in range(n - 1):
                # Compare adjacent rows

                if not resolved[row] and strs[row][col] > strs[row + 1][col]:
                    # If lexicographical order breaks
                    need_delete = True
                    # Mark column for deletion
                    break
                    # Stop checking further rows

            if need_delete:
                # If column breaks order
                deletions += 1
                # Increase delete count
                continue
                # Skip this column

            for row in range(n - 1):
                # Update resolved row pairs
                if not resolved[row] and strs[row][col] < strs[row + 1][col]:
                    # If this column fixes order
                    resolved[row] = True
                    # Mark as resolved
                    unresolved -= 1
                    # Reduce unresolved count

        return deletions
        # Return total number of deleted columns
