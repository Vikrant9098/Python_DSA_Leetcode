class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        m = len(boxGrid)          # rows
        n = len(boxGrid[0])       # cols

        # create empty rotated grid (transpose size)
        result = [["" for _ in range(m)] for _ in range(n)]

        # transpose the matrix
        for i in range(n):
            for j in range(m):
                result[i][j] = boxGrid[j][i]

        # reverse each row -> 90° clockwise rotation
        for i in range(n):
            result[i].reverse()

        # apply gravity column-wise
        for j in range(m):
            for i in range(n - 1, -1, -1):  # bottom → top
                if result[i][j] == ".":     # empty cell
                    next_stone = -1

                    # find nearest stone above (no obstacle in between)
                    for k in range(i - 1, -1, -1):
                        if result[k][j] == "*":
                            break          # obstacle blocks
                        if result[k][j] == "#":
                            next_stone = k
                            break

                    # move stone down
                    if next_stone != -1:
                        result[next_stone][j] = "."
                        result[i][j] = "#"

        return result