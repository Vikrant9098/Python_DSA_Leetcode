class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # If matrix is empty, return 0
        if not matrix:
            return 0

        cols = len(matrix[0])  # Number of columns
        heights = [0] * cols   # Array to store histogram heights
        max_area = 0           # To store maximum rectangle area

        # Go through each row
        for row in matrix:
            # Update histogram heights
            for j in range(cols):
                # If '1', add 1 to height; else reset to 0
                if row[j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            # Update max area for current histogram
            max_area = max(max_area, self.largestRectangleArea(heights))

        # Return final maximum area
        return max_area

    # Helper function to find largest rectangle in histogram
    def largestRectangleArea(self, heights):
        stack = []      # Stack to store indices
        max_area = 0    # To store maximum area
        n = len(heights)

        # Loop through all bars
        for i in range(n + 1):
            # Handle last bar as height 0
            h = 0 if i == n else heights[i]

            # While stack top is taller than current height
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]  # Get height
                # Width = current index - previous smaller - 1
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)  # Update max area

            # Push current index to stack
            stack.append(i)

        # Return largest area
        return max_area
