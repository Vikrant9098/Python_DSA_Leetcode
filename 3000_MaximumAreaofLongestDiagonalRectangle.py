class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        maxDiagonal = 0
        maxArea = 0

        for length, width in dimensions:
            diagonalSq = length * length + width * width
            area = length * width

            if diagonalSq > maxDiagonal:
                maxDiagonal = diagonalSq
                maxArea = area
            elif diagonalSq == maxDiagonal:
                maxArea = max(maxArea, area)

        return maxArea
