class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        """
        :type n: int
        :type m: int
        :type hBars: List[int]
        :type vBars: List[int]
        :rtype: int
        """

        def maxSpan(bars):
            # Sort the bars to find consecutive positions
            bars.sort()

            res = 1      # Stores maximum consecutive streak
            streak = 1   # Current consecutive streak

            for i in range(1, len(bars)):
                # Check if bars are consecutive
                if bars[i] - bars[i - 1] == 1:
                    streak += 1
                else:
                    streak = 1

                # Update maximum streak
                res = max(res, streak)

            return res + 1  # Add 1 to include grid edge

        # Find minimum span and return square area
        return min(maxSpan(hBars), maxSpan(vBars)) ** 2
