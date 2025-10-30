class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """
        # Area of first rectangle
        areaA = (ax2 - ax1) * (ay2 - ay1)
        
        # Area of second rectangle
        areaB = (bx2 - bx1) * (by2 - by1)
        
        # Overlapping width
        overlapWidth = min(ax2, bx2) - max(ax1, bx1)
        
        # Overlapping height
        overlapHeight = min(ay2, by2) - max(ay1, by1)
        
        overlapArea = 0  # Initialize overlap area
        
        # Check if rectangles actually overlap
        if overlapWidth > 0 and overlapHeight > 0:
            overlapArea = overlapWidth * overlapHeight
        
        # Total area covered by both rectangles
        return areaA + areaB - overlapArea
