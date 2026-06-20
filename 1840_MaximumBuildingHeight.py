class Solution(object):
    def maxBuilding(self, n, restrictions):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :rtype: int
        """

        # Building 1 must always have height 0
        restrictions.append([1, 0])

        # Sort restrictions based on building number
        restrictions.sort()

        # Total number of restricted buildings
        m = len(restrictions)

        def yCap(x1, y1, x2, y2):
            """
            Returns the maximum valid height at building x2
            considering the restriction at x1.

            Since adjacent buildings can differ by at most 1,
            height at x2 cannot exceed:
                y1 + abs(x2 - x1)

            We also cannot exceed its own restriction y2.
            """
            return min(y2, y1 + abs(x2 - x1))

        def yPeak(x1, y1, x2, y2):
            """
            Finds the highest possible building height between
            two restricted buildings (x1, y1) and (x2, y2).

            The peak occurs where the increasing slope from one side
            meets the decreasing slope from the other side.

            Formula:
                (y1 + y2 + distance) // 2
            """
            return (y1 + y2 + x2 - x1) >> 1

        # ---------------------------------------------------------
        # Left-to-right pass
        # Tighten each restriction using the previous restriction.
        # ---------------------------------------------------------
        for i in range(1, m):
            restrictions[i][1] = yCap(
                restrictions[i - 1][0], restrictions[i - 1][1],
                restrictions[i][0], restrictions[i][1]
            )

        # ---------------------------------------------------------
        # Right-to-left pass
        # Tighten each restriction using the next restriction.
        # This ensures all restrictions are mutually consistent.
        # ---------------------------------------------------------
        for i in range(m - 2, -1, -1):
            restrictions[i][1] = yCap(
                restrictions[i + 1][0], restrictions[i + 1][1],
                restrictions[i][0], restrictions[i][1]
            )

        # Stores the maximum height achievable anywhere
        res = 0

        # ---------------------------------------------------------
        # For every pair of consecutive restricted buildings,
        # compute the highest peak possible between them.
        # ---------------------------------------------------------
        for i in range(1, m):
            res = max(
                res,
                yPeak(
                    restrictions[i - 1][0], restrictions[i - 1][1],
                    restrictions[i][0], restrictions[i][1]
                )
            )

        # ---------------------------------------------------------
        # After the last restricted building, heights can keep
        # increasing by 1 until building n.
        # Maximum height there:
        #     last_height + (n - last_position)
        # ---------------------------------------------------------
        return max(
            res,
            restrictions[-1][1] + n - restrictions[-1][0]
        )