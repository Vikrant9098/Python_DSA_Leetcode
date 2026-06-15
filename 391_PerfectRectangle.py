class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """

        # Stores the total area covered by all small rectangles
        area = 0

        # Stores corner points.
        # A corner appearing twice will be removed,
        # leaving only the outer boundary corners.
        corner_point = set()

        # Process each rectangle
        for x, y, a, b in rectangles:

            # Add current rectangle's area
            area += (a - x) * (b - y)

            # Get all 4 corners of the current rectangle
            for point in [(x, y), (x, b), (a, y), (a, b)]:

                # If the corner already exists,
                # remove it because it is shared by two rectangles
                if point in corner_point:
                    corner_point.remove(point)
                else:
                    # Otherwise add it
                    corner_point.add(point)

        # For a perfect rectangle cover,
        # only the 4 outermost corners should remain
        if len(corner_point) != 4:
            return False

        # Sort corners by x-coordinate, then y-coordinate
        corner_point = sorted(corner_point, key=lambda p: (p[0], p[1]))

        # Bottom-left corner of the large rectangle
        min_x, min_y = corner_point[0]

        # Top-right corner of the large rectangle
        max_x, max_y = corner_point[-1]

        # Calculate area of the bounding rectangle
        bounding_area = (max_x - min_x) * (max_y - min_y)

        # The total area of all rectangles must equal
        # the area of the bounding rectangle
        return area == bounding_area