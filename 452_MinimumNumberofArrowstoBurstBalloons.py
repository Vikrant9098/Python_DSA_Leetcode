class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        if not points:
            return 0  # No balloons, no arrows needed

        # Sort balloons by their end position (greedy approach)
        points.sort(key=lambda x: x[1])

        arrows = 1  # At least one arrow is needed
        last_arrow_pos = points[0][1]  # Place the first arrow at the end of the first balloon

        # Iterate through the rest of the balloons
        for i in range(1, len(points)):
            start, end = points[i]

            if start > last_arrow_pos:
                # If current balloon starts after the last arrow, need new arrow
                arrows += 1
                last_arrow_pos = end  # Place arrow at end of this balloon

            # else: balloon overlaps, gets burst by the existing arrow

        return arrows
