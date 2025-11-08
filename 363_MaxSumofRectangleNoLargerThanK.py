from copy import deepcopy
import bisect


class Solution(object):
    @staticmethod
    def transpose(matrix):
        # Transpose the matrix (convert rows to columns)
        return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]

    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # If rows > columns, transpose to reduce complexity
        if len(matrix) > len(matrix[0]):
            matrix = self.transpose(matrix)

        numRows = len(matrix)        # total rows
        numCols = len(matrix[0])     # total columns

        assert numCols >= numRows    # ensure more columns than rows (optimization)

        partialSumMatrix = deepcopy(matrix)  # create copy to store prefix sums

        # build prefix sum matrix
        for i in range(numRows):
            for j in range(numCols):
                if i > 0:            # add value from top cell
                    partialSumMatrix[i][j] += partialSumMatrix[i - 1][j]
                if j > 0:            # add value from left cell
                    partialSumMatrix[i][j] += partialSumMatrix[i][j - 1]
                if i > 0 and j > 0:  # remove double-counted area
                    partialSumMatrix[i][j] -= partialSumMatrix[i - 1][j - 1]

        # check all row pairs (firstRow to lastRow)
        ret = float("-inf")          # store max sum <= k
        for firstRow in range(numRows):
            for lastRow in range(firstRow, numRows):
                sortedSums = [0]     # stores prefix sums in sorted order

                # loop through each column
                for j in range(numCols):
                    # calculate current rectangle sum up to column j
                    nextSum = partialSumMatrix[lastRow][j] - (partialSumMatrix[firstRow - 1][j] if firstRow > 0 else 0)

                    # find smallest prefix >= nextSum - k
                    ind = bisect.bisect_left(sortedSums, nextSum - k)
                    if ind < len(sortedSums):
                        # update max sum if within limit
                        ret = max(ret, nextSum - sortedSums[ind])
                        if ret == k:  # early stop if perfect match
                            return ret

                    # insert current sum in sorted order
                    bisect.insort(sortedSums, nextSum)

        return ret  # return max rectangle sum ≤ k
