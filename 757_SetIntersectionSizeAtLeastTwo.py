class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        # Sort intervals by end increasing, and if same end, start decreasing
        intervals.sort(key=lambda x: (x[1], -x[0]))

        ans = 0          # total numbers added
        a, b = -1, -1    # two largest selected numbers so far

        for l, r in intervals:   # loop through each interval
            if l > b:            # no selected number inside current interval
                a = r - 1        # choose r-1 as first number
                b = r            # choose r as second number
                ans += 2         # we added 2 numbers
            elif l > a:          # only one selected number inside
                a = b            # shift b to a (second largest)
                b = r            # choose r as the new number
                ans += 1         # added 1 number
            # else: already has 2 numbers → no action

        return ans
