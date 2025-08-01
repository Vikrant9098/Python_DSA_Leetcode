class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []  # This will hold all the rows of Pascal's Triangle

        for i in range(numRows):
            # Start each row with 1
            row = [1] * (i + 1)

            # Compute the values in between the 1s, if any
            for j in range(1, i):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]

            # Append the constructed row to the result
            result.append(row)

        return result
