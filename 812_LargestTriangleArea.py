class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        max_area = 0.0   # store the maximum area
        n = len(points)  # total number of points

        # try all possible triplets of points
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    # update max_area with the largest area found
                    max_area = max(max_area, self.area(points[i], points[j], points[k]))
        
        return max_area  # return the biggest area found

    def area(self, a, b, c):
        # calculate area using shoelace formula
        return abs(
            a[0] * (b[1] - c[1]) +  # x1 * (y2 - y3)
            b[0] * (c[1] - a[1]) +  # x2 * (y3 - y1)
            c[0] * (a[1] - b[1])    # x3 * (y1 - y2)
        ) / 2.0  # divide by 2 to get triangle area
