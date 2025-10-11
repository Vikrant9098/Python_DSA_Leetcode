class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict  # for counting slopes

        # Helper function to compute gcd
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b  # standard Euclidean algorithm
            return a

        n = len(points)
        if n <= 2:
            return n  # 0, 1, or 2 points always lie on the same line

        max_points = 0  # store overall maximum points

        # Loop through each point as reference
        for i in range(n):
            slope_count = defaultdict(int)  # map to count points with same slope
            duplicates = 0  # count points identical to points[i]
            curr_max = 0  # max points on a line with points[i] as reference

            # Compare reference point with every other point
            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]  # difference in x
                dy = points[j][1] - points[i][1]  # difference in y

                if dx == 0 and dy == 0:
                    duplicates += 1  # same point, increase duplicates
                    continue

                # Reduce slope to simplest fraction using gcd
                g = gcd(dy, dx)
                dx //= g
                dy //= g

                # Use tuple (dx, dy) as slope key
                slope = (dx, dy)
                slope_count[slope] += 1  # increment count for this slope
                curr_max = max(curr_max, slope_count[slope])  # update current max

            # Add duplicates and reference point itself
            max_points = max(max_points, curr_max + duplicates + 1)

        return max_points  # return overall maximum points on a line
