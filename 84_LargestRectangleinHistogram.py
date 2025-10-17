class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []  # stack to store indices of bars
        max_area = 0  # variable to store maximum area
        n = len(heights)

        for i in range(n + 1):
            # use 0 height for a virtual bar at the end
            h = 0 if i == n else heights[i]

            # calculate area for bars taller than current
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]  # height of rectangle
                width = i if not stack else i - stack[-1] - 1  # width of rectangle
                max_area = max(max_area, height * width)  # update max area

            stack.append(i)  # push current index to stack

        return max_area  # return maximum area
