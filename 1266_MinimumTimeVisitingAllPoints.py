class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0                          # Store total time

        for i in range(1, len(points)): # Loop from second point
            prev, cur = points[i - 1 : i + 1]  # Previous and current point
            ans += max(                  # Add max distance needed
                map(abs, (
                    prev[0] - cur[0],    # x difference
                    prev[1] - cur[1]     # y difference
                ))
            )

        return ans                       # Return total time
