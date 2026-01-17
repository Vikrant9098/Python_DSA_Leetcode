class Solution:
    # Define Solution class

    def largestSquareArea(self, bottomLeft, topRight):
        # Function to find the largest square area from overlapping rectangles

        ans = 0
        # Stores the maximum square side length found

        n = len(bottomLeft)
        # Number of rectangles

        for i in range(n):
            # Loop for the first rectangle

            firstRectBL = bottomLeft[i]
            # Bottom-left corner of first rectangle

            firstRectTR = topRight[i]
            # Top-right corner of first rectangle

            for j in range(i + 1, n):
                # Loop for second rectangle (avoid repeat pairs)

                secondRectBL = bottomLeft[j]
                # Bottom-left corner of second rectangle

                secondRectTR = topRight[j]
                # Top-right corner of second rectangle

                if secondRectBL[0] >= firstRectTR[0] or secondRectTR[0] <= firstRectBL[0]:
                    # Check if rectangles do NOT overlap on x-axis
                    continue
                    # Skip this pair if no horizontal overlap

                if secondRectTR[1] <= firstRectBL[1] or secondRectBL[1] >= firstRectTR[1]:
                    # Check if rectangles do NOT overlap on y-axis
                    continue
                    # Skip this pair if no vertical overlap

                pntAx = max(firstRectBL[0], secondRectBL[0])
                # Left x-coordinate of overlapping area

                pntAy = max(firstRectBL[1], secondRectBL[1])
                # Bottom y-coordinate of overlapping area

                pntBx = min(firstRectTR[0], secondRectTR[0])
                # Right x-coordinate of overlapping area

                pntBy = min(firstRectTR[1], secondRectTR[1])
                # Top y-coordinate of overlapping area

                sideA = pntBx - pntAx
                # Width of overlapping rectangle

                sideB = pntBy - pntAy
                # Height of overlapping rectangle

                ans = max(ans, min(sideA, sideB))
                # Take the largest possible square side from overlap

        return ans ** 2
        # Return area of the largest square
