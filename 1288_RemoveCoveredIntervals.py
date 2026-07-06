class Solution:
    def removeCoveredIntervals(self, A: List[List[int]]) -> int:

        # Sort by:
        # 1. Start in ascending order
        # 2. End in descending order (for same start)
        A.sort(key=lambda x: (x[0], -x[1]))

        # res = number of remaining (not covered) intervals
        # r = farthest end seen so far
        res = r = 0

        # Traverse all intervals
        for st, end in A:

            # If current interval extends beyond the farthest end,
            # it is not covered by any previous interval
            res += end > r

            # Update the farthest end reached so far
            r = max(r, end)

        # Return the number of intervals that are not covered
        return res